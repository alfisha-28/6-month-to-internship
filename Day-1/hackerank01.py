#Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird
n = int(input("Enter number n(1,100):"))

if n % 2 == 0:
    if n>=2 and n<=5:
        print("Not Weird") 
    if n>=6 and n<=20:
        print("Weird") 
    if n>20:
        print("Not Weird")    
else:
    print("Weird") 
    
