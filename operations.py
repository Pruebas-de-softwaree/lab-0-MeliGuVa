def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    
    return a / b  

def power(a, b):
    return a ^ b  

def square_root(x):
    import math
    return math.sqrt(x)

def average(list):
    return sum(list) / len(list)

def maximum(list):
    return min(list) 


if __name__ == "__main__":

    print("start test")

    print("Holi")

    #Suma
    print(add(5,8))
    print(add(-5,8))

    #Resta
    print(subtract(-5,8))
    print(subtract(-5,-8))

    #Multiply
    print(multiply(-5,-8))
    print(multiply(5,-0.5))

    #Divide
    #print(divide(5,0))
    print(divide(0,5))

    #Power
    print(power(5,2))

    print("end test")

