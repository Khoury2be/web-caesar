def encrypt(text, rot):
    new_text= ""
    for letter in text:
        new_letter = rotate_character(letter, rot)
        new_text = new_text + new_letter
    return new_text

def alphabet_position(letter):
    letter = letter.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    return alpha.index(letter)

def rotate_character(char, rot):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alphaCaps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if char in alphaCaps:
        num = alphabet_position(char)
        num = (num + rot) % 26
        num = alphaCaps[num]
        return num
    elif char in alpha:
        num = alphabet_position(char)
        num = (num + rot) % 26
        num = alpha[num]
        return num
    else:
        return char
