start=input("Welcome!!\nleft or right --- > ")
if(start.lower() == "left"):
    sw=input("swim/wait")
    if(sw.lower()=="swim"):
        print("over")
    else :
        door=input("Which door ? red/blue/yellow ")
        if(door.lower()=="blue"):
            print("Over")
        elif(door.lower()=="red"):
            print("Over")
        else:
            print("You win")
else:
    print("over")

# Learnings:-
# 1. variable_name.lower() is used to convert to lowercase
# 2. variable_name.count("e") counts the number of e in the word , 
#   so we can add t= variable_name.count("t") , r= variable_name.count("r") , like ( t+r )
#   and it will give total number of t and r together