X=int(input())
while X!=1:
    if X%2!=0:
        print(f'{X}*3+1={X*3+1}')
        X=X*3+1
    else:
        print(f'{X}/2={X//2}')
        X=X//2

        from itertools import count


        def A():
            n = input()
            special = {"CM": 900, "XC": 90, "IX": 9, "IV": 4}
            result = 0
            for i in special.keys():
                if i in n:
                    result += special[i]
                    n.replace(i, "")
            result += n.count("I")
            result += n.count("V") * 5
            result += n.count("X") * 10
            result += n.count("L") * 50
            result += n.count("C") * 100
            result += n.count("D") * 500
            result += n.count("M") * 1000
            print(result)


        def a(n):
            result = ""
            if n == 9:
                result = result + "IX" + "V"
            elif n == 8:
                result = result + "IVIV"
            else:
                result = result + "V"
                result = result + (n - 5) * "I"

            return result


        def b(n):
            result = ""
            if n > 90:
                result = result + "XC"
                res = a()
                result = result + res
                return result
            elif n > 50:
                result = result + "L"
                result = result + ((n - 50) % 10) * "X"
            else:
                result = result + (n // 10) * "X"
                a(n % 10)
