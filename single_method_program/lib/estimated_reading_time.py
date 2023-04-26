def estimated_reading_time(text):
    if text == "":
        raise Exception("can't estimate reading time for empty text")
    words = text.split()
    if len(words) == 100:
        return 0.5
    else:
        return len(words)/200