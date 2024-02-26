def to_freud(sentence):
    #your code here
    if not sentence:
        return ""
    else:
        return " ".join(["sex" for _ in sentence.split()])
