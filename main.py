#preguiça :)

import os
from sys import executable


try:
	import keyboard, requests
except:
	os.system('pkg install figlet && figlet Z-PAINEL')
	print(f'\n{az}============================== \n{br}[{am}i{br}] Instalando Modulos... {br}[{am}i{br}] \n{az}==============================')
	os.system(executable+' -m pip install requests phonenumbers keyboard faker')
import time;import requests;from faker import Faker;import base64;import datetime;from source.ascii import *;from source.geradores import *


#Não Juge o meu codigo!


##########################
r = requests.get('https://ip-api.org/json').json();ip_res = f'{vm}-={br}[{az}Seu IP{br}] {r["ip"]}'
##########################

#####
time = datetime.datetime;date = datetime.date;hora = time.today().hour;minute = time.today().minute;dia = date.today().day;mes = date.today().month;ano = date.today().year
####


error = f'{vm}-={br}[{az}consulta offline ou digitos invalidos{br}]Error!'
by_zorro = f'\n{vm}-={br}[{az}+{br}] {br}CONSULTA FEITA PELO PROGRAMA Zp4in3l\n{vm}-={br}[{az}+{br}] {br}by: Zorrinho'
IP = {'ipgeolocation': 'https://api.ipgeolocation.io/ipgeo?apiKey=be35b8be10834da8af67daff92154013&ip={}', 'ip': 'http://ip-api.com/json/{}', 'ipfind': 'https://api.ipfind.com/?ip={}&auth=f56dbef6-8fd8-4105-af74-a220f9a71610'}
CEP = {'postmon': 'https://api.postmon.com.br/v1/cep/{}', 'viacep': 'https://viacep.com.br/ws/{}/json/', 'apicep': 'https://ws.apicep.com/cep/{}.json'}


#################################################
def ent():
	back = input(f' {br}<{az}ENTER PARA VOLTAR{br}> ').replace('0', '')
	if back == '1' or '01': clear();loop()
	elif back == '2' or '02': exit()

def restart():
	os.system(executable+'cd && rm -fr Zpainel && git clone https://github.com/Zoro-Zoro/Zpainel')
#################################################


def ip():
	clear()
	print(lg)
	print(f'{vm}--={f}{br}[{az}CONSULTA IP{br}]{f}\n')
	for c, item in enumerate(IP.keys()):
		print(f'- {br}[{f}{az}{c+1}{br}] {br}{item}')
	n1 = str(input(f'\n {vd}=+> '))
	for num, api in enumerate(IP.values()):
		if n1 == f'{num+1}' or n1 == f'0{num+1}':
			ip = input(f'{vm}-=={f}{br}[{az} ip {br}] {vd}+=>{f}')
			res = requests.get(api.format(ip)).json()
			print(by_zorro)
			for key, item in res.items():
				print(f'{vm}-= {br}[{az}{key}{br}] {br}{item}')
			ent()
################
def cep():
	clear()
	print(lg)
	print(f'{vm}--={f}{br}[{az}CONSULTA CEP{br}]{f}')
	for c, item in enumerate(CEP.keys()):
		print(f'- {br}[{f}{az}{c+1}{f}{br}] {br}{item}{f}')
	n1 = str(input(f'\n {vd}=+> {f}'))
	for num, cep in enumerate(CEP.values()):
		if n1 == f'{num+1}' or n1 == f'0{num+1}':
			cep1 = input(f'{vm}-=={f}{br}[{az} cep {br}] {vd}+=> {f}')
			if len(cep1) == 9:
				res = requests.get(cep.format(cep1)).json()
				print(by_zorro)
				for key, value in res.items():
					print(f'{vm}-={br}[{az}{key}{br}]{br}{value}')
				ent()
			else:
				print(f' {vm}[!] valor invalido \n digite apenas numeros \n {f}ex: {az}01010-010 {f}');ent()
###################
def cnpj():
	clear()
	print(lg)                           
	req=requests.get('https://www.receitaws.com.br/v1/cnpj/%s'%input(f'{vm}--=={f}{br}[{az} fonte RECEITA FEDERAL {br}]{f} \n{vm}--=={f}{az}[ {az}cpnj{az} ]{f} {am}+=>{f} ')).json()
	print(by_zorro)
	for key, value in req.items():
		print(f'{vm}-={br}[{az}{key}{br}]{value}')
	ent()
