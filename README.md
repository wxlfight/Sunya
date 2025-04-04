# Sunya: AI and Emptiness

## Core Philosophy

This project explores the possibility of combining the philosophical concept of "Emptiness" (Śūnyatā) with Artificial Intelligence (AI). "Emptiness" is understood here as a state of **profound tranquility**, where an individual can maintain distance from their emotions without being overwhelmed by them, thus observing and understanding reality more clearly.

The core idea is to create an AI application that serves as a digital manifestation of the user's "other self" – an "Emptiness Self".

## Project Goals

1.  **Data Acquisition:** Collect user behavioral data and subjective experience records from the real world (e.g., journals, mood feedback, event descriptions).
2.  **AI Analysis & Modeling:** Utilize AI to analyze the collected data, identifying the user's emotional patterns, behavioral habits, and reaction triggers. Train AI models to simulate the "Emptiness" perspective.
3.  **Presentation of Emptiness:** Through the application interface, present the user with a more objective, less emotionally colored perspective, possibly by rephrasing events, offering reflective dialogue, or displaying analyses of behavioral patterns. The ultimate goal is to help users better understand themselves and explore the practice of maintaining distance from emotions.

## Current Status

*   The project is in the early ideation and design phase (as of 2025-04-04).
*   **Initial Focus:** Building an MVP centered around **health data** (specifically from sports watches/bands), prioritizing integration with **Garmin**.

## Tech Stack Overview

The project employs a hybrid architecture with the following main technologies:

*   **Core BaaS:** Supabase (providing PostgreSQL DB, Auth, Realtime, Storage, etc.)
*   **Custom Backend:** Python (FastAPI) - for complex logic, third-party integrations, AI analysis.
*   **Frontend:** React / Vue (To be decided)
*   **Task Queue (Optional):** Celery + Redis/RabbitMQ

For detailed technical architecture and design decisions, please refer to `DESIGN.md`.

## Collaboration & Documentation

This project is developed through AI-human collaboration. To maintain clarity and contextual memory over the long term, we maintain the following core documents:

*   `README.md`: This file, providing a project overview.
*   `DESIGN.md`: Records key design decisions, architecture, and functional specifications.
*   `DECISIONS.md`: Logs important project decisions and their rationale.
*   `PRINCIPLES.md`: Outlines the core principles guiding development and collaboration.

Documentation prioritizes AI-friendliness (clarity, structure, precision) while ensuring human readability. We encourage open, constructive communication, viewing the AI as a teammate rather than just an executor.

## Contributing

Please refer to `CONTRIBUTING.md` for guidelines on how to contribute to this project, including commit message conventions and code style (when defined).

## Privacy

Our commitment to your privacy is outlined in the `PRIVACY.md` file.