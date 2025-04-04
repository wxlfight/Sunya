# 项目设计文档 (Project Design Document)

本文档详细记录 Sunya 项目的设计决策、系统架构、核心功能规格和技术选型。

## 核心需求概述

项目旨在通过采集用户的多维度数据，利用 AI 分析并以"空性"视角（客观、非情绪化、引导观察）与用户交互，帮助用户更好地理解自身。

主要分为两大业务模块：
1.  **数据准备:** 对接各类数据源（如健康设备、App API），实现自动化、标准化数据采集。
2.  **用户与 AI 交互:** 提供界面（聊天、数据展示、主动通知）让用户与"空性的我"互动。

## 技术架构与选型 (v2 - 2025-04-04 - Hybrid Supabase)

### 整体架构

采用混合架构，结合 Supabase BaaS 和自定义后端服务：

```mermaid
graph TD
    A[用户/浏览器] --> B(前端 - React/Vue);
    B --> C(Supabase);
    C -- Auth, DB, Realtime, Storage --> B;
    C -- Database (Postgres) --> D{自定义后端 - FastAPI};
    B --> D; // 前端也可能直接调用自定义后端特定接口
    D --> E(数据采集适配器);
    E --> F[外部 API - Garmin等];
    E --> C; // 采集结果写入 Supabase DB
    D --> G(AI 核心模块);
    G --> C; // 分析结果写入 Supabase DB 或触发通知
```

*   **前端 (React/Vue):** 用户界面。与 Supabase 交互进行认证、基础数据操作和实时监听；与自定义后端交互触发特定任务或获取复杂结果。
*   **Supabase:** 提供核心 BaaS 功能：
    *   **数据库 (PostgreSQL):** 项目主数据库。
    *   **身份验证 (Auth):** 处理用户注册、登录、会话管理。
    *   **即时 API:** 提供基础的数据 CRUD 接口。
    *   **实时订阅:** 将数据库变更实时推送给前端。
    *   **存储:** (可选) 用于存储文件。
*   **自定义后端 (FastAPI):** 负责 Supabase 无法或不适合处理的逻辑：
    *   **复杂第三方 API 对接:** 实现如 Garmin 的 OAuth 流程和数据拉取逻辑 (通过数据采集适配器)。
    *   **核心 AI 分析:** 运行需要特定 Python 库的分析模型和算法。
    *   **复杂业务逻辑/后台任务:** (可能结合 Celery) 处理需要精细控制或长时间运行的任务。

### 技术选型

| 组件             | 选用技术                               | 主要理由                                                                     |
| ---------------- | -------------------------------------- | ---------------------------------------------------------------------------- |
| 核心 BaaS        | **Supabase**                           | 提供数据库、认证、实时等基础服务，加速开发，遵循"不重复造轮子"原则     |
| 数据库           | Supabase Managed PostgreSQL            | 由 Supabase 提供，免维护，与 Supabase 生态集成                               |
| 身份验证         | Supabase Auth                          | 内建、安全的用户管理方案                                                   |
| 实时通信         | Supabase Realtime                      | 开箱即用的数据库变更实时推送                                                 |
| 自定义后端服务   | Python (FastAPI)                       | 处理复杂逻辑、第三方对接、AI 分析，利用 Python 生态                        |
| 前端             | React / Vue (待定)                     | 同上                                                                       |
| 任务队列 (可选)  | Celery + Redis/RabbitMQ (若需要)       | 用于 FastAPI 服务中处理复杂后台任务                                          |
| 数据采集         | Python (FastAPI 服务的一部分)          | 同上                                                                       |
| AI 核心          | Python (Pandas, Scikit-learn, etc.)    | 同上                                                                       |

### 数据源策略

*   **起点:** 优先实现 **Garmin Connect** 数据对接。
*   **实现方式 (重要变更):** 由于 Garmin 官方 Health API 申请门槛高，我们将采用**非官方 Python 库 `cyberjunky/python-garminconnect`**。该库通过模拟用户登录和抓取 Garmin Connect 网站数据工作。
*   **重大风险:**
    *   **脆弱性:** 该方法依赖网站结构，Garmin 更新可能导致服务中断。
    *   **违反 ToS:** 可能违反 Garmin 服务条款，存在账户风险。
    *   **安全责任:** 需要处理用户 Garmin 用户名/密码，必须采取严格的安全措施（如加密存储）。
*   **适配器模式:** 数据采集适配器仍将由 FastAPI 服务实现，负责调用 `python-garminconnect` 库，处理认证（用户名/密码），获取数据，并将其转换为统一模型写入 Supabase 数据库。
*   **未来扩展:** 设计上仍考虑适配器模式，以便未来可能接入 Google Fit, Apple HealthKit 等官方 API。

*(此文档将在项目进展中逐步填充)* 