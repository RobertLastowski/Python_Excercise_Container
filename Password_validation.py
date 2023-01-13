'''
STRING VALIDATOR E.G. FOR PASSWORD VALIDATION
'''

def validator(my_string):
    check = 0
    numbers = 0
    upper = 0
    lower = 0
    for litera in my_string:
        if litera.isdigit() == True:
            numbers += 1
        elif litera.isupper() == True:
            upper += 1
        elif litera.islower() == True:
            lower += 1
        elif litera.isalnum() == False:
            check += 1
            
    if check < 1:
        print("Special characters are missing")
    elif numbers < 1:
        print("No digits")
    elif len(my_string) < 6:
        print( "Text shorter than 6 characters!")
    elif len(my_string) > 12:
        print( "Text longer than 12 characters!")
    elif upper < 1:
        print("Capital letters are missing")
    elif lower < 1:
        print("Lowercase letters are missing")
    else:
        print("The text meets the requirements :)")


validator("kie12!łbaSa")