from random import choice

def advinhe_num():
    numeros = []
    bordas = '-' * 20

    def quant_num_range():
        quant_num = input('Escolha a quantidade de numeros: ')
        print(bordas)
        print(f'Muito bem, você escolheu {quant_num} números !!!')
        print(bordas)
        int_num_quant = int(quant_num)

        def embaralha_nums():
            numeros_range = range(1, int_num_quant + 1)
            
            for n in numeros_range:
                numeros.append(n)
                emb_num = choice(numeros)
                
            num_escolhido = input('Advinhe o número: ')
            print(bordas)

            int_num_esc = int(num_escolhido)

            if int_num_esc == emb_num:
                print(f'PARÁBENS VOCÊ ACERTOU O NÚMERO QUE É ({emb_num})!!!')
                print(bordas)

            else:
                print(f'AAAAAAH, você errou, o número correto era ({emb_num})')
                print(bordas)

        embaralha_nums()   
    quant_num_range()

advinhe_num()