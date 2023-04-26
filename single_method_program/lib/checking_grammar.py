def checking_grammar(text):
    if text == "":
        raise Exception("No text to check.")
    if text[0].isupper() and text[-1] in ".!?":
        return True
    else:
        return False