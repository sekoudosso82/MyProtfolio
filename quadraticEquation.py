from math import sqrt

def quadraticEquation(a,b,c):
    ''' find solution of a quadratic equation ax*x+bx+c=0
    returns False if no real-number solution exists
    returns one solution, if there is only one solution, and
    returns a list with two elements - if there are two solutions'''
    
    try:
        D = sqrt(b*b-4*a*c)
    except ValueError:
        return False

    if D == 0:
        return -b/float(2*a)
    else:
        return [(-b+D)/float(2*a),(-b-D)/float(2*a)]

def getInput():

    ''' method for taking input from user : expecting three numbers,
        separated by commas '''

    while True:
        try:
            a,b,c = eval(input("Please,input coefficients a, b, and c of quadratic equation ax*x+bx+c=0, separated by commas:"))
            return a,b,c
        except NameError:
            print("You should provide three numbers, separated by comma.")
            print("Please, try again.")

def main():
    print("This programs finds solution(s) of a quadratic equation, if they exist,")
    print("otherwise, states that there are no solutions.\n")

    a,b,c = getInput()

    
    print("The equation to solve: "+ str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0")

    solution = quadraticEquation(a,b,c)

    if solution == False:
        print("The given equation has no real number solutions.")
    else:
        print("The given equation has solution(s): x=",solution)

main()

    

