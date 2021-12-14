import os
from sys import executable


try:
	import keyboard, requests
except:
	os.system(executable+' -m pip install requests phonenumbers keyboard faker')
import time
import requests
from faker import Faker
import base64
import datetime
from source.ascii import *
from source.apis import *
from source.geradores import *


##########################
r = requests.get('https://ip-api.org/json').json()
ip_res = f'{vm}-={br}[{az}Seu IP{br}]{r["ip"]}'
##########################


time = datetime.datetime
date = datetime.date
hora = time.today().hour
minute = time.today().minute
dia = date.today().day
mes = date.today().month
ano = date.today().year


by_zorro = f'\n{vm}-={az}[{cn}+{az}] {br}CONSULTA FEITA PELO PROGRAMA Zp4in3l\n{vm}-={az}[{cn}+{az}] {br}by: Zorrinho\n'

IP = {'ipgeolocation': 'https://api.ipgeolocation.io/ipgeo?apiKey=be35b8be10834da8af67daff92154013&ip={}',
	'ip': 'http://ip-api.com/json/{}',
	'ipfind': 'https://api.ipfind.com/?ip={}&auth=f56dbef6-8fd8-4105-af74-a220f9a71610'}
CEP = {'postmon': 'https://api.postmon.com.br/v1/cep/{}',
	'viacep': 'https://viacep.com.br/ws/{}/json/',
	'apicep': 'https://ws.apicep.com/cep/{}.json'}


#################################################
def ent():
	print('')
	back = input(f' {br}<{vd}ENTER PARA VOLTAR{br}> ').replace('0', '')
	if back == '1' or '01':
		clear()
		loop()
	elif back == '2' or '02':
		exit()


def restart():
	os.system(executable+'cd && rm -fr Zpainel && git clone https://github.com/Zoro-Zoro/Zpainel')
#################################################

def ip():
	print(f'{vm}--={f}{az}[{cn}CONSULTA IP{az}]{f}\n')
	for c, item in enumerate(IP.keys()):
		print(f'- {az}[{f}{cn}{c+1}{az}] {br}{item}')
	n1 = str(input(f'\n {am}=+> '))
	clear()
	for num, api in enumerate(IP.values()):
		if n1 == f'{num+1}' or n1 == f'0{num+1}':
			ip = input(f'{vm}-=={f}{az}[{cn} ip {az}] {am}+=>{f}')
			res = requests.get(api.format(ip)).json()
			print(by_zorro)
			for key, item in res.items():
				print(f'{vm}-= {az}[{cn}{key}{az}] {br}{item}')
			ent()


def cep():
	print(f'{vm}--={f}{az}[{cn}CONSULTA CEP{az}]{f}')
	for c, item in enumerate(CEP.keys()):
		print(f'- {az}[{f}{cn}{c+1}{f}{az}] {br}{item}{f}')
	n1 = str(input(f'\n {am}=+> {f}'))
	for num, cep in enumerate(CEP.values()):
		if n1 == f'{num+1}' or n1 == f'0{num+1}':
			cep1 = input(f'{vm}-=={f}{az}[{cn} ip {az}] {am}+=> {f}')
			if len(cep1) == 9:
				res = requests.get(cep.format(cep1)).json()
				print(by_zorro)
				for key, value in res.items():
					print(f'{vm}-={az}[{cn}{key}{az}]{br}{value}')
				ent()
			else:
				print(f' {vm}[!] valor invalido \n digite apenas numeros \n {f}ex: {vd}01010-010 {f}')



def cnpj():
	cpnj1=input(f'{vm}--=={f}{az}[{cn} fonte RECEITA FEDERAL {az}]{f} \n{vm}--=={f}{az}[ {cn}cpnj{az} ]{f} {am}+=>{f} ')                           
	req=requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cpnj1)).json()
	print(by_zorro)
	for key, value in req.items():
		print(f'{vm}-={br}[{vd}{key}{br}]{value}')
	ent()


def cpf():
	cpf1=input(f'{vm}--=={f}{az}[{cn} fonte TRACKEAR {az}]{f} \n{vm}--=={az}[ {cn}cpf{az} ] {am}+=>{f} ')
	req=requests.get('http://api.trackear.com.br/basepv/cpf/{}/noip'.format(cpf1)).json()
	print(by_zorro)
	for key, value in req.items():
		print(f'{vm}-={br}[{vd}{key}{br}]{value}')
	ent()


