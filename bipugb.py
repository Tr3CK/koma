a = 'products.txt'
b = 'extracted_lines.txt'
c = 3
with open(a, 'r') as f:
    lines = f.readlines()
d = lines[:c]
with open(b, 'w') as new_f:
  new_f.writelines(d)
f = open(b, 'r')
print(f.read())
f.close()
print("Извлечено {} строк из файла '{}' и записано в файл '{}'.".format(c, a, b))



