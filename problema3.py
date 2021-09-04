def contra_valida():
    contra = input('Por favor, a continuación, crea tu contraseña: ')
    print('')
    
    long = len(contra)
    mayus = False
    minus = False
    '''letra_rep = ''
    letra_rep_valida = False'''
    num = False
    '''especiales = ''
    especiales_valida = False'''
    espacio = False

    valida_contra = False
    valida = False
    
    while valida_contra == False:
        if contra != contra.upper() and contra != contra.lower():
            mayus = True
            minus == True
        '''if lista[i] == lista[i+1]:
            letra_rep_valida == True'''
        '''if int in contra:
            num == True'''
        '''if '!','@','#','$','%','ˆ','&','*','-','_','+','=','?':
            especiales_valida == True'''
        if ' ' in contra:
            espacio == True
        valida_contra == True
        while valida == False:
            if long >= 16:
                valida == True
            else:
                contra = input('La contraseña debe tener al menos 16 caracteres: ')
            if mayus==True and minus==True and num==True:
                valida == True
            else:
                valida == False
                contra = input('La contraseña debe tener mayúsculas, minúsculas y al menos 4 números: ') 
            if espacio==True:
                valida == False
                contra = input('La contraseña no debe tener espacios: ')
            else:
                valida == True

    print('¡Contraseña aceptada, bienvenido!')
