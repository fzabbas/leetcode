# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSumNoGood(nums, target):
  for num in nums:
    if target-num in nums[:nums.index(num)]:
      return nums.index(num), nums[:nums.index(num)].index(target-num)
    if target-num in nums[nums.index(num)+1:]:
      return nums.index(num), (nums[:nums.index(num)]+nums[nums.index(num)+1:]).index(target-num)+1

def twoSum(nums, target):
  hashmap = {}
  for i, num in enumerate(nums):
    if target-num in hashmap:
      return i, hashmap[target-num]
    else:
      hashmap[num] = i

def isPalindromeNum(num):
  if num < 0:
    return False

  list = []
  while num!= 0:
    list.append(num%10)
    num = num//10
  # while num != 0:
  #   list.append(num%10)
  #   print(list)

  # list = [int(x) for x in str(num)]
  return (list == list[::-1])
