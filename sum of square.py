# This program finds the sum of squares of first n postive integers,
# where n is inputed by the user. n>1 and is integer


def main():
    print("This program finds the sum of squares of first n postive integers.")

    tries = 0
    success=False
    
    while tries < 3 and not success:
        try:
            number=eval(input("Please input any positive integer and press Enter:"))
            success = True
        except NameError: # if a letter or string was typed, or a negative number
            print("This is a string/letter or a negative number.")
            print("You should input a postive integer.")
            tries += 1
        
    if tries == 3:
        print("You\'ve exceeded the maximum number of attempts to enter a correct number.")
    else:        
        answer=sumOfSquares(number)
        if answer != -1:
            print("The sum of squares of first",number,"positive integers is",answer,".")
        else:
            print("Incorrect input.\n")

    print("Have a good day!")


def sumOfSquares(n):
    ''' Finds the sum of squares of first n postive integers,

    method returns -1 if the argument is not integer or not positive'''
                  
    if type(n) == int and n > 1:
        sq = 0 # sum of squares
        for k in range(n+1):
            sq += k**2
    else:
        print("\n sumOfSquares Error: the argument should be positive integer.\n")
        sq = -1
    return sq

main()    
