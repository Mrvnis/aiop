"""
A simple hello world script for testing.
"""

def greet(name="World"):
    """Print a greeting message."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
    print(greet("Test User"))
