"""Inventory management."""

def restock(stock, sku, quantity):
    if quantity < 0:
        raise ValueError("quantity cannot be negative")

    stock[sku] = stock.get(sku, 0) + quantity