# Demonstrates logical operators and compound conditions
print("\tExclusive Computer Network")
print("\t\tMembers only!\n")

username = ""
while not username:
 username = input("Username: ")
password = ""
while not password:
 password = input("Password: ")
if username == "M.Dawson" and password == "secret":
 print("Hi,", username)

elif username == "S.Meier" and password == "civilization":
 print("Hey, Sid.")

elif username == "S.Miyamoto" and password == "mariobros":
 print("What's up, Shigeru?")
 
elif username == "W.Wright" and password == "thesims":
 print("How goes it, Will?")

elif username == "guest" or password == "guest":
 print("Welcome, guest.")

else:
 print("Login failed. You're not so exclusive.\n")
input("\n\nPress the enter key to exit")
