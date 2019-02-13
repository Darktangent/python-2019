def divison(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return ("Divison by zero is not allowed")

print(divison(1,0))
print("End of program")
