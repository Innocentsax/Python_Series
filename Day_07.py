// USING NESTED IF IN PYTHON

print("==> ALX", "\033[31m", "USER LOGIN","\033[0m","<==")
print()
username = input("kindly enter your username: ")
password = input("kindly enter you password: ")

if username == "Innocent" and password == "Charles":
    print("WOW!!..",username,"You are in cohort 11")
        if username == "Charles" and password == "Udo":
            print("I think you should be in cohort 10")
                    if username == "Ayuba" and password == "Omena":
                        print("Sure!! you are in Bwave group")
                    else:
                        print("You are in ALX programmer group")
        else:
            print("Enjoy you cohort 11.")
else:
    print("Invalid information")
