#1.
def max_num(num1, num2, num3):
  return max(num1, num2, num3)
result = max_num(10, 5, 20)
print("Maximum number:", result)

#2.
#iterative approach 
'''
def mult_list(list):
  result = 1
  for num in list:
    result *= num
  return result
'''
#recursive
def mult_list(list):
  if len(list) == 0:
    return 1
  else:
    return list[0] * mult_list(list[1:])

numbers = [2, 2, 2, 3]
result = mult_list(numbers)
print(result)

#3.
def rev_string(string):
  return string[::-1]
#[start:stop:step] notation 

#4.
def num_within(number, start, end):
  return start <= number <= end

result = num_within(5, 1, 10)
print(result)