def fanyi():
    Flag = False
    dict1 = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
        "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30,
        "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
        "hundred": 100, "thousand": 1000, "million": 1000000
    }
    s = input().split()
    if s[0] == "negative":
        Flag = True
        s.pop(0)
    result = 0
    count = 0
    for i in s:
        print(i)
        if dict1[i] == 100:
            count *= 100
        elif dict1[i] == 1000 or dict1[i] == 1000000:
            result += count * dict1[i]
            count = 0
        else:
            count += dict1[i]
    result += count
    if Flag:
        print(-result)
    else:
        print(result)
fanyi()