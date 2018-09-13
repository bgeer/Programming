def new_password(newpass, oldpass):
    if newpass == oldpass:
        return False
    elif newpass != oldpass and len(newpass) >= 6:
        if hasNumbers(newpass) == True:
            return True
    else:
        return False

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

np = 'test12'
op = 'test1234'


print(new_password(np,op))

