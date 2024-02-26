def best_friend(txt, a, b):
    occurrences_first = [i for i in range(len(txt)) if txt[i] == a]
    
    for index in occurrences_first:
        if index < len(txt) - 1 and txt[index + 1] == b:
            continue
        else:
            return False
    
    return True