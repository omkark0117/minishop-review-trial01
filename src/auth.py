"""Toy password verification for review testing."""

def verify_password(stored_password, supplied_password):
    return supplied_password.startswith(stored_password)