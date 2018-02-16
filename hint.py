
# print("Test")
# print(type(12)) #datanın türünü veriyor.
# print("Mustafa","İshak","Dölek",sep,="_")
# print("{}".format(12))

# #list operation
# liste=["Elma",23]
# liste = list()

# len(liste)
# liste[4:] #liste 4. elemandan başla
# #iki liste toplana bilir.
# liste1= list()
# liste2=list()
# liste1[:2]

# #liste bazı metotlar
# liste.append() #yeni bir elemen eklemeyi sağlıyor
# liste.pop() #listeden eleman çıkartma işlemi yapıyor
# liste.sort() #sıralama yapıyor.
# liste.sort(reverse=true) #sıralama yapıyor.
# #içe içe listeler olanak sağlıyor.

# #dememler veya kavramlar
# demet=(1,2,3)
# demet.count(1) #kaç tane geçtyiğini buluyor.
# demet.index("java")# demet içinde bulunuyorlar.end='\n'

# #Dictionary
# dict={"bir":1} #{"key":value}

# #kullanıcıdan input alma
# a=input("Lütfen değer girin:")#kullanıdeba string değer alınır
# a=int(input("Lütfen değer girin:"))#bu  şekilde casting yapılabilir.end='\n'

# try:
#     print(a)
# except expression as identifier:
#     print("Yanlış değer girdin!")

#For Döngüleri
#in # içerir
# liste=[1,2,3,4,54,55,43,13]
# for item in liste: #for döngüsü
#     if item%2!=0:
#         print(item)
# demet=(12,23,23,43)
# #demetleri liste içinde kullanılabilir # liste= [(2,3),(32,12)]
# for item in demet:
#     print(item)

# while(True):
#     print("Selam")
#     break

# liste=range(0,20)
# print(*liste)

# for item in range(1,20):
#     print("*"*item)

# i=0
# while True:
#     print("Selam"*i)
#     i+=1
#     continue
#     if(i==10):
#         break
# List Comprehension
# liste3=[2,42,32,,421,]
# liste4=[i for i in liste3] #TODO

#Fonkisyonlar görevi


# def sum1():
#     print(a + b)

#Fibonnacci Serisi Girilen sayıya kadar buluyor herhalde :)
# n=100
# print("Girilen Sayı:42")
# a=0
# b=1
# sum1()
# liste=list()
# liste.append(a)
# liste.append(b)
# while (b < n):
#    newItem2=a+b
#    a=b
#    b=newItem2
#    liste.append(newItem2)

# print(liste[:len(liste)-1]) # listeki son elemanın çıkartılması gerekir
# # help(a.append) burada metotun nasıl kullanıldığını bize gösteriyor.

# def Selamla(isim):
#     print(isim)

# def Fact(number):
#     if(number==1 or number ==0):
#         return
#     return number*(number-1)

# fact=int(Fact(4))
# print(fact)
# def Selamla(isim="İshak"):# default değer atmak için kullanılır.
#     print(isim)
# toplama(*a) #liste verilebilir
# #Global ve Yerel Değişkenler
# d=5
# def fonc():
#   global d #gloabaldak değerleri kullan.
#   d=3
# text= input("Metin giriniz!")
# text = "Ben sınıf öğretmeniyim bu işi de öğrencilerime katkıda bulunacak uygulamalar yapmak amacıyla öğreniyorum. Sınıflarımızda öğrenciler okudukları metinlerdeki kavramlara, kelimelere aşina olmadıkları için çok yavaş okuyorlar, bu yüzden de okuduklarını anlamıyorlar. Bu sorunun çözümüne katkıda bulunacak şöyle bir programa ihtiyacım var"
# wordList=text.split(" ")
# print(wordList)
# wordList.sort(key=lambda item: (-len(item), item),reverse=True)
# print(wordList)
# #Lambda
# mutlp=lambda x:x*3
# import math as name # math modulu programa dahil edilmiş oluyor.
# math.cos(90)
# math.floor(4.3)
# from math import* # * tüm funk alır
# import random
# import time
# print("""******************
# Rasgele Kavramı
# ***************************""")
# Object Orient Programing
# class Cars():
#     model ="Tes"
#     renk  = "red"
#     def __init__ (self,model,renk):
#         self.model=model
#         self.renk=renk
#      def showInfo(self):
#          print("{} {}".format(self.model,self.renk))
# class Human(Cars):
#     pass
# human=Human("Tes","Red")

