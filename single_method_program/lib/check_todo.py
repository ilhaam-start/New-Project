def check_todo(text):
    if text == "":
        raise Exception("No string to check")
    if "#TODO" in text:
        return True
    else:
        return False