password = input("Please enter your password: ")


if  len(password) < 8:
    print(f"Your password must contain at least 8 characters, and a mix of letters and numbers")
else:
    letter = False
    number = False
  

    for check in password:
        if check.isalpha():
          letter = True
        elif check.isdigit():
         number = True

    if letter and number:
         print(f"Your password is valid")
    else:
         print(f"Your password must contain at least 8 characters, and a mix of letters and numbers")