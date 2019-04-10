n=input()
try:
    if float(n):
        print("yes")
except ValueError:
    print("no")
