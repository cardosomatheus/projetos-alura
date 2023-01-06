def jogar():
    print('*'*10)
    print('TESTE DA FORCA')
    print('*'*10)

    palavra_secreta = "python".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while not enforcou and not acertou:
        
        chute_letra = str(input('CHUTE UMA LETRA:')).strip().upper()
        
        if chute_letra in palavra_secreta:
            #se o chute conter uma letra em palavra secreta:
            index = 0 
            for letra in palavra_secreta:
                # loop por letra em palavra secreta
                if chute_letra == letra:
                    # se o chute for igual a uma letra da palavra secreta
                    # adicionamos ela na lista de letra_acertadas atraves do index 
                    letras_acertadas[index] = letra
                    index += 1
        else:
            # se o chute não conter uma letra em palavra secreta, adicionamos um erro
            erros += 1
        
    
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        
    if acertou:
        print(f'parabens, voce ganhou!')

    else:
        print('enforcado, voce perdeu!')        
    


if __name__ == "__main__":
    jogar()