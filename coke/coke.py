## Question 2

#Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
#In a file called coke.py, implement a program that prompts the user to insert a coin,
#  one at a time, each time informing the user of the amount due. Once the user has inputted
#  at least 50 cents, output how many cents in change the user is owed. Assume that the user
#  will only input integers, and ignore any integer that isn’t an accepted denomination.

# Integers only, no decimals. Value is in Cents, not dollars


def main():
    cost = 50
    money = 0
    while cost > 0:
        print(f"Amount due: {cost}")
        coin = insert_coin()
        money = coin
        cost = cost - money
    else:
        print(f"Change Owed: {abs(cost)}")


def insert_coin():
    while True:
        insert = int(input("Insert coin: "))
        if insert % 5 == 0:
            break
#        elif:
#            print("Incorrect Coin denomination)
    return insert


if __name__ == "__main__":
    main()

