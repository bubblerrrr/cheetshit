m = int(input())
n = int(input())
nums =input().split()

from functools import cmp_to_key

def cmp(a,b):
	# a and b are **string**
	# 遵循cmp函数的写法
	if a+b > b+a:
		return -1#表示a在b前面
	if a+b < b+a:
		return 1#表示a在b后面
	return 0
nums.sort(key=cmp_to_key(cmp))

memory = [['']*220 for _ in range(1020)]

_int = lambda x:int(x) if x != "" else 0

def dp(index,available_digit):

	if memory[index][available_digit] != '':
		return memory[index][available_digit]

	if available_digit <= 0:
		return '';
	if index >= n:
		return '';

	# attempt1: dont pick
	attempt1 = dp( index + 1, available_digit )

	# attempt2: pick
	current_num = nums[index]
	if len(current_num) <= available_digit:
		attempt2 = current_num + dp( index + 1, available_digit - len(current_num))
	else:
		attempt2 = ""

	# save the max one
	if _int(attempt1) >= _int(attempt2):
		memory[index][available_digit] = attempt1
	else:
		memory[index][available_digit] = attempt2
	return memory[index][available_digit]

print(dp(0,m))