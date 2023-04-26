def make_snippet(sentence):
    sentence_split = sentence.split()
    if len(sentence_split) >= 5:
        sentence_count = sentence_split[:5]
        return " ".join(sentence_count) + "..."
    else:
        return sentence

    
    
    
