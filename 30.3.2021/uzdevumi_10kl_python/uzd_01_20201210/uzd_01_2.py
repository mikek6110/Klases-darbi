# Izveidot programmu, kura prasa lietotâjam ievadît cilindra râdiusu un tâ augstumu, tiek aprçíinâts cilindra laukums un tilpums. Rezultâts tiek parâdîts konsolç.
# tilpums = 3.14 * râdiuss * râdiuss * augstums
# laukums = 2 * (3.14 * râdiuss * râdiuss) + augstums * (2 * 3.14 * râdiuss)



radiuss=float(input('Ievadi radiusu:'))
augstums=float(input('Ievadi augstumu'))

tilpums= 3.14*radiuss*radiuss*augstums
laukums=2*(3.14*radiuss*radiuss)+augstums*(2*3.14*radiuss)

print('Tilpums ir:',tilpums)
print('Laukums ir:',laukums)