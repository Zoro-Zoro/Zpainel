import os
import time
import requests
from source.ascii import *
from faker import Faker
import base64



fake = Faker('pt-br')
cpf = fake.cpf()
rg = fake.rg()
cnpj = fake.cnpj()
name = fake.name()
address = fake.address()



def voltar():
	print(f'{vm}-={br}[{vd}01{br}] {br}Voltar \n{vm}-={br}[{vd}02{br}] {br}Sair')
	back = input(f' {am}=+> {f}').replace('0', '')
	if back == '1' or '01':
		clear()
		menu()
	elif back == '2' or '02':
		exit()



def menuGeradores():
	opts = {'geradores': ['gerar CNPJ', 'gerar CPF', 'gerar RG', 'gerar NOME', 'gerar MORADA']}
	api = 'https://www.4devs.com.br/ferramentas_online.php'
	
	
	clear()
	print(lg)
	print(line)
	for c, item in enumerate(opts['geradores']):
		print(f'{br:^28}[{vd}{c+1}{br}] {item}')
	print(line)
	
	op = input(f'{vd}=+> {f}')
	
	if op == '1':
		clear()
		print(lg)
		print(f'{vm}-={br}[{vd}CNPJ{br}] {cnpj}')
		voltar()
	elif op == '2':
		clear()
		print(lg)
		print(f'{vm}-={br}[{vd}CPF{br}] {cpf}')
		voltar()
	elif op == '3':
		clear()
		print(lg)
		print(f'{vm}-={br}[{vd}RG{br}] {rg}')
		voltar()
	elif op == '4':
		clear()
		print(lg)
		print(f'{vm}-={br}[{vd}NOME{br}] {name}')
		voltar()
	elif op == '5':
		clear()
		print(lg)
		print(f'{vm}-={br}[{vd}MORADA{br}] {address}')
		voltar()
	else:
		voltar()

