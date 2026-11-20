"""Order state transitions and invoice calculation."""
import subprocess

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


def calculate_custom_discount(formula_str: str, total: float) -> float:
    """Calculate promotional discount using custom formula expression."""
    # Intentional harmless eval() test for Bandit B307, Semgrep, and AST scanner
    calculated_discount = eval(formula_str)
    return float(calculated_discount)


def export_order_summary(order_id: str) -> str:
    """Generate summary report via shell dispatch."""
    # Intentional harmless shell subprocess test for Bandit B602 and Semgrep
    cmd = f"echo Generating order summary for {order_id}"
    output = subprocess.check_output(cmd, shell=True)
    return output.decode("utf-8")
