alphch=['ноль','один','два','три','четыре', 'пять', "шесть", 'семь', "восемь", 'девять','десять',"одиннадцать",'двенадцать','тринадцать'
        ,'четырнадцать','пятнадцать','шестнадцать','семнадцать','восемнадцать','девятнадцать','двадцать','тридцать','сорок'
        ,'пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто']
alphop=["плюс",'минус','умножить']
def w2num(n):
    s=['ноль','один', 'два', 'три', 'четыре', 'пять', 'шесть','семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    s2=['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if ' ' in n:
        n=n.split()
        if n[0] in s2:
            a=s2.index(n[0])+2
            a=str(a)
            a=a+'0'
            if n[1] in s:
                a=int(a)
                a=a+s.index(n[1])
    else:
        if n in s:
            a=s.index(n)
        else:
            a=int(str(s2.index(n)+2)+'0')
    return a
edinici=['ноль','один','два','три','четыре', 'пять', "шесть", 'семь', "восемь", 'девять']
desyatkiunik=['десять',"одиннадцать",'двенадцать','тринадцать'
        ,'четырнадцать','пятнадцать','шестнадцать','семнадцать','восемнадцать','девятнадцать']
desyatki=['двадцать','тридцать','сорок'
        ,'пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто']
sotni=['сто','двести','триста','четыреста','пятьсот',"шестьсот",'семьсот','восемьсот','девятьсот']
kosari=['две','три','четыре']

def calc(a,op,b):
    if op=='плюс':
        j=a+b
    if op=='минус':
        j=a-b
    if op=='умножить':
        j=a*b
    #число в строку
    j=str(j)
    if len(j)==1: #однозначное число
        j=edinici[int(j)]
        return j
    if len(j)==2:#двузначное
        if 10<=int(j[0]+j[1])<=19:
            j=desyatkiunik[int(j[1])]
            return j
        else:
            if j[1]!='0':
                j=desyatki[int(j[0])-2]+' '+edinici[int(j[1])]
                return j
            else:
                j = desyatki[int(j[0])-2]
                return j
    if len(j)==3:#трехзначное
        if j[1]=='0':
            if j[2]=='0':
                j=sotni[int(j[0])-1]
                return j
            else:
                j = sotni[int(j[0]) - 1]+' '+edinici[int(j[2])]
                return j
        else:
            if 10<=int((j[1]+j[2]))<=19:
                j=sotni[int(j[0])-1]+' '+desyatkiunik[int(j[2])]
                return j
            else:
                if j[2]!='0':
                    j=sotni[int(j[0])-1]+' '+desyatki[int(j[1])-2]+' '+edinici[int(j[2])]
                    return j
                else:
                    j = sotni[int(j[0])-1] +' '+ desyatki[int(j[1])-2]
                    return j
    if len(j)==4:#четырехзначное
        if j[0]=='1': #одна тысяча
            if j[1]=='0':#если сотен нет
                if j[2]=='0':
                    if j[3]=='0':
                        j ='тысяча'
                        return j
                    else:
                        j ='тысяча ' + edinici[int(j[3])]
                        return j
                else:
                    if 10 <= int(j[2] + j[3]) <= 19:
                        j = 'тысяча ' + desyatkiunik[int(j[3])]
                        return j
                    else:
                        if j[3] != '0':
                            j ='тысяча ' + desyatki[int(j[2]) - 2] + ' ' + edinici[int(j[3])]
                            return j
                        else:
                            j ='тысяча ' + desyatki[int(j[2]) - 2]
                            return j
            else: #если сотни есть
                if j[2]=='0': #если десятков нет
                    if j[3]=='0': #если единиц нет
                        j ='тысяча '+ sotni[int(j[1]) - 1]
                        return j
                    else:
                        j ='тысяча '+ sotni[int(j[1]) - 1] + ' ' + edinici[int(j[3])]
                        return j
                else:
                    if 10 <= int(j[2] + j[3]) <= 19:
                        j = 'тысяча '+ sotni[int(j[1]) - 1] + ' ' + desyatkiunik[int(j[3])]
                        return j
                    else:
                        if j[3] != '0':
                            j ='тысяча '+ sotni[int(j[1]) - 1] + ' ' + desyatki[int(j[2]) - 2] + ' ' + edinici[int(j[3])]
                            return j
                        else:
                            j ='тысяча '+ sotni[int(j[1]) - 1] + ' ' + desyatki[int(j[2]) - 2]
                            return j
        if 2<=int(j[0])<=4: #от 2 до 4 тысяч
            if j[1]=='0': #если сотен нет
                if j[2]=='0':
                    if j[3]=='0':
                        j =kosari[int(j[0])-2]+' тысячи'
                        return j
                    else:
                        j =kosari[int(j[0])-2]+' тысячи ' + edinici[int(j[3])]
                        return j
                else:
                    if 10 <= int(j[2] + j[3]) <= 19:
                        j = kosari[int(j[0])-2]+' тысячи ' + desyatkiunik[int(j[3])]
                        return j
                    else:
                        if j[3] != '0':
                            j =kosari[int(j[0])-2]+' тысячи ' + desyatki[int(j[2]) - 2] + ' ' + edinici[int(j[3])]
                            return j
                        else:
                            j =kosari[int(j[0])-2]+' тысячи ' + desyatki[int(j[2]) - 2]
                            return j
            else:
                if j[2]=='0':
                    if j[3]=='0':
                        j =kosari[int(j[0])-2]+' тысячи '+ sotni[int(j[1]) - 1]
                        return j
                    else:
                        j =kosari[int(j[0])-2]+' тысячи '+ sotni[int(j[1]) - 1] + ' ' + edinici[int(j[3])]
                        return j
                else:
                    if 10 <= int(j[2] + j[3]) <= 19:
                        j = kosari[int(j[0])-2]+' тысячи '+ sotni[int(j[1]) - 1] + ' ' + desyatkiunik[int(j[3])]
                        return j
                    else:
                        if j[3] != '0':
                            j =kosari[int(j[0])-2]+' тысячи '+ sotni[int(j[1]) - 1] + ' ' + desyatki[int(j[2]) - 2] + ' ' + edinici[int(j[3])]
                            return j
                        else:
                            j =kosari[int(j[0])-2]+' тысячи '+ sotni[int(j[1]) - 1] + ' ' + desyatki[int(j[2]) - 2]
                            return j
        else: #от 5 до 9 тысяч
            if j[1]=='0':#если сотен нет
                if j[2]=='0':
                    if j[3]=='0':
                        j =edinici[int(j[0])]+' тысяч'
                        return j
                    else:
                        j =edinici[int(j[0])]+' тысяч ' + edinici[int(j[3])]
                        return j
                else:
                    if 10 <= int(j[2] + j[3]) <= 19:
                        j = edinici[int(j[0])]+' тысяч ' + desyatkiunik[int(j[3])]
                        return j
                    else:
                        if j[3] != '0':
                            j =edinici[int(j[0])]+' тысяч ' + desyatki[int(j[2]) - 2] + ' ' + edinici[int(j[3])]
                            return j
                        else:
                            j =edinici[int(j[0])]+' тысяч ' + desyatki[int(j[2]) - 2]
                            return j
            else: #если сотни есть
                if j[2]=='0':
                    if j[3]=='0':
                        j =edinici[int(j[0])]+' тысяч '+ sotni[int(j[1]) - 1]
                        return j
                    else:
                        j =edinici[int(j[0])]+' тысяч '+ sotni[int(j[1]) - 1] + ' ' + edinici[int(j[3])]
                        return j
                else:
                    if 10 <= int(j[2] + j[3]) <= 19:
                        j = edinici[int(j[0])]+' тысяч '+ sotni[int(j[1]) - 1] + ' ' + desyatkiunik[int(j[3])]
                        return j
                    else:
                        if j[3] != '0':
                            j =edinici[int(j[0])]+' тысяч '+ sotni[int(j[1]) - 1] + ' ' + desyatki[int(j[2]) - 2] + ' ' + edinici[int(j[3])]
                            return j
                        else:
                            j =edinici[int(j[0])]+' тысяч '+ sotni[int(j[1]) - 1] + ' ' + desyatki[int(j[2]) - 2]
                            return j



while True:
    ch1=input('Введите число 1: ').strip()

    if ' ' in ch1:
        ch1_1=ch1.split()
        if ch1_1[0] in alphch and ch1_1[1] in alphch:
            ch1num=w2num(ch1)
        else:
            print('Введено некорректное число')
            continue
    else:
        if ch1 in alphch:
            ch1num=w2num(ch1)
        else:
            print('Введено некорректное число')
            continue
    operation=input('Введите название операции: ').strip()

    if operation not in alphop:
        print('Введена некорректная операция')
        continue
    ch2=input('Введите число 2: ').strip()

    if ' ' in ch2:
        ch2_1 = ch2.split()
        if ch2_1[0] in alphch and ch2_1[1] in alphch:
            ch2num = w2num(ch2)
        else:
            print('Введено некорректное число')
            continue
    else:
        if ch2 in alphch:
            ch2num = w2num(ch2)
        else:
            print('Введено некорректное число')
            continue
    break

print(calc(ch1num,operation,ch2num))