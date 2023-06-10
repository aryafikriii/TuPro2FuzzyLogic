#============LIBRARY============
import pandas as pd
import matplotlib.pyplot as plt

#===========MEMBACA DATA============
data = pd.read_excel("bengkel.xlsx")

#==========MEMBERSHIP HARGA==========
def Pricey(x):
    '''
    Fungsi ini digunakan untuk membership harga bengkel yang mahal
    '''
    a, b = 6, 8

    if x > b: 
        return 1
    elif x <= a: 
        return 0
    elif x > a and x <= b: 
        return ((x - a) / (b - a))

def Average(x):
    '''
    Fungsi ini digunakan untuk membership harga bengkel yang sedang
    '''
    a, b, c, d = 4, 6, 7, 9

    if x > b and x <= c: 
        return 1
    elif x <= a or x > d: 
        return 0
    elif x > a and x <= b: 
        return ((x - a) / (b - a))
    elif x > c and x <= d: 
        return ((d - x) / (d - c))

def Cheap(x):
    '''
    Fungsi ini digunakan untuk membership harga bengkel yang murah
    '''
    a, b = 4, 6

    if x <= a: 
        return 1
    elif x > b: 
        return 0
    elif x > a and x <= b: 
        return ((b - x) / (b - a))

#==========PLOT MEMBERSHIP HARGA==========
x = [i for i in range(11)]

yPricey = [Pricey(i) for i in x]
yAverage = [Average(i) for i in x]
yCheap = [Cheap(i) for i in x]

plt.figure(figsize=(10,4))
plt.title('Membership Harga',fontsize = 20) 
plt.plot(x, yCheap, label = 'Murah')
plt.plot(x, yAverage, label = 'Sedang')
plt.plot(x, yPricey, label = 'Mahal')
plt.xlabel('Nilai')
plt.ylabel(r'$\mu\ (x)$')
plt.show()

#==========MEMBERSHIP SERVIS==========
def Bad(x):
    '''
    Fungsi ini digunakan untuk membership kualitas bengkel yang buruk
    '''
    a, b = 50, 70

    if x <= a: 
        return 1
    elif x > b: 
        return 0
    elif x > a and x <= b: 
        return (b - x) / (b - a)

def Normal(x):
    '''
    Fungsi ini digunakan untuk membership kualitas bengkel yang sedang
    '''
    a, b, c, d = 50, 60, 70, 85

    if x > b and x <= c: 
        return 1
    elif x <= a or x > d: 
        return 0
    elif x > a and x <= b: 
        return ((x - a) / (b - a))
    elif x > c and x <= d: 
        return ((d - x) / (d - c))

def Excellent(x):
    '''
    Fungsi ini digunakan untuk membership kualitas bengkel yang terbaik
    '''
    a, b = 75, 80
    
    if x > b: 
        return 1
    elif x <= a: 
        return 0
    elif x > a and x <= b: 
        return ((x - a) / (b - a))

#==========PLOT MEMBERSHIP SERVIS==========
x = [i for i in range(101)]

yBad = [Bad(i) for i in x]
yNormal = [Normal(i) for i in x]
yExcellent = [Excellent(i) for i in x]

plt.figure(figsize=(10,4))
plt.title('Membership Servis',fontsize = 20) 
plt.plot(x, yBad, label = 'Bad Service')
plt.plot(x, yNormal, label = 'Normal Service')
plt.plot(x, yExcellent, label = 'Excellent Service')
plt.xlabel('Nilai')
plt.ylabel(r'$\mu\ (x)$')
plt.show()

#==========FUZZIFIKASI==========
def fuzziHarga(priceValue):
    '''
    Fungsi ini digunakan untuk melakukan proses fuzifikasi pada harga
    '''
    priceSet = []
    priceSet.append(Pricey(priceValue))
    priceSet.append(Average(priceValue))
    priceSet.append(Cheap(priceValue))
    return priceSet

def fuzziServis(serviceValue):
    '''
    Fungsi ini digunakan untuk melakukan proses fuzifikasi pada servis
    '''
    serviceSet = []
    serviceSet.append(Bad(serviceValue))
    serviceSet.append(Normal(serviceValue))
    serviceSet.append(Excellent(serviceValue))
    return serviceSet

#==========INFERENSI==========
def inference(priceSet, serviceSet):
    '''
    Fungsi ini digunakan untuk melakukan proses inferensi, dengan menggunakan model sugeno.
    Input menggunakan fungsi keanggotaan Trapesium, Linier Naik dan Linier Turun untuk Servis dan Harga. 
    '''
    inferensi = []
    Terbaik, Baik, Buruk = [], [], []

    #Bengkel yang Terbaik
    Terbaik.append(min(priceSet[2], serviceSet[2]))
    Terbaik.append(min(priceSet[2], serviceSet[1]))
    Terbaik.append(min(priceSet[1], serviceSet[2]))

    #Bengkel Rata-rata
    Baik.append(min(priceSet[0], serviceSet[2]))
    Baik.append(min(priceSet[1], serviceSet[1]))
    Baik.append(min(priceSet[0], serviceSet[1]))
    
    #Bengkel yang buruk
    Buruk.append(min(priceSet[0], serviceSet[0]))
    Buruk.append(min(priceSet[1], serviceSet[0]))
    Buruk.append(min(priceSet[2], serviceSet[0]))

    inferensi.append(max(Terbaik))
    inferensi.append(max(Baik))
    inferensi.append(max(Buruk))
    
    return inferensi

#==========DEFUZIFIKASI==========
def defuzzification(inferenceSet):
    '''
    Fungsi ini digunakan untuk melakukan proses defuzifikasi dengan menggunakan Weighted Average.
    '''  
    return ((inferenceSet[0]*100) + (inferenceSet[1]*80) + (inferenceSet[2]*50)) / (inferenceSet[0] + inferenceSet[1] + inferenceSet[2])

xBuruk = [50,50]
xBaik = [80,80]
xTerbaik = [100,100]

y = [0,1]

plt.figure(figsize=(10,4))
plt.title('Defuzzifikasi',fontsize = 20)
plt.plot(xBuruk,y,label='Buruk')
plt.plot(xBaik,y,label='Baik')
plt.plot(xTerbaik,y,label='Terbaik')
plt.xlabel('Nilai')
plt.ylabel(r'$\mu\ output$')
plt.show()

#==============MAIN==============
hasilAkhir = []
for i in range(100):
    x = fuzziHarga(data['harga'][i])
    y = fuzziServis(data['servis'][i])
    z = inference(x, y)
    hasilAkhir.extend([defuzzification(z)])

result = pd.DataFrame(hasilAkhir)
result.columns = ['hasil']
id = [i for i in range(1, len(result)+1)]
result['id'] = id

rank = pd.merge(data, result, how='inner', on ='id')
rank.sort_values(['hasil'], ascending=False, inplace=True)
rank.head(10)
rank[:10].to_excel('peringkat.xlsx')
#================================