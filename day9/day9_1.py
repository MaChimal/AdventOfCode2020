### Day 9: Encoding Error ###

## Part 1

nums = []

for num in open("day9.txt"):
    num = num.strip()
    nums.append(int(num))

def errorNum():

    allData = len(nums)

    for i in range(25, allData):
        sum = False

        for x in nums[i-25:i]:
            for y in nums[i-25:i]:
                if x + y == nums[i] and x != y:
                    sum = True
                    break
            
            if sum:
                break
        
        if not sum:
            return(nums[i])
    
answer = errorNum()

print(answer)

