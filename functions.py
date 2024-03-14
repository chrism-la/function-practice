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

#5.
triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)

#totally did not look at solution code for the last question