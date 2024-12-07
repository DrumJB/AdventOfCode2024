# AOC day 7

# recursion easyland :-)

with open('input.txt', 'r+') as f:
    data = f.readlines()

# first part
def rec_oper(nums):
    if len(nums) == 1:
        return [nums[0]]
    else:
        results = []
        for n in rec_oper(nums[:-1]):
            results.append(n*nums[-1:][0])
            results.append(n+nums[-1:][0])
    return results


def check_eq(result, numbers):
    total = 0
    results = rec_oper(numbers)
    for r in results:
        if r == result:
            total += 1
    if total > 0:
        return result
    return 0

total_sum = 0
for d in data:
    a = d.split(':')
    res = int(a[0])
    num = [int(b) for b in a[1][1:-1].split(' ')]
    total_sum += check_eq(res, num)
print(total_sum)

# second part
def concat(x, y):
    return int(str(x)+str(y))

def rec_oper2(nums):
    if len(nums) == 1:
        return [nums[0]]
    else:
        results = []
        for n in rec_oper2(nums[:-1]):
            results.append(n*nums[-1:][0])
            results.append(n+nums[-1:][0])
            results.append(concat(n, nums[-1:][0]))
    return results

def check_eq2(result, numbers):
    total = 0
    results = rec_oper2(numbers)
    for r in results:
        if r == result:
            total += 1
    if total > 0:
        return result
    return 0

total_sum = 0
for d in data:
    a = d.split(':')
    res = int(a[0])
    num = [int(b) for b in a[1][1:-1].split(' ')]
    total_sum += check_eq2(res, num)
print(total_sum)