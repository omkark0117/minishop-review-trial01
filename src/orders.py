"""Order state transitions."""
ALLOWED_TRANSITIONS = {
    "new": {"paid", "cancelled"},
    "paid": {"shipped", "cancelled"},
    "shipped": {"delivered"},
    "delivered": set(),
    "cancelled": set(),
}
def transition_order(order, new_status):
    current = order["status"]
    if new_status not in ALLOWED_TRANSITIONS.get(current, set()):
        raise ValueError(f"Invalid transition: {current} -> {new_status}")
    order["status"] = new_status
    return order