####################
def cpf():
	clear()
	print(lg)
	req=requests.get('http://api.trackear.com.br/basepv/cpf/%s/noip'%input(f'{vm}--=={f}{br}[{az} fonte TRACKEAR {br}]{f} \n{vm}--=={br}[ {az}cpf{br} ] {vd}+=>{f} ')).json()
	print(by_zorro)
	for key, value in req.items():
		print(f'{vm}-={br}[{az}{key}{br}]{value}')
	ent()
	clear()
###################
def numero():
	clear()
	print(lg)
	# a mesma api com outra key: http://apilayer.net/api/validate?access_key=f134484ed14981a957368f2a06aaa251&number={}&country_code=&format=1
	#token de asseço f134484ed14981a957368f2a06aaa251
	# conta: https://numverify.com/dashboard
	req=requests.get('http://apilayer.net/api/validate?access_key=8c830d7095b0888b0b6941b01dac1a1e&number=%s&country_code=BR&format=1'%input(f'{vm}--=={f}{br}[{az} fonte NUMERY {br}]{f} \n{vm}--=={br}[ {az}number{br} ] {vd}+=>{f} ')).json()
	print(by_zorro)
	for key, value in req.items():
		print(f'{vm}-={br}[{az}{key}{br}]{value}')
	ent()
##################
def localidades():
	clear()
	print(lg)
	req=requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/%s'%input(f'{vm}--=={f}{br}[{az} fonte IBGE {br}]{f} \n{vm}--=={br}[ {az}estado{br} ] {vd}+=>{f} ')).json()
	print(by_zorro)
	for key, value in req.items():
		print(f'{vm}-={br}[{az}{key}{br}] {value}')
	ent()
##################
def nome():
	clear()
	print(lg)
	api = "http://ghostcenter.xyz/api/nome/"
	usu = input(f'{vm}--=={f}{br}[{az} fonte GHOSTCENTER {br}]{f} \n{vm}--=={br}[ {az}nome{br} ] {vd}+=>{f} ').split()
	usu = "%20".join(usu)
	req = eval(requests.get(api+usu).text)
	try:
		for item in req['dados']:
			for key, value in item.items(): print(f'{vm}-={br}[{az}{key}{br}]{br}{value}');print(by_zorro);ent()
	except: print(error);ent()
#################
def covid():
	clear()
	print(lg)
	req=requests.get('https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/%s'%input(f'{vm}--=={f}{br}[{az} fonte BRASILAPI {br}]{f} \n{vm}--={br}[ {az}estado - Sigla{br} ] {az}+=>{f} ')).json()
	print(by_zorro)
	for key, value in req.items():
		print(f'{vm}-={br}[{az}{key}{br}]{br}{value}')
	ent()
################
def ddd():
	clear()
	print(lg)
	req = requests.get('https://viaddd.com.br/api/ddd/%s'%input(f'{vm}-=={br}[ {az}fonte VIADDD{br} ] \n{vm}-={br}[ {az}ddd{br} ] {az}=+> {f}')).json()
	print(by_zorro)
	print(f'{vm}-={br}[{az}Estado{br}] {req["Estado"]}')
	for c, item in enumerate(req['Municipios']):
		print(f'{vm}-={br}[{az}Municipio {c+1}{br}] {item}')
	ent()
#################
def bank():
	clear()
	print(lg)
	req=requests.get('https://brasilapi.com.br/api/banks/v1/%s'%input(f'{vm}-={br}[ {az}fonte BRASILAPI{br} ] \n{vm}-={br}[ {az}banco{br} ] {az}=+> {f}')).json()
	clear()
	print(by_zorro)
	for key, value in req.items():
		print(f'{vm}-={br}[{az}{key}{br}] {value}')
	ent()
#################
def bin():
	clear()
	print(lg)
	req=requests.get(f'https://lookup.binlist.net/%s'%input(f'{vm}-=={br}[ {az}fonte BINLIST{br} ] \n{vm}-={br}[ {az}bin{br} ] {az}=+> {f}')).json()
	for key, value in req.items():
		print(f'{vm}-={br}[{az}{key}{br}] {value}')
	ent()
################
def placa():
	clear()
	print(lg)
	placa = input(f'{vm}-={br}[ {az}fonte APICARROS{br} ] \n{vm}-={br}[ {az}placa{br} ] {az}=+> {f}')
	url=requests.get('https://apicarros.com/v1/consulta/{}/json'.format(placa), verify = False).json() # JSQ7436
	clear()
	print(lg)	
	for key, value in url.items():
		print(f'{vm}-={br}[{az}{key}{br}] {value}')
	ent()
