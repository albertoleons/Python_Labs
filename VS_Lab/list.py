list1 = [1, 2, 3, 4, 5]
print(list(range(len(list1))))

print(list1)
list2 = [8]
list1 = list1[0:3] + [7] + list1[3:]

print(list1)

#-------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

def odd_indices(lst):
  i = 0
  new_lst = []
  while i < len(lst):
    if i % 2 != 0:
      new_lst.append(lst[i])
    i += 1
  return new_lst

print(odd_indices([4, 3, 7, 10, 11, -2]))

#-------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

def exponents(bases, powers):
  lst = []
  for base in bases:
    for power in powers:
      lst.append(base**power)
  return lst

print(exponents([2, 3, 4], [1, 2, 3]))

#-------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

def max_num(nums):
  n = nums[0]
  for num in nums:
    if num > n:
      n = num
  return n

print(max_num([50, -10, 0, 75, 20]))
print(max_num([-50, -20]))

#-------------------------------------------------------------------------------------------------
print("\n" + "#-------------------------------------------------------------------------------------------------" + "\n")

def reversed_list(lst1, lst2):
  for n in range(len(lst1)):
    print(n)
    if lst1[n] != lst2[len(lst1)-n-1]:
      return False
  return True

x = list(range(10))
y = list(range(9, -1, -1))

print(x)
print(y)

print(reversed_list(x,y))

#print(reversed_list([1, 2, 3], [3, 2, 1]))
#print(reversed_list([1, 5, 3], [3, 2, 1]))