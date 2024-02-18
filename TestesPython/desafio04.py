obj = input('Digite qualquer coisa: ')
r1 = obj.isnumeric()
r2 = obj.isalpha()
r3 = obj.isalnum()

print('É númerico: {}, é uma palavra: {}, é uma palavra com número: {}'.format(r1,r2,r3))
