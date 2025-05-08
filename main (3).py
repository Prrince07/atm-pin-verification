pin = 1234
for i in range(3):
    p = int(input("Enter your pin: "))
    if p == pin:
        print("Correct pin")
        break
    else:
        print("Incorrect pin")
else:
    print("Block the card")
