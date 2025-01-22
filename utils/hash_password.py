import hashlib

def hash_password(password: str) -> str:
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_hash: str, input_password: str) -> bool:
    """Verify if the input password matches the stored hashed password."""
    return stored_hash == hash_password(input_password)
