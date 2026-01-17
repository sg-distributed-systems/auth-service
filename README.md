# auth-service

Handles authentication and authorization logic for users.

## Why this repo exists

Centralizing authentication logic in a dedicated service ensures consistent security policies and simplifies credential management across the platform.

## Core Components

### `authenticate_user(user_id: str) -> bool`
Validates user credentials and returns whether authentication succeeded.

**Logs:**
- `auth_success` — Logged when a user successfully authenticates

### `fail_authentication(user_id: str)`
Records a failed authentication attempt.

**Logs:**
- `auth_failure` — Logged when authentication fails, includes the failure reason

## HTTP Interface

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/healthz` | GET | Liveness probe |
| `/readyz` | GET | Readiness probe |
| `/auth/authenticate` | POST | Authenticates a user |

### Running the service

```bash
uvicorn src.auth_service.app:app --host 0.0.0.0 --port 8001
```
