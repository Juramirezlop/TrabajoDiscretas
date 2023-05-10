def function(cad) -> bool:
    
    if cad == 'abb':
        return True 

    if len(cad) < 3:
        return False

    return function(cad[1:-2])


if function(input()):
    print('Pertenece')
else:
    print('No Pertenece')
