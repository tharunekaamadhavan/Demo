num=int(input("Enter numerator: "))
den=int(input("Enter deno: "))
try:
    quo=num/den
    print("quotient: ",quo)
except ZeroDivisionError:
    print("Deno can't be 0")
