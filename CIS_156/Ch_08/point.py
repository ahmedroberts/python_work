nums = [10, 20, 30, 40, 50]

for pos in range(len(nums)):
  print(nums[pos])
  tmp = nums[pos] / 2
  if (tmp % 2) == 0:
      nums[pos] = tmp