# Giraffe Language
# vowels -> g
# _______________
#
# dog => dgg
# cat => cgt


def translate(phrase):
    translation = ""
    vowels = "aeiou"
    for letter in phrase:
        if letter.lower() in vowels:
            if letter.isupper():
                translation += "G"
            else:
                translation += "g"
        else:
            translation += letter
    return translation


print(translate(input("Enter a phrase: ")))