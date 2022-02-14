# we require to import a math module to perform the square root
import math
# using an already given formula that if a number squared multiplied by five then the answer 
# either add or subtract should be a perfect square.
#create a function to check whether a perfect square

def isPerfectSquare(num):
    # variable to store the squareroot of the parsed parameter
    checker=int(math.sqrt(num))
    return checker *checker==num
# a function to check whether its a fibonacci
def isFib(value):
    #the formula to work with
    if isPerfectSquare((5*value*value)+4) or isPerfectSquare((5*value*value)-4):
        return "is a fibonacci "
    else:
        return "Not a fibonacci"
print(isFib(4))# call the function  