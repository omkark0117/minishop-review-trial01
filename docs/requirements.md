# MiniShop behavior requirements

- Discounts are percentages: a 10% discount on 200 leaves 180.
- Restocking adds new units to the current inventory count.
- Password verification must require an exact match in this toy example.
- Express shipping should add a surcharge; it must not reduce the standard fee.
- `calculate_tax(amount, rate)` returns the tax amount only, not the total including tax.
- Order transitions must follow the transition table in `src/orders.py`.
