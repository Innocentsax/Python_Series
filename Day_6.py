// HOW TO USE ELIF STATEMENT IN PYTHON

print("==> USER LOGIN <==")

username = input("Please enter you Username: ")
print()
password = input("Please enter you pasword: ")
print()
if username == "Innocent" and password == "Ben":
    print(username, "You are welcome")
elif username == "Udo" and password == "Ufan":
    print("Wow!! You are a great man")
elif username == "Charles" and password == "Result":
    print("Welcome to ALX Africa")
else:
    print("Go away")