# class Book():
#     def __init__(self,yazar):
#         self.yazar = yazar
# book = Book("Selam")
# print(book.yazar)

# file = open("filepath", "w",encoding="utf-8")
# file.write("İshak DÖLEK")
# file.append(" 1989 doğumludur.")  # olan dosyaya veri ekliyor.
# file.close() #dosyayı kapatır.


# file=file.read("filepath","r") # dosyayı oku

# try:
#     file = file.read("filepath", "r",encoding="utf-8")  # dosyayı oku
# for i in file
#     print(i,end="")
# except expression as identifier:
#     pass

# liste=file.readlines() # her bir satırı okur bir diziye atar.

# with open("filepath","r+",encoding=None) as file: #r+ olduğu zmana hem okuma hem yazma işlemi gerleşir.
#     file.seek()# dosya üzerinde arama yapar.

# def double(x):
#     return x*2

# list(map(double,[1,2,3])

# reduce(funcName,datatype) # kümülatif bir sonuç verir.

# listedeki max eleman bulmak için reduce kullanılabilir.

# from functools import reduce

# def max(x,y):
#     if(x>y):
#         return x
#     else:
#         return y


# z=reduce(max ,[1,2,7,4,5])
# print(z)

# filter founksiyonu bool değer döndürüyor
#  filter(lambda x:x%2==0,[1,2,4,5,6,7])

# # zip listeleri gruplama için kullanılır

# enumerate

# bin(2) #
# abs() #mutlak değer
# hex
# round("sayı yaz","kaç basamak gösterilecek virgülden sonra")#yuvarlama
# # max ve min () sayıdki max verir
# print(bin(4))

# # pow üstel sayılarda kullanılıyor
# upper ==UpperCase
# lower== LowerCase
# replace
# 
# liste="selam ben yoruldum hayat".split(" ")

# x=set() #küme leme yapıyor
# type(x)
# x.add(5)
# x.discard(4)
# def funcName(*args): # birden fazla değer gönderilebilir.
#     for i in args
#     print(i)
# def functools(**kwarags): # değer gönderip demet gib çalışabilir.
#     print(kwarags)
# # del object #bunula obje silinebilir.
# def Test1:
#     def Test2:# bu local metot olur dişarıdan erişelemez
#         print("Selam")
# # python içerisinde başka bir metot geri döndürülebilir.
# # Decorator kullanımı çok önemli
# def zaman_hesapla(funcName):
#     def wrapper(sayılar):
#         start=time.time()
# @zaman_hesapla
# def  funcName():
#     raise StopIteration: # bu hata fırlatıyor

# #generator
# @staticmethod
# sonuc = []
# def kare_al():

#     for i in range(1,6):
#         sonuc.append(i**2)
#     return sonuc


# print(sonuc)

# from datetime import datetime

# import matplotlib.pyplot as plt


# import locale

# print(datetime.now())
# now=datetime.now()
# print(now.year)

# locale.setlocale(locale.LC_ALL,"")


# plt.plot()
# plt.show()


###os fonksiyorun

# import os
# print(os.getcwd()) # buluna dizini veriyor.
# # os.chdir("c:\x\") # dizini değiştirebiliyoruz 
# os.mkdir("deneme") # yolu create ediyor
# os.rmdir()#remove directory
# os.rename("old.txt","new.txt")#rename directory or file
# os.stat("xx.txt").st_mtime # dosya hakkı9nda bilgi veriyor
# for i in os.walk("c:/x/x"): # burada bulunan yerdeki tüm klasörleri veriyor
#         print(i)
#         if(i.endswith(".txt")):
#             print(i)



### sys  func

import sys

# a = int(input("a:"))
sys.stderr.write("Bu bir hata mesajıdır!")
sys.stderr.flush()









