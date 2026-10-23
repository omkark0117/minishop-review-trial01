"""Tax calculations."""

def calculate_tax(amount, rate):
    if amount < 0:
        raise ValueError("amount cannot be negative")

    if not 0 <= rate <= 1:
        raise ValueError("rate must be between 0 and 1")

    return amount * (1 + rate)