print ('Hello, World!')
name = "Lisa"
print(name)
if 3 > 2:
    print("It works!")
if 5 > 2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')
name = "Lisa"
if name == "Lisa":
    print("Hey, Lisa!")
elif name == "Rory":
    print("Hey, Rory!")
else:
    print("Hey, who the heck are you?")
volume = 57
if volume < 20:
    print("it's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music.")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details.")
elif 60 <= volume < 80:
    print("Nice for parties.")
elif 80 <= volume < 100:
    print ("A bit loud!")
else:
    print("My ears are hurting! :(")
def hi(name):
    print("Hi " + name + "!")
hi(name)
def hi(name):
    print("Hi " + name + '!')

girls = ["Rachel", "Monica", "Phoebe", "Ola", "You"]
for name in girls:
    hi(name)
    print("Next girl")
    for i in range(1, 6):
        print(i)
        
