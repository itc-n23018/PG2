import re


def custom_strip(text, chars=None):
    
    if chars is None:
        pattern = r'^\s+|\s+$'
    else:
        pattern = f'^[{re.escape(chars)}]+|[{re.escape(chars)}]+$'

    return re.sub(pattern, '', text)


text = "  Hello, World!  "
chars_to_remove = " !"
print(custom_strip(text))  
print(custom_strip(text, chars_to_remove))  
