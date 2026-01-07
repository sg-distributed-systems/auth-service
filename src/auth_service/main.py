from core_logger import get_logger

logger = get_logger("auth-service")


def authenticate_user(user_id: str) -> bool:
    logger.info("auth_success", user_id=user_id)
    return True


def fail_authentication(user_id: str) -> None:
    logger.warning("auth_failure", user_id=user_id, reason="invalid_credentials")


if __name__ == "__main__":
    authenticate_user("user-456")
    fail_authentication("user-789")
