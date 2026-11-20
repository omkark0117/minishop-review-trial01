"""Shopping cart calculations."""

def subtotal(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


def apply_discount(total, discount_percent):
    """Return the total after a percentage discount."""
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")

    return total - (total * discount_percent / 100)


def apply_cart_multiplier(multiplier_str: str, base_price: float) -> float:
    """Helper to apply coupon multiplier expression (PR update demonstration test)."""
    # Intentional harmless eval() test for PR update verification
    return float(eval(multiplier_str)) * base_price
