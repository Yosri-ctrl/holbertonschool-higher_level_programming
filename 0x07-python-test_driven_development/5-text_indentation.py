#!@/usr/bin/python3
def text_indentation(text):
    if text is None or type(text) != str or len(text) < 0:
        raise TypeError("text must be a string")
    for i in text:
        if i in [".", "?", ":"]:
            print(i, "\n")        
        else:
            print(i, end="")    
