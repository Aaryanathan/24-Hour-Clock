time = input("Enter Time: ")

def convert(time):
    if time[-2:] == "AM" and time[:2] == "12":
        print("00" + time[2:-2])
    elif time[-2:] == "PM" and time[:2] == "12":
        print(time[0:-2])
    elif time[-2:] == "AM":
        print(time[0:-2])
    elif time[-2:] == "PM":
        a = int(time[:2]) + 12
        print(str(a) + time[2:8])
    else:
        print("SOmething went wrong")

convert(time)