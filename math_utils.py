def find_max_number(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  if num2 > num1 and num2 > num3:
    return num2
  return num3

def find_max_number(num1, num2, num3):
  if num1 > num2 and num1 > num3:
      print("the max number is:", num1)
  elif num2 > num1 and num2 > num3:
      print("the max number is:", num2)
  else:
      print("the max number is:", num3)

find_max_number(1,3,-1)

def find_mean(num1, num2, num3):
    sum = num1 + num2 + num3
    mean = sum / 3
    print("the mean is:", mean)

find_mean(1,3,2)

def find_mean(num1, num2, num3):
    mean = (num1 + num2 + num3) / 3
    return mean

def find_mean_std(num1, num2, num3):
    mean = find_mind(num1, num2, num3)
    var = ((num1 - mean)**2 + (num2 - mean)**2 + (num3 - mean)**2) /3
    std = var ** 0.5
    return mean, std

num1 = 1
num2 = 3
num3 = 2

mean_value = find_mean(num1, num2, num3)
print("the mean is:", mean_value)

mean, std = find_mean_std(num1, num2, num3)
print ("the mean is:", mean)
print("the standard deviation is:", std)

    

