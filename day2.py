amount=float(input("Welcome to the tip calculator.\nWhat was the total bill ? "))
n=int(input("How many people to split the bill ?"))
tip=int(input("Tip % ? 10 , 12 or 15 ? "))
print("Each person should pay "+f"{round((amount*((100+tip)/100))/n,2)}")

# Learnings
# 1. int() is used to convert to integer, float() for deciaml values
# 2. round(100.0000,2) will print to 2 decimal places
# 3. f strings are used like f"{}" to print variables value