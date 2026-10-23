"""Inventory management."""

def restock(stock, sku, quantity):
    if quantity < 0:
        raise ValueError("quantity cannot be negative")

    stock[sku] = quantity