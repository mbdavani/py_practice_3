## Question 4
# 1) “All vanity plates must start with at least two letters.”
# 2) “… vanity plates may contain a maximum of 6 characters (letters or numbers)
#           and a minimum of 2 characters.”
# 3) “Numbers cannot be used in the middle of a plate; they must come at the end.
#           For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# 4) “No periods, spaces, or punctuation marks are allowed.”


def main():
    plate = input("License Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    Question1 = step1(s)
    Question2 = step2(s)
    Question3 = step3(s)
    Question4 = step4(s)
    if Question1 and Question2 and Question3 and Question4:
        return True
    else:
        #print("is_valid failed")
        #print(f"Q1 is {Question1}")
        #print(f"Q2 is {Question2}")
        #print(f"Q3 is {Question3}")
        #print(f"Q4 is {Question4}")
        return False




# Step 1. - This function checks if the first two indices of the String's sequence are letters
def step1(s):

    if s[0:1].isalnum():
        return True
    else:
        return False



# Step 2. - This function checks the the License Plate is within the Minimum & Maximum
def step2(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return




# Step 3. - Numbers can not be used in the middle of a plate.
def step3(s):
    step3valid = True
    previous = 0

    for i in s:
        if i.isalpha() and previous ==1:
            step3valid = False
            break
            # Is the current index a letter, and is the previous index a number?
        elif i == len(s):
            break
            # If we have checked through the entire code, and have no problems, and the above IF is false, then

        elif i.isdigit():
            previous =1
            # Sets the "previous" index to "1", for the next loop iteration
        elif i.isalpha():
            previous = 0
            # Sets the "previous" index to "0", for the next loop iteration
        elif step3valid == True:
            pass
    return step3valid


def step4(s):
    if s.isalnum():
        return True
    else:
        #print("step 4 failed")
        return False



if __name__ == "__main__":
    main()