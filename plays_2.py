maps=list(range(1,10)) #обозначаем кол-во ячейек для крестиков ноликов
victory=[[0,1,2], #выигрышные комбинации
         [3,4,5],
         [6,7,8],
         [0,3,6],
         [1,4,7],
         [2,5,8],
         [0,4,8],
         [2,4,6]]
def print_maps(): #функция для печати таблицы
    for i in range (3): #поочередно выводим строки таблицы
        print(maps[i*3+0],maps[i*3+1],maps[i*3+2])
def input_maps(): #функция для ввода значений
    if igrok==False: #проверка какой игрок ходит
        igroks='X'
    else:
        igroks='O'
    hod=input('Ваш ход игрок '+ igroks + ' ')
    while (hod not in '123456789') or (int(hod) not in maps) : #пороверка на корректность ввода
        hod=input('Введено неверное значение. Еще раз ваш ход '+ igroks + ' ')
    maps[int(hod)-1]=igroks #замена цифры в таблице крестиком или ноликом
        
def proverka_win(): #проверка на победу
    win='никто'
    for i in victory: #проходимся по списку выигрышных комбинаций
        for i in victory:
            if (maps[i[0]]==maps[i[1]]==maps[i[2]]):
                if igrok==False:
                    win='X'
                else:
                    win='O'
                    break
    return win     
count=9
igrok=False
win='никто' 
while win =='никто' and count!=0:
    print_maps()
    input_maps()
    win = proverka_win()
    igrok=not igrok
    count-=1
print('Выиграл игрок '+ win)
