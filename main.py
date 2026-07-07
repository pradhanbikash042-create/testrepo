from calculator import add, subtract, multiply, divide


def greet(name="world"):
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("GitHub Copilot"))
    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))
    print("Multiplication:", multiply(10, 5))
    print("Division:", divide(10, 5))
