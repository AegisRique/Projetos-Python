#Exibe as opções de conversor de temperaturas para o Usuário
print('''
Bem-Vindo ao Conversor de Temperaturas!
Escolha a Conversão:
1 - Celsius para Fahreinheit
2 - Fahrenheit para Celsius
3 - Celsius para Kelvin
4 - Kelvin para Celsius
''') 

#Aqui o usuário deve digitar o número das opções (1-4) e em seguida digitar a temperatura
option = input('Digite o número da conversão: ') 
temp = float(input('Digite a Temperatura: ')) 

#Receber a temperatura pelas opções e as converter
if option == '1':
    result = (temp * 9/5) + 32
    print(f'{round(temp)}°C = {round(result)}°F')

elif option == '2':
    result = (temp - 32) * 5/9
    print(f'{round(temp)}°F = {round(result)}°C')

elif option == '3':
    result = (temp + 273.15)
    print(f'{round(temp)}°C = {round(result)}K')

elif option == '4':
    result = (temp - 273.15)
    print(f'{round(temp)}K = {round(result)}C°')

else:
    print('Opção Inválida!') #Se nenhum número for válido (1-4)
