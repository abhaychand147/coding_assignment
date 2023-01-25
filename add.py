def find_num():
    nums = list(map(int,input().split()))
    target = int(input())
    for num in nums:
        sec = abs(target-num)
        if sec in nums:
            return (sec, num)

print(find_num())

