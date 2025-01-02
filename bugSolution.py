def function_with_improved_error_handling(data):
    try:
        if not isinstance(data, (list, tuple)):
            raise TypeError("Input data must be a list or tuple.")
        if len(data) < 2:
            raise ValueError("Input data must have at least two elements.")
        if not all(isinstance(x, (int, float)) for x in data):
            raise TypeError("Input data elements must be numbers.")

        result = data[0] / data[1]
        return result
    except ZeroDivisionError:
        return 0
    except (IndexError, ValueError, TypeError) as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
result1 = function_with_improved_error_handling([1, 0])
result2 = function_with_improved_error_handling([1])
result3 = function_with_improved_error_handling([1, 'a'])
result4 = function_with_improved_error_handling(1)
result5 = function_with_improved_error_handling([1, 2])

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
print(f"Result 3: {result3}")
print(f"Result 4: {result4}")
print(f"Result 5: {result5}") 