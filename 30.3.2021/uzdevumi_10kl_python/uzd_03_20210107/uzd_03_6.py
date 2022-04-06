
# Izveidot reizināšanas tabulu lietotāja ievadītam skaitlim.

skaitlis=input('Ievadi skaitli:')
sk=int(skaitlis)


if sk<0:
    print('Skaitlis ir negativs.')
else:
    for i in range(10):
        print(f"{sk}*{i+1}={sk*(i+1)}")