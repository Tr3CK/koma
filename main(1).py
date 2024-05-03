def find_median(num1, num2, num3):
  min_num = min(num1, num2, num3)
  max_num = max(num1, num2, num3)
  median = num1 + num2 + num3 - min_num - max_num
  return median

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

result = find_median(num1, num2, num3)
print("Медиана введенных чисел равна:", result)