def numero():
	# a mesma api com outra key: http://apilayer.net/api/validate?access_key=f134484ed14981a957368f2a06aaa251&number={}&country_code=&format=1
	#token de asseço f134484ed14981a957368f2a06aaa251
	# conta: https://numverify.com/dashboard
	number=input(f'{vm}--=={f}{az}[{cn} fonte NUMERY {az}]{f} \n{vm}--=={az}[ {cn}number{az} ] {am}+=>{f} ')
	req=requests.get('http://apilayer.net/api/validate?access_key=8c830d7095b0888b0b6941b01dac1a1e&number={}&country_code=BR&format=1'.format(number)).json()
	print(by_zorro)
	for key, value in req.items():
		print(f'{vm}-={br}[{vd}{key}{br}]{value}')
	ent()


def localidades():
	loc1=input(f'{vm}--=={f}{az}[{cn} fonte IBGE {az}]{f} \n{vm}--=={az}[ {cn}estado{az} ] {am}+=>{f} ')
	req=requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/{}'.format(loc1)).json()
	print(by_zorro)
	for key, value in req.items():
		print(f'{vm}-={br}[{vd}{key}{br}] {value}')
	ent()


def nome():
	api = "http://ghostcenter.xyz/api/nome/"
	usu = input(f'{vm}--=={f}{az}[{cn} fonte GHOSTCENTER {az}]{f} \n{vm}--=={az}[ {cn}nome{az} ] {am}+=>{f} ').split()
	usu = "%20".join(usu)
	req = eval(requests.get(api+usu).text)
	for item in req['dados']:
		for key, value in item.items():
			print(f'{vm}-={br}[{az}{key}{br}]{br}{value}')
		print(by_zorro)
		ent()


def covid():
	cov1=input(f'{vm}--=={f}{az}[{cn} fonte IBGE {az}]{f} \n{vm}--={az}[ {cn}estado - Sigla{az} ] {am}+=>{f} ')
	req=requests.get('https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{}'.format(cov1)).json()
	print(by_zorro)
	for key, value in req.items():
		print(f'{vm}-={br}[{az}key{br}]{br}{value}')
	ent()
	


def ddd():
	ddd = input(f'{vm}-=={br}[ {az}fonte VIADDD{br} ] \n{vm}-={br}[ {az}ddd{br} ] {vd}=+> {f}')
	req = requests.get('https://viaddd.com.br/api/ddd/{}'.format(ddd)).json()
	print(by_zorro)
	for key, value in req.items():
		print(f'{vm}-={br}[{az}{key}{br}] {value}')
	ent()


def bank():
	bank = input(f'{vm}-={br}[ {az}fonte BRASILAPI{br} ] \n{vm}-={br}[ {az}banco{br} ] {vd}=+> {f}')
	req=requests.get('https://brasilapi.com.br/api/banks/v1/{}'.format(bank)).json()
	print(by_zorro)
	for key, value in req.items():
		print(f'{vm}-={br}[{az}{key}{br}] {value}')
	ent()


def bin():
	bin = input(f'{vm}-=={br}[ {az}fonte BINLIST{br} ] \n{vm}-={br}[ {az}bin{br} ] {vd}=+> {f}')
	req=requests.get(f'https://lookup.binlist.net/{bin}').json()
	for key, value in req.items():
		print(f'{vm}-={br}[{az}{key}{br}] {value}')
	ent()


def placa():
	placa = input(f'{vm}-={br}[ {vd}fonte APICARROS{br} ] \n{vm}-={br}[ {vd}placa{br} ] {vd}=+> {f}')
	url=requests.get('https://apicarros.com/v1/consulta/{}/json'.format(placa), verify = False).json() # JSQ7436
	clear()
	print(lg)
	if (url['codigoRetorno']) == '0':	
		for key, value in url.items():
			print(f'{vm}-={br}[{az}{key}{br}] {value}')
	ent()


