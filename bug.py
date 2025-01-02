def function_with_uncommon_error(data):
    try:
        # Assuming 'data' is a list or tuple
        result = data[0] / data[1]
        return result
    except ZeroDivisionError:
        return 0
    except IndexError:
        return None
    except TypeError:
        return "Invalid data type"

# Example of uncommon error (TypeError):
result1 = function_with_uncommon_error([1, 0])  # ZeroDivisionError (common)
result2 = function_with_uncommon_error([1])    # IndexError (common)
result3 = function_with_uncommon_error([1, 'a']) # TypeError (uncommon if not anticipated)
result4 = function_with_uncommon_error(1)      # TypeError (uncommon)

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
print(f"Result 3: {result3}")
print(f"Result 4: {result4}")