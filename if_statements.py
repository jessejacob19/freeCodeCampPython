is_male = True
is_tail = False

if is_male and is_tail:
    print("you are a tall male")
elif is_male and not(is_tail):
    print("you are a short male")
elif not(is_male) and is_tail:
    print("you are not a male but are tall")
else:
    print("you are neither")