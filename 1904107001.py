#https://github.com/omerhubx/untitled.git

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

o= {1 : "a" , 2 : "b" , 3  :  "c", 4 : "d" , 5 : "e" , 6 : "f" , 7 : "g" , 8 : "h" , 9 : "i" , 10 : "j" , 11 : "k" , 12 : "l",
    13 :"m" , 14 : "n" , 15 :  "o" , 16 : "p" , 17 : "q" ,18 : "r" , 19 : "s" , 20 : "t" , 21 : "u" , 22 : "v" , 23 :"w",
    24 : "x" , 25 : "y" , 26 : "z"}


m = [[15,13,5]]
m2 = [[18,8,1]]
m3 = [[14,15,7]]
m4 = [[12,21,1]]


e = [[0,0,0]]
e2 = [[0,0,0]]
e3 = [[0,0,0]]
e4 = [[0,0,0]]


Sifre=[[1,2,-1],[2,5,2],[-1,-2,2]]

for r in range(len(m)):
     for h in range(len(Sifre[0])):

         for a in range(len(Sifre)):
             e[r][h] += m[r][a] * Sifre[a][h]

for g in e:
    print(g)


for r in range(len(m2)):
     for h in range(len(Sifre[0])):

         for a in range(len(Sifre)):
             e2[r][h] += m2[r][a] * Sifre[a][h]

for g in e2:
    print(g)


for r in range(len(m3)):
     for h in range(len(Sifre[0])):

         for a in range(len(Sifre)):
             e3[r][h] += m3[r][a] * Sifre[a][h]

for g in e3:
    print(g)

for r in range(len(m4)):
     for h in range(len(Sifre[0])):

         for a in range(len(Sifre)):
             e4[r][h] += m4[r][a] * Sifre[a][h]

for g in e4:
    print(g)

#4.Soru


print( 0, "ile", 10, "arasındaki asal sayılar:")
e=[]
for o in range(0, 10 + 1):
    if o > 1:
        for m in range(2, o):
            if (o % m) == 0:
                break

        else:

            e.append(o)
            print(e)


