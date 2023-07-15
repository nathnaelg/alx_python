def validate_password(password):
    password = str(password)
    if len(str(password)) < 8:
        return False
    for i in range(len(password)):
        if password[i] == password[i].upper() and password[i] != password[i].lower():
            break
        if password[i] == password[len(password)-1]:
            return False
    for i in range(len(password)):
        if password[i] == password[i].lower() and password[i] != password[i].upper():
            break
        if str(i) == password[len(password)-1]:
            return False
    for i in range(len(password)):
        if password[i].isspace():
            return False
    return True