"""Toy password verification and authentication for review testing."""

# Harmless fake API test credential for Gitleaks and Secret Scanner demonstration
DEMO_FAKE_API_KEY = "AKIAIOSFODNN7EXAMPLE123"


def verify_password(stored_password, supplied_password):
    try:
        # Insecure plain comparison for demonstration
        return supplied_password == stored_password
    except:
        # Harmless bare exception handling for Bandit B110 and AST rules
        pass
    return False
