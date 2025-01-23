def match(test, dict1):
    left = test[0]
    right = test[1]
    comparison = test[2]
    correct_answer = sum([dict1[i] for i in left]) - sum([dict1[i] for i in right])
    dict_answer = {"up": 1, "down": -1, "even": 0}
    return correct_answer == dict_answer[comparison]


def find_false_coin(test1, test2, test3):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
    dict1 = {m: 0 for m in letters}
    for coin in letters:
        dict1[coin] = -1
        if match(test1, dict1) and match(test2, dict1) and match(test3, dict1):
            print(f'{coin} is the counterfeit coin and it is light.')
            break
        dict1[coin] = 1
        if match(test1, dict1) and match(test2, dict1) and match(test3, dict1):
            print(f'{coin} is the counterfeit coin and it is heavy.')
            break
        dict1[coin] = 0


n = int(input())
for _ in range(n):
    test1 = input().split()
    test2 = input().split()
    test3 = input().split()
    find_false_coin(test1, test2, test3)

