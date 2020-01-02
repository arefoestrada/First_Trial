angka = input('Masukkan angka Anda: ')
angka = eval(angka)
if angka % 2 == 0:
	print('Angka {} adalah bilangan genap'.format(angka))
else:
	print('Angka {} adalah bilangan ganjil'.format(angka))