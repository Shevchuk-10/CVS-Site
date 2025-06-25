from __future__ import annotations

from itsdangerous import URLSafeSerializer

SECRET_KEY = "supersecretkey"
serializer = URLSafeSerializer(SECRET_KEY, salt="auth")


def create_token(username: str) -> str:
    return serializer.dumps({"username": username})


def verify_token(token: str) -> str | None:
    try:
        data = serializer.loads(token)
        return data["username"]
    except Exception:
        return None
