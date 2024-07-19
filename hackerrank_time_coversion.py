def timeConversion():
    s = input()
    #s = "09:05:45PM"
    new_time = ""
    if s[-2:] == "AM" and s[:2] == "12":
        new_time = "00" + s[2:-2]
    elif s[-2:] == "AM":
        new_time = s[:-2]
    elif s[-2:] == "PM" and s[:2] == "12":
        new_time = s[:-2]
    else:
        ans = int(s[:2]) + 12
        new_time = str(str(ans) + s[2:8])
    print(new_time)

timeConversion()
