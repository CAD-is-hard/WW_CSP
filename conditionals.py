# WW, Conditionals

military_time = int(input("What time is it in military time: "))

if military_time <= 600:
    print("It's too early, why are you awake!!!!")
elif military_time > 600 and military_time <= 900:
    print("Good Morning!")
elif military_time > 900 and military_time <= 1200:
    print("Good Morning! You should be at school!")
elif military_time <= 1700 and military_time >1200:
    print("Good Afternoon")
else:
    print("Good Evening!")


# nesting conditionals
day = input("What day is it: ")
time = int(input("What time is it(in military time): "))

if time > 900 and time < 1553:
    if day !="Saturday" or day != "Sunday":
        print("You should be at school!")
    else:
        if time > 1200:
            print("Good Afternoon!")
        else:
            print("Good Morning!")
else:
    print("You are not required to be at school")