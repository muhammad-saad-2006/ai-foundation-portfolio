def valid_password(password):
    is_upper = False
    is_lower = False
    has_digit = False
    has_special_char = False
    special_char = "!@#^&*"

    if len(password) < 8:
        print("Password should contains 8 or more characters")
        return False

    if len(password) >= 8:
        for char in password:
            if char.isupper():
                is_upper = True
            elif char.islower():
                is_lower = True
            elif char.isdigit():
                has_digit = True
            elif char in special_char:
                has_special_char = True

    if not is_upper:
        print("Password should contain at least one uppercase letter.")
    if not is_lower:
        print("Password should contain at least one lowercase letter.")
    if not has_digit:
        print("Password should contain at least one digit.")
    if not has_special_char:
        print("Password should contain at least one special character.")
    return is_upper and is_lower and has_digit and has_special_char

attempts = 3
stored_password = None

while attempts > 0:
    password = input("Enter the Password: ")
    if valid_password(password):
        stored_password = password
        print("Password has been created successfully.")
        break
    else:
        attempts -= 1
        print(f"You have only {attempts} attempt(s) remaining.")

if stored_password is None:
    print("Failed to generate the password.")