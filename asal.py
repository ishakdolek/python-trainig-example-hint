primeNumberList=list()
number=100 #int(input("Sayı GİRİNİZ:")
for  item in range(2,number):
    isPrime = True
    i=item
    while(i > 2):
        i-=1
        if(item%i==0):
          isPrime=False
          break
      
    if(isPrime==True):
        primeNumberList.append(item)
          
print(primeNumberList)

