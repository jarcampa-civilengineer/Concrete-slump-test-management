# Reusable validation helpers for future GUI or web versions.
def is_valid_slump(value):
    try:
        return float(value) >= 0
    except (TypeError, ValueError):
        return False
