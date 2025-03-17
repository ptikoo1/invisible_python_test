import re

def is_valid_string(input_string):
    """
    Checks if a string is valid according to the specified criteria.

    Args:
        input_string: The string to validate.

    Returns:
        True if the string is valid, False otherwise.
    """

    # 1. Check minimum length
    if len(input_string) < 6:
        return False

    # 2. Count numbers
    number_count = len(re.findall(r'\d', input_string))
    if not 2 <= number_count <= 3:
        return False

    # 3. Check for non-numerical characters between numbers
    number_positions = [m.start() for m in re.finditer(r'\d', input_string)]
    for i in range(len(number_positions) - 1):
        if number_positions[i+1] - number_positions[i] <= 1:
            return False
        if re.search(r'[^0-9]', input_string[number_positions[i]+1:number_positions[i+1]]) is None:
            return False

    return True
