print('Ingresa la cadena de caracteres: ')
cad = input().lower()
n = 0
m = 0
t = 0
for i in cad:
    letra = ord(i)
    if letra == 97:
        n = n+1
    elif letra == 98:
        m = m+1
    else:
        t = t+1
if t >= 1:
    print('No pertenece al conjunto')
elif 2*n == m:
    print('Pertenece al conjunto')
else:
    print('No pertenece al conjunto')
