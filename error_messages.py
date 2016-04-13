def return_error_message(self, index):
    error_messages = {
        0: "ERROR: Invalid expression!",
        1: "ERROR: Not a number!",
        2: "ERROR: Cannot divide by 0!",
        3: "ERROR: Already cleared!"
    }
    return error_messages.get(index)