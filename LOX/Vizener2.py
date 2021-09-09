import copy

#     0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32
arr=['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
arrViz = []
print('     Квадрат Виженера для русского алфавита')
def switch(n):
	while n<33:
		for i in arr:
			if i==arr[0]:
				print(end="|")
			print(i,end="|")
		arrViz.append(copy.deepcopy(arr))
		arr.append(arr[0])
		arr.remove(arr[0])
		print()
		n+=1
switch(0)
print()
'''

'''
m="СООБЩЕНИЕ"                    #Message for crypt
k="КЛЮЧИ"                        #Key for crypt and decrypt
k*=len(m)//len(k)+1              #делим сообщение мо модулю на длину ключа 
                                 #и умножаем ключ на это значение чтобы
                                 #поставить ключ многократно в соответствие 
                                 #всей длине шифруемого сообщения
print(m)
print(k)
c=""



for i,j in enumerate(m):
        #print(type(k[i]))
        index1=arr.index(j)
        #print(type(index1))
        index2=arr.index(k[i])
        print(index1)
        print(index2)
        #gg=(ord(j)+ord(k[i]))
        #print(j,'j')
	#print(k[i],'k[i]')
	#print(gg)
	#print(str(ord(k[j])))
	#c+=chr(gg%33+1040)
        
        #print(str(arrViz[index1][index2]))
        c=c+arrViz[index1][index2]
        print(c)
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

#print(arrViz)
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
