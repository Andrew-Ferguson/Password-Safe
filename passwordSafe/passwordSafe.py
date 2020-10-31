#author: Andrew Ferguson, 15
#start date: 10/14/2020
#file name: passwordSafe
#function of program: keep your passwords safe and use it so you can remember them too. It allows the user to create 
#new login info to store, access all there logins that they have stored, and access some info about there login data.
#current version: 1.0.0

def main():
    decide = str(input("\nNew password or Access password or info - n/a/i: "))
    
    if decide == "n":
        username = str(input("Enter the username that is used: "))
        password = str(input("Enter a password: "))
        website = str(input("Enter the website that the password is used for: "))
        newPassword(username, password, website)
    elif decide == "a":
        accessPasswords()
    elif decide == "i":
        safeInfo()
    else:
        print("**invalid**\n")

def safeInfo():
    totalLines = 0
    convertToList = []
    f = open("safe.txt", "r")
    for line in f:
        totalLines += 1
        convertToList.append(line)
    convertToString = ''.join(convertToList)
    print("\n info about your login data ")
    print("----------------------------")
    print("the total amount of lines in the safe is", totalLines, "\n")

    while True:
        restart = str(input("Whould you like to do more or exit - m/e: "))
        if restart == "m":
            main()
        elif restart == "e":
            exit()
        else:
            print("**invalid try again**\n")

    

def newPassword(username, password, website):
    f = open("safe.txt", "a")
    f.write(username + " / " + password + " / " + website)
    f.write("\n")
    f.close()
    
    while True:
        restart = str(input("\nWhould you like to do more or exit - m/e: \n"))
        if restart == "m":
            main()
        elif restart == "e":
            exit()
        else:
            print("**invalid try again**\n")


def accessPasswords():
    count = 0
    lines = []
    f = open("safe.txt", "r")
    print("\n All your info ")
    print("---------------")
    for line in f: 
        count += 1
        print("{} | username/Password/website -- {}".format(count, line.strip()))
    f.close()
    print("")

    while True:
        restart = str(input("Whould you like to do more or exit - m/e: "))
        if restart == "m":
            main()
        elif restart == "e":
            exit()
        else:
            print("**invalid try again**\n")

main()
