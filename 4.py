maps='123456789111213141516171819'
variants=[]
    
def print_maps():
    print('abcdefghi')
    for i in range ((len(maps)-1)//9+1):
        if len(maps[i*9:i*9+9])<9:
            print(maps[i*9:i*9+9]+' '*(9-len(maps[i*9:i*9+9])),'|'+str(i))
        else:
            print(maps[i*9:i*9+9],'|'+str(i))

def input_hod():
    error =True
    while error:
        a1=input("Введите координаты первого числа (столбец и строку) ")
        error=False
        if len(a1)<2:
            error =True
        elif a1[0] not in 'abcdefghi':
            error =True
        elif a1[1:].isdigit()==False or ((len(maps)-1)//9+1)<=int(a1[1:]):
            error =True
        elif not proverka_hoda1(a1):
            error =True
    error =True
    while error:
        a2=input("Введите координаты второго числа (столбец и строку) ")
        error=False
        if len(a2)<2:
            error =True
        elif a2[0] not in 'abcdefghi':
            error =True
        elif a2[1:].isdigit()==False or ((len(maps)-1)//9+1)<=int(a2[1:]):
            error =True
        elif not proverka_hoda12(a1,a2):
            error =True
    i1=adr_el_maps(a1)
    i2=adr_el_maps(a2)
    maps1=maps[:i1]+"-"+maps[i1+1:]
    maps1=maps1[:i2]+"-"+maps1[i2+1:]
    return maps1

# Проверка на правильность первого хода
def proverka_hoda1(xy):
    resultat=False
    axy=adr_el_maps(xy)
    for i in variants:
        if i[0]==axy or i[1]==axy:
            resultat=True
            break   
    return resultat

# Проверка на правильность первого и второго хода
def proverka_hoda12(xy1,xy2):
    resultat=False
    axy1=adr_el_maps(xy1)
    axy2=adr_el_maps(xy2)
    for i in variants:
        if (i[0]==axy1 and i[1]==axy2) or (i[0]==axy2 and i[1]==axy1):
            resultat=True
            break   
    return resultat

# Пересборка вариантов хода
def creat_variants():
    variants.clear()
    for i in range(len(maps)):
        var=proverka_variant(i)
        if var[1]<var[0]:
            variants.append([i,var[1]])
        if var[2]<var[0]:
            variants.append([i,var[2]])

# Возвращает массив, где первый элемент кол-во эл-в массива maps, второй и третий возможные варианты хода вправо и вниз соответственно
# Причем, если 2 или 3 элементы массива равны первому (те вне массива maps), то элемент не прошел проверку (вариант не найден)
# Условие проверки это равенство суммы элементов maps[adr] и найденно элемента по условию. Условие это пустые значения между элементами.
def proverka_variant(adr):
    var=[len(maps),len(maps),len(maps)]
    if maps[adr]!="-":
        i_count=len(maps)
        i=adr+1
        while i<i_count and maps[i]=="-" :
            i+=1
        if i<i_count and (maps[adr]==maps[i] or (int(maps[adr])+int(maps[i]))==10) and (i//9)==(adr//9):  
            var[1]=i
        i=adr+9
        while i<i_count and maps[i]=="-":
            i+=9
        if i<i_count and (maps[adr]==maps[i] or (int(maps[adr])+int(maps[i]))==10):  
            var[2]=i
    return var

#Позиция элемента в массиве maps в соответствии с координатами
def adr_el_maps(xy):
    x= 'abcdefghi'.index(xy[0])
    y=int(xy[1:])
    return y*9+x

def read_el_maps(xy):
    x= 'abcdefghi'.index(xy[0])
    y=int(xy[1:])
    return maps[y*9+x]

def del_space():
    maps1=maps
    for i in range (len(maps)//9):
        if maps[i*9:i*9+9]=='---------':
            maps1=maps[:i*9]+maps[i*9+9:]
    return maps1

def add_string():
    maps1=maps
    for i in maps:
        if i!='-':
            maps1+=i
    return maps1
            

win=False
while not win:
    print_maps()
    creat_variants()
    if len(variants)>0:
        print('Кол-во возможных вариантов хода ',len(variants))
        maps=input_hod()
        maps=del_space()
    elif maps.replace('-','').isdigit()==True:
        maps=add_string()
    else:
        print('Игра окончена!')
        win=True
