import copy

#     0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32
arr=['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
arrViz = []          #массив в виде списка для хранения квадрата Виженера
print('     Квадрат Виженера для русского алфавита')

def switch(n):    #функция для записи в массив arrViz квадрата Виженера и его вывода в консоль
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

m="ЬСА"                    #Message for Decrypt
k="ПИ"                        #Key for crypt and decrypt
k*=len(m)//len(k)+1              #делим сообщение мо модулю на длину ключа 
                                 #и умножаем ключ на это значение чтобы
                                 #поставить ключ многократно в соответствие 
                                 #всей длине шифруемого сообщения
print(m)
print(k)

c=""   #переменная для хранения расшифровываемого сообщения



for i,j in enumerate(m):              #пробегаемся по всем буквам сообщения
        
        index1=arr.index(j)           #определяем индекс для буквы сообщения     
        index1=arr.index(k[i])        #определяем индекс для буквы ключа
        n=0
        while j!=arrViz[index1][n]:
                n=n+1
                
        #print(n)
        index2=n
        print(index2,'index2')
        #print(index1,'index1')   
        c=c+arr[index2]
        
        print(c)
print("Зашифрованное сообщения: "+str(c))


