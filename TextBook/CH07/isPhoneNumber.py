def is_post_code(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
        if text[7] != '-':
            return False
        for i in range(8, 12):
            if not text[i].isdecimal():
                return False
    return True


print('415-555-4242 は郵便番号:')
print(is_post_code('415-55-4242')) 
print('Moshi moshi は郵便番号:')
print(is_post_code('Moshi moshi'))  
