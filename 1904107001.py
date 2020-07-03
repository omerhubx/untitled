#1.Soru

o= { 1 : "Ocak", 2 : "Şubat" , 3 : "Mart", 4 : "Nisan" , 5 : "Mayıs" , 6: "Haziran" ,
         7 : "Temmuz" , 8 :"Ağustos" , 9 : "Eylül" , 10 :"Ekim" , 11 : "Kasım" , 12 : "Aralık"  }
while True:
    try:
        m=int(input("Gün :"))
        e=int(input("Ay :"))
        r=int(input("Yıl :"))
        if m <32 and m >0:
            print("{}-{}-{}".format(m, o[e], r))
            break
        else:
            print("Lütfen 'Gün' aralığını düzgün giriniz !!! ")
            continue
    except (KeyError):
        print("Lütfen 'Ay'  Aralığını Düzgün Giriniz !!!")
        continue

    except ValueError:
        print("Lütfen geçerli değer girniz !!!")



#2.Soru

def o(m):
    if 9> e >=0:

        if m == 1:
            return m
        else:

            return m*o(m-1)


    elif 9 <= e < 16:
        if  m <0:
            return 0
        else:

            return m + o(m-2)


    else:
        print("Lütfen Geçerli Aralıkta Bir Sayı Griniz !!!!")


e=int(input("Sayi :"))
if 9 > e >= 0:
    print(o(e * 3))
elif  9 <= e < 16:
    print(o(e * 2))
else:
    print("Lütfen Geçerli Aralıkta Bir Sayı Giriniz !!!!\n")







#3.Soru










#4.Soru


print(0, "ile", 10, "arasındaki asal sayılar:")
e=[]
for o in range(0, 10 + 1):
    if o > 1:
        for m in range(2, o):
            if (o % m) == 0:
                break

        else:

            e.append(o)
            print(e)


