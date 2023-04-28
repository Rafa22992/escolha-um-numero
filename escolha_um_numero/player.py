from random import choice
import os

def advinhe_num():
    
    numeros = []
    bordas = '-' * 20
    print(bordas)
    print(f'{"ADVINHE O NÚMERO":=^20}')
    print(bordas)

    while True:
            quant_num = input('Escolha a quantidade de numeros: ')
            print(bordas)
            os.system('cls')

            if quant_num.isalpha():
                 print('Digite apenas números!!!')
                 print(bordas)
                 continue
            
            print(f'Muito bem, você escolheu {quant_num} números !!!')
            print(bordas)
            int_num_quant = int(quant_num)

            numeros_range = range(1, int_num_quant + 1)
                
            for n in numeros_range:
                numeros.append(n)
                emb_num = choice(numeros)
                    
            num_escolhido = input('Advinhe o número: ')
            print(bordas)
            os.system('cls')

            if num_escolhido.isalpha():
                 print('Digite apenas números!!!')
                 print(bordas)
                 continue

            int_num_esc = int(num_escolhido)

            if int_num_esc > len(numeros):
                print(f'Você só pode escolher até o {quant_num}')
                print(bordas)
                continue

            if int_num_esc == emb_num:
                print(f'PARÁBENS VOCÊ ACERTOU O NÚMERO QUE É ({emb_num})!!!')
                print(bordas)
                continue

            else:
                print(f'AAAAAAH, você errou, o número correto era ({emb_num})')
                print(bordas)

            
advinhe_num()