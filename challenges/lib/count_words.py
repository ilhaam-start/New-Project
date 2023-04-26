def count_words(sentence):
    if sentence != str:
        return sentence
    elif sentence != "":
        sentences = sentence.split()
        return len(sentences)
    else:
        return sentence