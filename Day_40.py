"""🌟Contact Card🌟"""

name = input("input your name > ").strip() 
number = input("input your telephone number > ").strip()
mail = input("Input your email > ").strip()
address = input("Input your address >").strip()
dob =  input("Enter you date of birth > ")

dict = {"name": name, "number": number, "mail": mail, "address": address, "dob": dob}

print(f"""Name:{dict["name"]}""")
print(f"""number:{dict["number"]}""")
print(f"""mail:{dict["mail"]}""")
print(f"""address:{dict["address"]}""")
print(f"""dob:{dict["dob"]}""")
