i = 0   
while i < 6:
    print("Sayı:", i)
    i = i + 1
#%% 
for j in range(1,6):
    print("Sayı:" + str(j)) 
    #ya da print("Sayı", j)
# %%       
sum = 0
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in nums:
    sum = sum + num    
    if sum > 28:
       break
    elif sum < 28:
        print("Toplam:", sum)
    else:
        print("Sonuc:", sum)
# %%            
for a in nums:
    if a == 5:
        continue
    print(a)
# %%      
def bolme(sayi1, sayi2):
    return (sayi1 / sayi2)
print(bolme(1113,1))
# %%  
def bolme2(sayi1, sayi2):
    try:
        return (sayi1 / sayi2)
    except ZeroDivisionError:
        return None

print(bolme2(1113,0))
# %%