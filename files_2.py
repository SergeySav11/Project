with open('text.txt',encoding= 'utf-8') as infile:
    text = infile.readlines()
print(text)
z = 0
for i in range(len(text)):
    if text[i - z] == 'Новая строка\n':
        text.remove('Новая строка\n')
        z += 1

print(text)
