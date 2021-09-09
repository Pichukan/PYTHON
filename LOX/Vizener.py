
#     0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32
arr=['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
print('     Квадрат Виженера для русского алфавита')
def switch(n):
	while n<33:
		for i in arr:
			if i==arr[0]:
				print(end="|")
			print(i,end="|")
		arr.append(arr[0])
		arr.remove(arr[0])
		print()
		n+=1
switch(0)
print()
'''

'''
m="СООБЩЕНИЕ"
k="КЛЮЧ"
k*=len(m)//len(k)+1 
c=""



for i,j in enumerate(m): 
	gg=(ord(j)+ord(k[i]))
	print(ord(j))
	print(gg)
	#print(str(ord(k[j])))
	c+=chr(gg%33+1040) 
	print(c,'Raund')
print("Encrypted message: "+str(c))


a=ord('А')          #1040  в кодировке ASCII 'А' русское
print(str(a))

b=ord('Б')          #1041  в кодировке ASCII 'Б' русское
print(str(b))       

с=ord('Е')          #1045  в кодировке ASCII 'Е' русское
print(str(с))

с=ord('Ё')          #1025  в кодировке ASCII 'Ё' русское
print(str(с))

h=ord('Я')          #1071  в кодировке ASCII 'Я' русское
print(str(h))


'''
s=0
while s<33:
    print(chr(1040+s))
    s=s+1
'''


'''
c="DSCWR"
k="WORLD"
d="" 
for i,j in enumerate(c): 
	gg=(ord(j)-ord(k[i])) 
	print(chr(gg%26+65))
	d+=chr(gg%26+65) 
print("Decrypted message: "+str(d))
'''
