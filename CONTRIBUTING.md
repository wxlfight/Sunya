# Contributing to Sunya

Thank you for your interest in contributing to the Sunya project! We aim to maintain a high standard of quality and consistency. Please adhere to the following guidelines.

## Security: Avoiding Sensitive Information

**Under no circumstances should any sensitive information be committed to the repository.** This includes, but is not limited to:

*   API keys, secrets, or authentication tokens
*   Passwords or private keys
*   Personal Identifiable Information (PII)
*   Proprietary configuration details

If the application requires such information (e.g., API keys for external services), use standard secure practices like environment variables, configuration file templates (`.example` files), or dedicated secrets management. Provide clear instructions in the documentation (`README.md` or specific setup guides) on how users should configure these securely in their local environment.

## Git Commit Guidelines

We follow specific rules for Git commit messages to ensure clarity, consistency, and enable potential automation (e.g., generating changelogs).

### Atomic Commits

*   Each commit should represent a single, complete, and logical unit of change.
*   Avoid mixing unrelated changes in one commit.
*   Keep commits reasonably small to facilitate code review and history tracking.

### Commit Message Format

*   **All commit messages must be written in English.**
*   We adhere to the **Conventional Commits** specification (v1.0.0).
*   The basic format is:

    ```
    <type>[optional scope]: <description>

    [optional body]

    [optional footer]
    ```

*   **`<type>`:** Describes the kind of change:
    *   `feat`: A new feature
    *   `fix`: A bug fix
    *   `docs`: Documentation only changes
    *   `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
    *   `refactor`: A code change that neither fixes a bug nor adds a feature
    *   `perf`: A code change that improves performance
    *   `test`: Adding missing tests or correcting existing tests
    *   `build`: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
    *   `ci`: Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
    *   `chore`: Other changes that don't modify `src` or `test` files (e.g., updating dependencies)
*   **`<scope>` (Optional):** A noun specifying the place of the commit change (e.g., `auth`, `parser`, `ui`).
*   **`<description>`:** A short, imperative mood description of the change (e.g., `add login page`, `fix user validation`). Use lowercase.
*   **`<body>` (Optional):** A longer description providing context, motivation, and details of the change.
*   **`<footer>` (Optional):** Contains information about Breaking Changes or references to issues that this commit closes (e.g., `BREAKING CHANGE: ...`, `Closes #123`).

*   **Example:**

    ```
    feat(api): implement user profile endpoint

    Adds a new GET endpoint `/api/users/me` to retrieve the authenticated user's profile information.

    Closes #55
    ```

## Code Style (To Be Determined)

We will establish and enforce a consistent code style using linters and formatters appropriate for the chosen programming languages. Details will be added here once decided.

## Branching Strategy (To Be Determined)

We will likely adopt a simple branching model like GitHub Flow (`main` is deployable, work happens in feature branches, merged via Pull Requests). Details will be finalized and added here. 