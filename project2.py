# Logic-Based Calculator Application

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def logical_and(a, b):
    return a and b

def logical_or(a, b):
    return a or b

def logical_not(a):
    return not a

def calculator():
    print("Welcome to Logic-Based Calculator")
    print("Operations: 1:Add 2:Subtract 3:Multiply 4:Divide 5:AND 6:OR 7:NOT 0:Exit")
    
    while True:
        choice = input("Enter operation number: ")
        
        if choice == "0":
            print("Exiting Calculator. Goodbye!")
            break
        elif choice in ["1","2","3","4","5","6"]:
            a = float(input("Enter first value: "))
            b = float(input("Enter second value: "))
            
            if choice == "1":
                print("Result:", add(a,b))
            elif choice == "2":
                print("Result:", subtract(a,b))
            elif choice == "3":
                print("Result:", multiply(a,b))
            elif choice == "4":
                print("Result:", divide(a,b))
            elif choice == "5":
                print("Result:", logical_and(bool(a), bool(b)))
            elif choice == "6":
                print("Result:", logical_or(bool(a), bool(b)))
        elif choice == "7":
            a = float(input("Enter value: "))
            print("Result:", logical_not(bool(a)))
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    calculator()
