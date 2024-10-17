print("")
print("Welcome to the Virtual Fortune Teller!!")
print(" ")
print("This program works very similarly to a magic 8ball, and will answer best if you ask similar questions!")
print(" ")
question=input("Ask a yes or no question:")
print(" ")
num=int(input("Pick a number from 1-4:"))
print(" ")
if num == 1:
    print("One.")
elif num == 2:
    print("One, two.")
elif num == 3:
    print("One, two, three.")
else:
    num == 4
    print("One, two, three, four.")
print(" ")
print("Your color options are:")
print(" ")
if num == 1 or num == 3:
    print("Red, Blue, Pink, or Yellow")
elif num == 2 or num == 4:
    print("Brown, Green, Purple, or Orange")
print(" ")
color=str(input("Pick a color from the above colors:"))
print(" ")
print("Your question was:",question)
print(" ")
print("Our answer is:")
if color == "Red" or color == "red":
    print("It is your destiny!")
elif color == "Blue" or color == "blue":
    print("You wish!")
elif color == "Pink" or color == "pink":
    print("Yes!")
elif color == "Yellow" or color == "yellow":
    print("No. Just no.")
elif color == "Brown" or color == "brown":
    print("NEVER!!!")
elif color == "Green" or color == "green":
    print("Don't count on it.")
elif color == "Purple" or color == "purple":
    print("Who knows?")
elif color == "Orange" or color == "orange":
    print("Absolutely!")
print(" ")