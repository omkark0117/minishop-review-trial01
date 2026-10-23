"""Shipping fee calculations."""

def shipping_fee(weight_kg, express=False):
    if weight_kg < 0:
        raise ValueError("weight cannot be negative")

    fee = 50 if weight_kg <= 2 else 100

    if express:
        fee += 50

    return fee