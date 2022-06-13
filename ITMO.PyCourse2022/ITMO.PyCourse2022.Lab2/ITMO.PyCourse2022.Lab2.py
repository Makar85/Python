
print("-----------Работа со строками-------------")

string1 ="This is a string."
string2 = " This is another string."
string3 = string1+string2
print(string3)
print(len(string1)) #len() - определяет длину строки;
print(string1.title()) #title() - преобразует первый символ каждого слова в строке к верхнему регистру;
print(string1.lower()) #lower() - символы строки преобразуются к нижнему регистру;
print(string1.upper()) #upper() - символы строки преобразуются к верхнему регистру;
print(string1.rstrip()) #rstrip() – удаляются пробелы в конце строки;
print(string2.lstrip()) #lstrip() – удаляются пробелы в начале строки;
print(string2.strip()) #strip() - удаляются пробелы с обоих концов;
print(string1.strip('T')) #strip('0') - удаляются с обоих концов указанные символы в параметре функции.


d = "Hello, how are you?"
ch = d[4]
print(ch)
chm = d[1:3]
print(chm)
chm1=d[1:]
chm2=d[:2]
chm3=d[:]
chm4=d[1:5:2]
print(chm4)
d[2] = 'o'

print("-----------Работа с числами-------------")
dig1=15
dig2=64
newdig1=dig2/dig1
newdig2=dig2%dig1
newdig3=dig2**dig1
print(newdig1)
print(newdig2)
print(newdig3)

print("-----------Преобразование данных-------------")
param ="string"+str(15)
print(param)
n1 = input("Введите первое число: ")
n2 = input("Введите второе число: ")
n3 = float(n1)+float(n2)
print(n1+" plus " + n2 + " = ", n3)

print("-----------Форматирование строк-------------")

a=1/3
print("{:7.3f}".format(a))

a=2/3
b=2/9
print("{:7.3f} {:7.3f}".format(a,b))

n1 = float(input("Введите первое число: "))
n2 = float(input("Введите второе число: "))
n3=n1+n2
print('{:7.3f}' " plus " '{:7.3f}' "=" '{:7.3f}'.format(n1,n2,n3))

print("----------Списки--------------")

list1=[82,8,23,97,92,44,17,39,11,12]
print(dir(list1))
print(help(list1))

list1[0] = 33
list1[1] = 54
list1[2] = 81
list1[3] = 12
list1[4] = 34
list1[5] = 94


list1.append(144)
list1.insert(6,350)
list1.pop(8)
list1.pop()
print(list1)

list1.sort(reverse = True)
print(list1)

list2 = [3,5,6,2,33,5,11]
lis = sorted(list2)
print(lis)

print("----------Кортежи--------------")
print(dir(tuple))
help(dir(tuple))

seq = (2,8,23,97,92,44,17,39,11,12)
print(seq)
print(seq.count(8))
print(seq.index(44))
listseq=type(seq)
print(listseq)
listseq.sort()
listseq.append(55)
print(listseq)

print("-----------Словари-------------")
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
print(D['food'])
D['quantity'] +=10
print(D['quantity'])

dp = {}
dp['name'] = input('Введите имя:')
dp['age'] = input('Введите возраст:')
print(dp)

print("-----------Вложенность хранения данных-------------")
rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
'job': ['dev', 'mgr'],'age': 25}

print(rec['name']['firstname'], ' ',rec['name']['lastname'])
print(rec['name']['firstname'])
print(rec['job'])
rec['job'].append('janitor')
print(rec)



