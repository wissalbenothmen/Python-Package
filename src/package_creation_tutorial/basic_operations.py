def add(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Sum of the two numbers
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Subtract second number from first number.
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Difference between the two numbers
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers together.
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Product of the two numbers
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Divide first number by second number.
    
    Args:
        a (float): Numerator
        b (float): Denominator
        
    Returns:
        float: Result of division
        
    Raises:
        ZeroDivisionError: If the denominator is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
