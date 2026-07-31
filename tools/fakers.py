import time
from typing import AnyStr


def get_random_email() -> AnyStr:
    return f"test.{time.time()}@example.com"