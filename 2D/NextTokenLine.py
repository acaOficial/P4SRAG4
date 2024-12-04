def next_token_line(file_pointer, token):
    """
    Look for the next line containing the specified token in a file.

    Args:
        file_pointer: An open file object for reading.
        token (str): The keyword to search for in the lines.

    Returns:
        tuple:
            next_line (str): The next line containing the token, or None if not found.
            pos (int): The position of the token in the line, or None if not found.
    """
    pos = None
    next_line = None

    for line in file_pointer:
        pos = line.find(token)
        if pos != -1:  # Token found in the line
            next_line = line.strip()  # Remove trailing newline and spaces
            return next_line, pos

    # End of file reached without finding the token
    return None, None
