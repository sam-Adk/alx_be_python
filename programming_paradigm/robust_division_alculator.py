def safe_divide(numerator, denominator):
    """
    Safely performs division between two values.
    Handles non-numeric input and division by zero.
    """
    try:
        # Convert both inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        # Perform the division
        result = num / den
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
