#.lowwer() funqcia yvela asos gadaaqcevs patara asod >upper() funqcia gadaaqces yvela asos did asod .capitalize() winadadebis pirvel asos gadaaqcevs pirvel asos da .find() funqcia gviwers meramdenezea konkretuli aso

second_name=input("Please enter youre second name")
if second_name[0]==second_name[0].upper():
    print("hello")
else:
    print("bye")


name=input("Please enter youre name:")
if name.find("a")==-1:
    print("Cant find character")



surname=input("Enter youre surname:")
change=input("How would you like to change:")

if change=="upper":
    print(surname.upper())
elif change=="lower":
    print(surname.lower())
else:
    print("invaild input")