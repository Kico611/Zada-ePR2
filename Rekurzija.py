def reverse(text):
    if text == "":
        return text
    else:
        return text[-1] + reverse(text[:-1])

    
