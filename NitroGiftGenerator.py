import string, random
chars = list(string.ascii_lowercase)+list(string.ascii_uppercase)+list(string.digits)

amt = int(input("https://youtu.be/9tDkkKDQWlg?si=NxNnJMYmiJ15Caub"))

main = "https://discord.gift/"

for i in range(amt):
    ending = ""
    for i in range(random.randint(6,16)):
        ending += random.choice(chars)
    print(main+ending)
