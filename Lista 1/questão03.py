#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input("insira um dia: " ))
horas = int(input("insira as horas: "))
minutos = int(input("insira os minutos: "))
segundos = float(input("insira os segundos: "))

total = dias * 24 * 60 * 60 + horas * 60 * 60 + minutos * 60 + segundos

print total
