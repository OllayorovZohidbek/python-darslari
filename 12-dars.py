# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 11:36:19 2025

@author: ASB
"""
# 03 - dars

# Amaliyot
# print("\"Nexia\", \"Tico\", 'Damas' ko'rganlar qilar havas")
# 1 - misol
#print("5 ning 4 darajasi", 5**4, "ga teng")
# 2 - misol
#print("22 ni 4 ga bo'lgandagi qoldiq", 22%4,"ga teng")
# 3 - misol
#print("Tomonlari 125 ga teng kvadratning yuzi", 125**2, "," , "perimetri", 125*4,"ga teng")                    
# 4 - misol
#print("Diametri 12 ga teng bo'lgan doiraning yuzi",6**2*3.14,"ga teng!")
# 5 - misol
#print("Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasi",(6**2+7**2)**0.5,"ga teng")

# 04 - dars

# 1-misol
#hello_world = "Hello World!"
#print(hello_world)
# 2-misol
#xabar = "Seshanba"
#print(xabar)
#xabar = "Chorshanba"
#print(xabar)
# 3-misol
#class = "Xatolik beradi"
#radius = 5
#pi = 3.14159
#aylana_yuzi = pi * radius**2
#print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)

# 05-dars

# f-string
#ism = "Zohid"
#familiya = "Ollayorov"
#print(f"Mening ismim {ism}, familyam  {familiya}")

# Maxsus belgilar
#print("Hello World!")
#print("Hello \tWorld!") # \t -- boshliq qoldiradi
#print("Hello \nWorld!") # \n -- pastgi qatorga tushiradi

# String metodlar
#ism = "Zohid"
#familya = "Ollayorov"
#ism_sharif = f"{ism} {familya}"
#print(ism_sharif.upper())
#print(ism_sharif.lower())
#print(ism_sharif.title())
#print(ism_sharif.capitalize())

#meva = "    olma    "
#print("Men " + meva.lstrip() + " yaxshi ko'raman")
#print("Men " + meva.rstrip() + " yaxshi ko'raman")
#print("Men " + meva.strip() + " yaxshi ko'raman")

#ism = input("Ismingiz nima?\n>>>")
#print("Assalomu aleykum, " + ism.title())

# 06 - dars
#print("Iltimos quyidagi ma'lumotlarni kiriting?")
#kocha = input("Ko'changiz?\n>>>").title()
#mahalla = input("Mahallangiz?\n>>>").title()
#tuman = input("Tumaningiz?\n>>>").title()
#viloyat = input("Viloyatingiz?\n>>>").title()

#kocha = "Bog'bon"
#mahalla = "Sog'bon"
#tuman = "Bodomzor"
#viloyat = "Samarqand"
#print(f"{kocha} ko'chasi,{mahalla} mahallasi,{tuman} tumani,{viloyat} viloyati")

# 06-dars

#a = 20
#b = 5.5
#print(type(a))
#print(type(b))
#print(type(type))
#aholi_soni = 7_594_345_987
#print(aholi_soni)
#x,y,z = 3,4,5
#print(x,y,z)
#radius = 20
#PI = 3.14159    
#diametr = 2*radius
#print("Aylana uzunligi=",PI*diametr)

# Amaliyot
# 1-misol
#son = int(input("Istalgan son kiriting?\n>>>"))
#print(str(son) + " ning kvadrati",son**2,"ga teng")
#print(str(son) + " ning kubi",son**3,"ga teng")
# 2- misol
#yosh = int(input("Yoshingiz nechada?\n>>>"))
#t_yil = 2025-yosh
#print("Siz" , t_yil ,"-yilda tugilgansiz")
# 3 - misol
#birinchi_son =int(input("Birinchi sonni kiriting?\n>>>"))
#ikkinchi_son =int(input("Ikkinchi sonni kiriting?\n>>>"))
#print(birinchi_son,"+",ikkinchi_son,"=",birinchi_son+ikkinchi_son)
#print(birinchi_son,"-",ikkinchi_son,"=",birinchi_son-ikkinchi_son)
#print(birinchi_son,"*",ikkinchi_son,"=",birinchi_son*ikkinchi_son)
#print(birinchi_son,"/",ikkinchi_son,"=",birinchi_son/ikkinchi_son)

# 07-dars
#mevalar = ['olma','anjir','shaftoli',"o'rik"]
#narhlar = [12000,18000,10900,22000]
#sonlar = ['bir','ikki',3,4.5]
#ismlar = []
#mevalar[0] = 'banan'
#mevalar.append('olma')
#mevalar.insert(0,"tarvuz")
#print(mevalar)
# .append() --> ro'yxatni oxiriga element qo'shadi
# .insert() --> index,object , berilgan indexsga malumot qoshadi.

#cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
#del cars[0] # royxatdagi birincgi elementni o'chiradi
#cars.insert(0,"Nexia 3")
#cars.remove("volvo") # royxatdan volvo ni ochiradi. agar bir nechta bolsa birinchisini ochiradi remove funksiyasi
#print(cars)
#bozorlik = ['yog','piyoz','un','gosht']
#mahsulot = bozorlik.pop(3) # pop --> berilgan indexsdagi elemenetni sugurib oladi. Agar indexs berilmasa oxirgi elementni sugurib oladi
#print(mahsulot)
#print(bozorlik)
#print("Men " + mahsulot +" sotib oldim")
#print("Olinmagan mahsulotlar" , bozorlik)

# 1-misol
#ismlar = ["Shaxzod","Bobur","Asad"]
#print("Salom",ismlar[0],'qachon kelasan Xorazmga?')
#print("Salom",ismlar[1],'ishlar yaxshimi?')
#print("Salom",ismlar[2],"qalaysan?")
#2-misol
#sonlar = [5,-8,2.3,3,2]
#print(sonlar)
#del sonlar[2]
#sonlar[0] = sonlar[0]+sonlar[-1]
#print(sonlar)
#print(sonlar[0])
# 3 - misol
#t_shaxslar = ["Amir Temur","Alisher Navoiy"]
#z_shaxslar = ["Islom Karimov","Shayx Muhammad Yusuf Muhammad Sodiq"]
#print("Men tarixiy shaxslardan",t_shaxslar[1]," bilan,\n","zamonaviy shaxslrdan esa",z_shaxslar[1],"bilan korishishni xoxlardim")
# 4 - misol
#friends = []
#friends.append("Shaxzod")
#friends.append("Bobur")
#friends.append("Asad")
#print(friends)
#friends.remove("Bobur")
#friends.append("Umid")
#friends.insert(0, "Dilshod")
#print(friends)
#mehmonlar = []
#mehmonlar.append(friends.pop(0))
#mehmonlar.append(friends.pop(0))
#mehmonlar.append(friends.pop(0))
#print(mehmonlar)

# 08-dars . Lists
# 09-dars . Ro'yxatlar bilam ishlash

#cars = ['BMW','Tesla',"Audi","Toyota",'KI',"General Motors"]
#cars.sort(reverse=True) # .sort(reverse=True) --> royxatni teskari tartibda saralaydi
#print(cars)
#print(sorted(cars)) # Asl royxatga tegmagan holda saralaydi
#print(cars)
#cars.reverse() # royxatni teskarisaga aylantiradi
#print(cars)
#print(len(cars)) # Ro'yxatni uzunligini qaytaradi
#sonlar = list(range(10))
#print(sonlar)
#print(cars[0:3])
#my_cars = cars[:] # Royxatdan nusxa olish
#print(cars)
#print(my_cars)
#my_cars.remove("Toyota")
#my_cars.append("Gentra")
#print(my_cars)
#print(cars)

# Tuples
#toys = ('bus','car','bear','dino','snake')
#print(toys[2:])
#toys = list(toys)
#print(type(toys))
#toys.append("teddy")
#print(toys)
# Amaliyot
#davlatlar = ["Uzbekistan","Rossiya","Aqsh","Germaniya","Fransiya","Turkiya","Eron"]
#print(len(davlatlar))
#print(sorted(davlatlar))
#print(sorted(davlatlar,reverse=True))
#print(davlatlar)
#davlatlar.reverse()
#print(davlatlar)
#davlatlar.sort()
#print(davlatlar)
#davlatlar.sort(reverse=True)
#print(davlatlar)
#sonlar = list(range(120,1201,2))
#print(sonlar)
#print(sum(sonlar))
#print(max(sonlar)-min(sonlar))
#print(len(sonlar))
#print(sonlar[:20])
#print(sonlar[-20:])
#print(sonlar[210:230])
#taomlar = ['osh','manti','shashlik','somsa','norin','qazonkabob']
#nonushta = taomlar[:]
#nonushta.remove("osh")
#nonushta.remove("shashlik")
#nonushta.remove("qazonkabob")
#nonushta.append("mastava")
#nonushta.append("shorva")
#print(nonushta)
#print(taomlar)
#nonushta =tuple(nonushta)
#nonushta[0] = 'qaymoq va non'
#print(nonushta)

# For takrorlash operatori
#mehmonlar = ["Ali","Vali","Xasan","Anvar"]
#for mehmon in mehmonlar:
#    print(f"Hurmatli {mehmon}, sizni 20 dekabr kuni nahorga oshga taklif qilamiz!")
#    print("Hurmat bilan Ollayorovlar oilasi")

#sonlar = list(range(1,11))
#for son in sonlar:
#    print(f"{son} ning kvadrati {son**2} ga teng")
#sonlar = list(range(11))
#sonlar_kvadrati = []
#for son in sonlar:
#    sonlar_kvadrati.append(son**2)
#print(sonlar)
#print(sonlar_kvadrati)

#dostlar = []
#print("5 ta eng yaqin dostingiz kim?")
#for i in range(5):
#    dostlar.append(input(f"{i+1} - dostingizni ismini kiriting:/n>>>"))
#print(dostlar)


# Amaliyot
#mehmonlar = ["Ali","Vali","Xasan","Anvar"]
#for mehmon in mehmonlar:
#    print(f"Hurmatli {mehmon}, sizni 20 dekabr kuni nahorga oshga taklif qilamiz!")
#    print("Hurmat bilan Ollayorovlar oilasi")
#print(f"Kod {len(mehmonlar)} marta takrorlandi")
#kinolar = []
#print("5 ta sevimli kinongizni kiriting:")
#for i in range(5):
#    kinolar.append(input(f"{i+1} - kinongizni kiriting:/n>>>>"))
#print(kinolar)
#n = int(input("Bugun nechta odam bilan suhbatlashdingiz?/n>>>"))
#odamlar = []
#for i in range(n):
#    odamlar.append(input(f'{i+1} - suhbatlashgan odamni ismini kiriting: /n>>>'))
#print(odamlar)


# 10-dars. Tarmoqlanish
#avtolar = ['audi','bmw','volvo','kia','toyota']
#for avto in avtolar:
#    if avto == 'bmw':
#        print(avto.upper())
#    else:
#        print(avto.title())
        
#ism = input("Ismingiz nima?\n>>>")
#if ism.lower() != 'ali':
#   print(f"Uzr, {ism.title()} biz Alini kutyapmiz!")
#else:
#    print("Salom , Ali")

#javob = float(input("12x6 nechiga teng?\n>>>"))
#if javob!=72:
#    print("Javob xato!")

#yosh = int(input("Yoshingizni kiriting?\n>>>>"))
#if yosh>=18:
#    print("Xush kelibsiz!")
#else:
#    print("KIrish mumkin emas!")

#login = input("Yangi login tanlang:\n>>>")
#if len(login)<=5:
#    print("Login 5 harfdan ko'p bo'lishi shart!")

#yil = int(input("Tugulgan kuningizni kiriting?\n>>>"))
#if 2025-yil<18:
#    print(f"Sizning yoshingiz {2025-yil} da ekan")
#    print("Sizga kirish mumkin emas!")
#else:
#    print("Xush kelibsiz!")
    
    
#yosh = int(input("Yoshingiz nechida?\n>>>"))
#if yosh>65:print("SIz covid 19 risk guruhida ekansiz")    
    
#x,y = 25,50
#rint("x>y")if x>y else print("x<y")

# Amaliyot 

#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#    if car.lower() != "gm":
#        print(car.title())
#    else:
#        print(car.upper())       

#foydalanuvchi = input("Ismingizni kiriting?\n>>>")
#if foydalanuvchi.lower() == 'admin':
#    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
#else:
#    print(f"Xush kelibsiz, {foydalanuvchi}!")

#x = int(input("Birinchi sonni kiriting?\n>>>"))
#y = int(input("Ikkinchi sonni kiriting?\n>>>"))
#if x==y:
#    print("Sonlar teng!")
    
#x = int(input("Istalgan son kiriting!\n>>>"))
#print("Musbat son") if x>=0 else print("Manfiy son")

#x = int(input("Istalgan son kiriting!\n>>>"))
#if x>=0:
#    print(x**0.5)
#else:
#    print("Musbat son kiriting")

# 11-dars . if -elif - else

#son = 50
#if son<0:
#    print("Manfiy son")
#else:
#    print("Musbat son")

#yosh = int(input("Yoshingiz nechida?\n>>>"))
#if yosh<=4:
#    narx = 0
#elif yosh <=12:
#    narx = 5000
#elif yosh <18:
#    narx = 8000
#else:
#    narx = 10000
#print(f"Sizga kirish {narx} so'm")

#kun = input("Bugun nima kun?\n>>>")
#harorat = float(input("Havo harorati qanday?\n>>>"))

#if (kun.lower() =='yakshanba' or kun.lower() == "shanba") and harorat>=30:
#    print("Cho'milgani ketdik")
#elif (kun.lower() =='yakshanba' or kun.lower() == "shanba") and harorat<30:
#    print("Uyda dam olamiz")


#narh = 15000 # mijoz 15 so'mga ovqat oldi
#choy = 1
#salat = 0
#non = 1
#kompot = 1
#assorti = 1
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
#if choy:   # agar choy olsa
#    print("Mijoz choy oldi.")
#    narh = narh + 3000
#if salat:  # agar salat olsa
#    print("Mijoz salat oldi.")
#    narh = narh + 5000
#if non:    # agar non olsa
#    print("Mijoz non oldi.")
#    narh = narh + 2000
#if kompot: # agar kompot olsa
#    print("Mijoz kompot oldi.")
#    narh = narh + 5000
#if assorti: # agar assorti olsa
#    print("Mijoz assorti oldi.")
#    narh = narh + 15000
    
#print(f"Jami {narh} so'm")

#menu = ["osh","qazonkabob","shashlik","norin","somsa"]
#buyurtmalar = ["osh","somsa","manti","shashlik"]
#if buyurtmalar:
#    for taom in buyurtmalar:
#        if taom.lower() in menu:
#            print(f"Menuda {taom} bor")
#        else:
#            print(f"Menuda {taom} yo'q")
#else:
#    print("Ro'yxat bo'sh")

# Amaliyot

#son = int(input("Juft son kiriting!\n>>>"))
#if son%2==0:
#    print("Rahmat")
#else:
#    print("Bu juft emas")

#yosh = int(input("Yoshingiz nechida?\n>>>"))
#if yosh<=4 or yosh>=60:
#    narx = 0
#elif yosh <=18:
#    narx = 10000
#else:
#    narx = 20000
#print(f"Sizga kirish {narx} so'm")

#x = float(input("Birinchi sonni kiriting!\n>>>"))
#y = float(input("Ikkinchi sonni kiriting!\n>>>"))

#if x==y:
#    print(f"{x}={y}")
#elif x>y:
#    print(f"{x}>{y}")
#else:
#    print(f"{x}<{y}")

#mahsulotlar = ['kartoshka','sabzi','piyoz','go\'sht','guruch','yog','un','olma','uzum','non']
#savat = []
#print('Savatga mahsulot qo\'shing')
#bor_mahsulotlar = []
#mavjud_emas = []
#for i in range(5):
#    savat.append(input(f"{i+1} - mahsulotni kiriting\n>>>"))
#if savat:
#    for i in savat:
#        if i in mahsulotlar:
#            bor_mahsulotlar.append(i)
#        else:
#           mavjud_emas.append(i)
#else:
#    print("Savatchangiz bo'sh")
#if mavjud_emas==[]:
#    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
#else:
#    print(f"Quyidagi mahsulot dokonimizda yoq: {mavjud_emas}")

#foydalanuvchilar = ['admin','zohid','anvar','ali','xusan']
#foydalanuvchi = input("Login kiriting!\n>>>")
#if foydalanuvchi in foydalanuvchilar:
#    print("Login band, yangi login tanlang!")
#else:
#    print(f"Xush kelibsiz, {foydalanuvchi}")

#son = int(input("Butun son kiriting!\n>>>"))
#for i in range(2,11):
#    if son %i==0:
#        print(f"{son} {i} ga qoldiqsiz bo'linadi")

# 12-dars. Xatolar bilan ishlash.

#son = float(input("Juft son kiriting: "))
#if son%2!=0:
#    print('Bu son juft emas.')
#else:
#    print("Rahmat!")

#yosh = int(input("Yoshingiz nechida?"))

#if yosh<=4 or yosh>=60:
#    narh = 0
#elif yosh < 18:
#    narh = 10000
#else:
#    narh = 20000
#print(f"Chipta {narh} so'm")

#x = float(input("Birinchi sonni kiriting: "))
#y = float(input("Ikkinchi sonni kiriting: "))
#if x==y:
#    print(f"{x}={y}")
#elif x<y:
#    print(f"{x}<{y}")
#else:
#    print(f"{x}>{y}")

#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

#if savat:
#    for mahsulot in savat:
#        if mahsulot in mahsulotlar:
#            print(f"Do'konimizda {mahsulot} bor")
#        else:
#            print(f"Do'konimizda {mahsulot} yo'q")
#else: 
#    print("Savatingiz bo'sh") 

#users = ['alisher1983','aziza','yasina' 'umar']

#login = input("Yangi login tanlang:")

#if login in users:
#    print("Xush kelibsiz!")
#else:
#    print('Login band, yangi login tanalng!')

#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

#bor_mahsulotlar = []
#mavjud_emas = []
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        bor_mahsulotlar.append(mahsulot)
#    else:
#        mavjud_emas.append(mahsulot)

#if mavjud_emas:
#    print("Do'konimizda quyidagi mahsulotlar yo'q:")
#    for mahsulot in mavjud_emas:
#      print(mahsulot)
#else:
#  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

#  13- dars. Github
























































