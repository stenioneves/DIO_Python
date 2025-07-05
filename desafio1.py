import os

saque=0
limite_saque =3
valor_diario = 500
saldo= 300
d=0
menu= f'''
    Sistema Bancário v1 
    Selecione um opção abaixo:
    0 - sair
    1 - depositar
    2 - sacar
    3 - exibir extrato

    Digite uma opção:

'''



while True:
     
    op=int(input(menu))
    if op ==1:
        valor=float(input("Digite o valor para depositar :"))
        if valor<=0:
            print(f"{valor} é inválido!, votando para o menu..")
        else:
            saldo+= valor
            print("Deposito realizado!")
            d+=1
    elif op==2:
        valor=float(input("Digite um valor para sacar:"))
        if valor<=valor_diario:
            if saque<limite_saque:
                if(saldo>= valor):
                  saldo-=valor
                  print("Saque realizado!!! :)")
                  saque+=1  
                else :
                  print("Saldo insuficiente!! ):")
            else :
                print("Limite de saque diário excedido !")
        else :
            print("Limite de valor superior ao permitido :(")
    elif op==3 :
        print( "Extrato ")
        print(f"Deposito: {d}")
        print(f"saques: {saque}")
        print(f"Seu saldo é R$:{saldo: .2f}")
    elif op==0:
        print("Good Bye !Até proxima :)")
        break
    else:
        print("Opção invalida!!!")




