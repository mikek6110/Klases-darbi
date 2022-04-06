
# Atrast pozitīva skaitļa ciparu summu. Piemērs: 14214 => 12

skaitlis=input('Ievadi skaitli:')
sum=0
if int(skaitlis)<0:
    print('Nav ievadits pozitivs skaitlis.')
else:
    for i in skaitlis:
        sum+= int(i)    

print(f'Ievadita skaitla summa ir {sum}.')