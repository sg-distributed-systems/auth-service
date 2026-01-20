"""
Service entrypoint with lifecycle management.

Initializes configuration, correlation ID, and signal handlers before running
the main service logic. Provides structured error handling for all exceptions.
"""
from core_logger import get_logger

from auth_service.config import load_config
from auth_service.errors import AppError
from auth_service.lifecycle import install_signal_handlers
from auth_service.observability import init_correlation_id

logger = get_logger("auth-service")


def authenticate_user(user_id: str) -> bool:
    logger.info("auth_success", user_id=user_id)
    return True


def fail_authentication(user_id: str) -> None:
    logger.warning("auth_failure", user_id=user_id, reason="invalid_credentials")


def run() -> None:
    cfg = load_config("auth-service")
    cid = init_correlation_id()
    install_signal_handlers("auth-service")

    logger.info("service_starting", env=cfg.env, correlation_id=cid)

    try:
        authenticate_user("user-456")
        fail_authentication("user-789")
        logger.info("service_completed")
    except AppError as e:
        logger.warning("app_error", **e.to_log_fields())
        raise
    except Exception as e:
        logger.exception("unhandled_exception", exc=e)
        raise


def main() -> None:
    run()


if __name__ == "__main__":
    main()