def crm():
	crm = input(f'{vm}-=={br}[{vd} fonte CONSULTACRM {br}] \n{vm}-=={br}[{vd} crm {br}] {vd}=+> {f}')
	uf_crm = input(f'{vm}-={br}[{vd} uf {br}] {vd}=+> {f}')
	url = requests.get('https://www.consultacrm.com.br/api/index.php?tipo=crm&uf={}&q={}&chave=4188146193&destino=json'.format(uf_crm, crm)).json() # 814830 rj
	for key, value in url.items():
		print(f'{vm}-={br}[{az}{key}{br}] {value}')
	ent()


def apis():
	apis = {'zapis': ['https://www.consultacrm.com.br/api/', 'https://apicarros.com/v1/consulta/', 'https://brasilapi.com.br/api/banks/v1/', 'https://lookup.binlist.net/', 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/', 'http://ghostcenter.xyz/api/nome/', 'https://viaddd.com.br/api/ddd/', 'http://apilayer.net/api/', 'http://api.trackear.com.br/basepv/cpf/', 'https://www.receitaws.com.br/v1/cnpj/']}
	
	print(line)
	for c, item in enumerate(apis['zapis']):
		print(f'{br}[{az}API 0{c+1}{br}] {item}')
	ent()


def cotacao():
	req = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL').json()
	req_usd = req['USDBRL']
	req_eur = req['EURBRL']
	req_btc = req['BTCBRL']
	print(f'{vm}-={br}[{vd}cotação do DOLAR!{br}]')
	for key, value in req_usd.items():
		print(f'{vm}-={br}[{az}{key}{br}] {value}')
	print(line)
	print(f'{vm}-={br}[{vd}cotação do EURO!{br}]')
	for key, value in req_eur.items():
		print(f'{vm}-={br}[{az}{key}{br}] {value}')
	print(line)
	print(f'{vm}-={br}[{vd}cotação do BITCOIN!{br}]')
	for key, value in req_btc.items():
		print(f'{vm}-={br}[{az}{key}{br}] {value}')
	ent()


def menu():
	clear()
	function = {'consultas': ['IP', 'CEP', 'CNPJ', 'CPF', 'NOME', 'LOCALIDADES', 'COVID', 'GERADORES', 'DDD', 'BANCO', 'BIN', 'PLACA', 'CRM', 'COTAÇÃO DE MOEDAS', 'NUMERO', 'ATUALIZAE', 'APIs', 'Sair']}
		
	print(lg)
	print(ip_res)
	print(f'{vm}-={br}[{az}Data{br}] {dia}/{mes}/{ano} \n{vm}-={br}[{az}Data de entrada{br}] {hora}:{minute}')
	print(line)
	for c, item in enumerate(function['consultas']):
		print(f'{vm}-={br}[{az}{c+1}{br}] {item}')
	print(line)


def loop():
	try:
		menu()
		inpu = input(f'{vd}=+> {f}')
		if inpu == '1' or inpu == '01':
			clear()
			print(lg)
			ip()
		elif inpu == '2' or inpu == '02':
			clear()
			print(lg)
			cep()
		elif inpu == '3' or inpu == '03':
			clear()
			print(lg)
			cnpj()
		elif inpu == '4' or inpu == '04':
			clear()
			print(lg)
			cpf()
		elif inpu == '5' or inpu == '05':
			clear()
			print(lg)
			nome()
		elif inpu == '6' or inpu == '06':
			clear()
			print(lg)
			localidades()
		elif inpu == '7' or inpu == '07':
			clear()
			print(lg)
			covid()
		elif inpu == '8' or inpu == '08':
			clear()
			print(lg)
			menuGeradores()
		elif inpu == '9' or inpu == '09':
			clear()
			print(lg)
			ddd()
		elif inpu == '10' or inpu == '10':
			clear()
			print(lg)
			bank()
		elif inpu == '11' or inpu == '11':
			clear()
			print(lg)
			bin()
		elif inpu == '12' or inpu == '12':
			clear()
			print(lg)
			placa()
		elif inpu == '13' or inpu == '13':
			clear()
			print(lg)
			crm()
		elif inpu == '14' or inpu == '14':
			clear()
			print(lg)
			cotacao()
		elif inpu == '15' or inpu == '15':
			clear()
			print(lg)
			numero()
		elif inpu == '16' or inpu == '16':
			clear()
			restart()
			loop()
		elif inpu == '17' or inpu == '17':
			clear()
			print(lg)
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


#o programa nao pode estar muito limpo, mas quando atualizarmos novamente nos vamos deixar o codigo mais limpo.