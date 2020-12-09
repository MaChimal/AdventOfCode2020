### Day 9: Encoding Error ###

## Part 2

nums = []

for num in open("day9.txt"):
    num = num.strip()
    nums.append(int(num))

def errorNum():

    allData = len(nums)

    for i in range(25, allData):
        sum_ = False

        for x in nums[i-25:i]:
            for y in nums[i-25:i]:
                if x + y == nums[i] and x != y:
                    sum_ = True
                    break
            
            if sum_:
                break
        
        if not sum_:
            return(nums[i])
    
errNum = errorNum()

def weakness():

    for i in range(len(nums)):
        n = 0

        for j in range(i, len(nums)):
            n += nums[j]

            if n > errNum:
                break

            elif n == errNum:
                contiguousSet = nums[i:j+1]
                
                return(min(contiguousSet) + max(contiguousSet))

answer = weakness()

print(answer)