################
def crm():
	clear()
	print(lg)
	crm = input(f'{vm}-=={br}[{az} fonte CONSULTACRM {br}] \n{vm}-=={br}[{az} crm {br}] {az}=+> {f}')
	uf_crm = input(f'{vm}-={br}[{az} uf {br}] {az}=+> {f}')
	req = requests.get('https://www.consultacrm.com.br/api/index.php?tipo=crm&uf={}&q={}&chave=4188146193&destino=json'.format(uf_crm, crm)).json() # 814830 rj
	for key, value in req.items():
		print(f'{vm}-={br}[{az}{key}{br}] {value}')
	ent()
################
def apis():
	clear()
	print(lg)
	apis = {'zapis': ['https://www.consultacrm.com.br/api/', 'https://apicarros.com/v1/consulta/', 'https://brasilapi.com.br/api/banks/v1/', 'https://lookup.binlist.net/', 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/', 'http://ghostcenter.xyz/api/nome/', 'https://viaddd.com.br/api/ddd/', 'http://apilayer.net/api/', 'http://api.trackear.com.br/basepv/cpf/', 'https://www.receitaws.com.br/v1/cnpj/']}
	
	print(f'{vm}-={br}[{az}*{br}]Lista de APIs')
	print(line)
	for c, item in enumerate(apis['zapis']):
		print(f'{br}[{az}API 0{c+1}{br}] {item}')
	ent()
################
def cotacao():
	clear()
	print(lg)
	req = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL').json()
	req_usd = req['USDBRL']
	req_eur = req['EURBRL']
	req_btc = req['BTCBRL']
	print(f'{vm}-={br}[{az}cotação do DOLAR!{br}]')
	for key, value in req_usd.items():
		print(f'{vm}-={br}[{az}{key}{br}] {value}')
	print(line)
	print(f'{vm}-={br}[{az}cotação do EURO!{br}]')
	for key, value in req_eur.items():
		print(f'{vm}-={br}[{az}{key}{br}] {value}')
	print(line)
	print(f'{vm}-={br}[{az}cotação do BITCOIN!{br}]')
	for key, value in req_btc.items():
		print(f'{vm}-={br}[{az}{key}{br}] {value}')
	ent()
################
def menu():
	clear()
	function = {'consultas': ['IP', 'CEP', 'CNPJ', 'CPF', 'NOME', 'LOCALIDADES', 'COVID', 'GERADORES', 'DDD', 'BANCO', 'BIN', 'PLACA', 'CRM', 'COTAÇÃO DE MOEDAS', 'NUMERO', 'ATUALIZAR', 'APIs', 'Sair']} #opções
		
	print(lg)
	print(ip_res)
	print(f'{vm}-={br}[{az}Data{br}] {dia}/{mes}/{ano} \n{vm}-={br}[{az}Data de entrada{br}] {hora}:{minute} \n{vm}-={br}[{az}Version{br}] 2.0 \n{vm}-={br}[{az}Blog{br}] https://blogzorrosecurity.blogspot.com/')
	print(line)
	for c, item in enumerate(function['consultas']):
		print(f'{br:28}[{az}{c+1}{br}] {item}')
	print(line)
################
def loop():
	try:
		clear()
		menu()
		inpu = input(f'{az}==+> {f}')
		if inpu == '1' or inpu == '01':
			ip()
		elif inpu == '2' or inpu == '02':
			cep()
		elif inpu == '3' or inpu == '03':
			cnpj()
		elif inpu == '4' or inpu == '04':
			cpf()
		elif inpu == '5' or inpu == '05':
			nome()
		elif inpu == '6' or inpu == '06':
			localidades()
		elif inpu == '7' or inpu == '07':
			covid()
		elif inpu == '8' or inpu == '08':
			menuGeradores()
		elif inpu == '9' or inpu == '09':
			ddd()
		elif inpu == '10' or inpu == '10':
			bank()
		elif inpu == '11' or inpu == '11':
			bin()
		elif inpu == '12' or inpu == '12':
			placa()
		elif inpu == '13' or inpu == '13':
			crm()
		elif inpu == '14' or inpu == '14':
			cotacao()
		elif inpu == '15' or inpu == '15':
			numero()
		elif inpu == '16' or inpu == '16':
			clear()
			restart()
			loop()
		elif inpu == '17' or inpu == '17':
			apis()
		elif inpu == '18' or inpu == '18':
			print(f'{vm}Saindo...')
			time.sleep(3)
			exit()
			
		else:
			loop()
	except:
		exit()

try:
	loop()
except:
	exit()
