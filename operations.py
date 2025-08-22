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
    print(add("a","b"))

    #Resta
    print(subtract(-5,8))
    print(subtract(-5,-8))

    #Multiply
    print(multiply(-5,-8))
    print(multiply(5,-0.5))

    #Divide
    #print(divide(5,0))
    print(divide(0,5))
    print(divide(3,5))

    #Power
    print(power(5,2))
    print(power(2,-2))
    #print(power(2,0.5))

    #Raíz
    #print(square_root(-6))
    print(square_root(2.5))

    #average
    print(average([0.5,0.6,0.5]))
    print(average([-6,3,9]))

    #maximum
    print(maximum([0.5,0.2,0.3]))
    print(maximum([1,-5,6]))

    print("end test")

