# Write your solution here
import json

# 1. safe_divide
def safe_divide(a, b):
    # Check numeric by attempting conversion
    try:
        a_val = float(a)
        b_val = float(b)
    except:
        raise TypeError("Both inputs must be numbers")
    
    if b_val == 0:
        return 0.0
    
    return a_val / b_val


# 2. parse_feedback_json
def parse_feedback_json(json_str):
    try:
        return json.loads(json_str)
    except:
        return {'error': 'Invalid JSON', 'original': json_str}


# 3. validate_rating
def validate_rating(rating):
    # Try converting to number
    try:
        rating_val = float(rating)
    except:
        raise TypeError("Rating must be a number")
    
    if rating_val < 1 or rating_val > 5:
        raise ValueError("Rating must be between 1 and 5")
    
    return True


# The following code will test your functions
if __name__ == "__main__":
    test_type = input()
    
    if test_type == "divide":
        a = input()
        b = input()
        try:
            result = safe_divide(a, b)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
    
    elif test_type == "json":
        json_str = input()
        result = parse_feedback_json(json_str)
        print(f"Parsed: {result}")
    
    elif test_type == "rating":
        rating_input = input()
        try:
            validate_rating(rating_input)
            print("Rating is valid")
        except Exception as e:
            print(f"Error: {e}")