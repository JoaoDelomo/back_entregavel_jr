import hmac
import hashlib
import os

def encode_hmac_hash(data: str) -> str:
    secret_key = os.getenv("HMAC_SECRET_KEY", "default_secret_key").encode()
    return hmac.new(secret_key, data.encode(), hashlib.sha256).hexdigest()
