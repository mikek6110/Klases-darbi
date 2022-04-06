
# Atrast cik skaitļi norādītajā intervālā dalās ar lietotāja norādīto dalītāju.


sakt=int(input('Sakuma vertiba:'))
end=int(input('Beigu vertiba:'))
dala=int(input('Dalitaj vertiba:'))

cik=0

for i in range(sakt,end+1):
    if i%dala==0:
        cik+=1
#print(cik) 
print(f'{cik} skaitli dalas ar {sakt} un {end}, kas dalas ar {dala}.')