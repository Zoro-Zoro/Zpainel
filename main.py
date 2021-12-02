br = '\033[1;37m'
vm = '\033[1;31m'
vd = '\033[1;32m'
am = '\033[1;33m'
az = '\033[1;34m'
rx = '\033[1;35m'
cn = '\033[1;36m'
f = '\033[m'


import os
import time
import socket
import requests

def clear():
	os.system("clear")

def ban():
	print(f"""{cn}
	 /﹋\_
	(҂`_´) {br}- {vd}By: Zorro{cn}
	 <;︻╦╤─ ҉ - - - - - - - - - - - - -{vm}
	--=== >> {br}[   {vd}Zp4in3l{br}  ]
	""")
def ip():
	n1 = str(input(f'{vm}--={f}{az}[{cn}CONSULTA IP{az}]{f}\n\n- {az}[{f}{cn}01{f}{az}] {br}ipgeolocation{f}\n- {az}[{f}{cn}02{f}{az}] {br}ip{f}\n- {az}[{f}{cn}03{f}{az}] {br}ipfind{f} \n- {am}+=>{f} '))
	if n1=='1' or n1=='01':
		ip1=input(f'{vm}--=={f}{az}[{cn}fonte IPGEOLOCATION{az}]{f} \n{vm}-=={f}{az}[{cn} ip {az}] {am}+=>{f}')
		url1 = "https://api.ipgeolocation.io/ipgeo?apiKey=be35b8be10834da8af67daff92154013&ip={}".format(ip1)
		res = requests.get(url1);req=res.json()
		b=f"""
		\n{vm}-={az}[{cn}+{az}] {br}CONSULTA FEITA PELO PROGRAMA Zp4in3l\n{vm}-={az}[{cn}+{az}] {br}by: Zorrinho\n{vm}-={az}[{cn}ip{az}] {br}{req["ip"]}\n{vm}-={az}[{cn}country{az}] {br}{req["country_name"]}\n{vm}-={az}[{cn}estado{az}] {br}{req["state_prov"]}\n{vm}-={az}[{cn}city{az}] {br}{req["city"]}\n{vm}-={az}[{cn}latitude{az}] {br}{req["latitude"]}\n{vm}-={az}[{cn}longitude{az}] {br}{req["longitude"]}\n{vm}-={az}[{cn}time zone{az}] {br}{req["time_zone"]}\n{vm}-={az}[{cn}isp{az}] {br}{req["isp"]}\n{vm}-={az}[{cn}currency{az}] {br}{req["currency"]}\n{vm}-={az}[{cn}country flag{az}] {br}{req["country_flag"]}
		"""
		print(b)
		exit()
	elif n1=='2' or n1=='02':
		ip2=input(f'{vm}--=={f}{az}[{cn} fonte IP {az}]{f} \n{vm}--=={f}{az}[{cn} ip {az}]{f} {am}+=>{f} ')
		url2="http://ip-api.com/json/{}".format(ip2)
		res2=requests.get(url2);req1=res2.json()
		b2=f"""
		\n{vm}-={az}[{cn}+{az}] {br}CONSULTA FEITA PELO PROGRAMA Zp4in3l\n{vm}-={az}[{cn}+{az}] {br}by: Zorrinho\n{vm}-={az}[{cn}query{az}]{br}{req1['query']}\n{vm}-={az}[{cn}status{az}]{br}{req1['status']}\n{vm}-={az}[{cn}região{az}]{br}{req1['region']}\n{vm}-={az}[{cn}nome da região{az}]{br}{req1['regionName']}\n{vm}-={az}[{cn}cidade{az}]{br}{req1['city']}\n{vm}-={az}[{cn}cep{az}]{br}{req1['zip']}\n{vm}-={az}[{cn}latitude{az}]{br}{req1['lat']}\n{vm}-={az}[{cn}longitude{az}]{br}{req1['lon']}\n{vm}-={az}[{cn}timezone{az}]{br}{req1['timezone']}\n{vm}-={az}[{cn}isp{az}]{br}{req1['isp']}\n{vm}-={az}[{cn}org{az}]{br}{req1['org']}\n{vm}-={az}[{cn}as{az}]{br}{req1['as']}
		"""
		print(b2)
		exit()
	elif n1=='3' or n1=='03':
		ip3=input(f'{vm}--=={f}{az}[{cn} fonte IPFIND {az}]{f} \n{vm}--=={f}{az}[{cn} ip {az}]{f} {am}+=>{f} ')
		url3="https://api.ipfind.com/?ip={}&auth=f56dbef6-8fd8-4105-af74-a220f9a71610".format(ip3)
		res3=requests.get(url3);req3=res3.json()
		b3=f"""
		\n{vm}-={az}[{cn}+{az}] {br}CONSULTA FEITA PELO PROGRAMA Zp4in3l\n{vm}-={az}[{cn}+{az}] {br}]by: Zorrinho\n{vm}-={az}[{cn}ip_address{az}]{br}{req3["ip_address"]}\n{vm}-={az}[{cn}country{az}]{br}{req3["country"]}\n{vm}-={az}[{cn}countryCode{az}]{br}{req3["country_code"]}\n{vm}-={az}[{cn}continente{az}]{br}{req3["continent"]}\n{vm}-={az}[{cn}continenteCode{az}]{br}{req3["continent_code"]}\n{vm}-={az}[{cn}city{az}]{br}{req3["city"]}\n{vm}-={az}[{cn}county{az}]{br}{req3["county"]}\n{vm}-={az}[{cn}região{az}]{br}{req3["region"]}\n{vm}-={az}[{cn}latitude{az}]{br}{req3["latitude"]}\n{vm}-={az}[{cn}longitude{az}]{br}{req3["longitude"]}
		"""
		print(b3)
		exit()
def cep():
	n1 = str(input(f'{vm}--={f}{az}[{cn}CONSULTA CEP{az}]{f}\n\n- {az}[{f}{cn}01{f}{az}] {br}postmon{f}\n- {az}[{f}{cn}02{f}{az}] {br}viacep{f}\n- {az}[{f}{cn}03{f}{az}] {br}apicep{f} \n- {am}+=>{f} '))
	if n1=='1' or n1=='01':
		cep1=input(f'{vm}--=={f}{az}[{cn}fonte POSTMON{az}]{f} \n{vm}-=={f}{az}[{cn} ip {az}] {am}+=>{f}')
		if len(cep1) == 9:
			url1='https://api.postmon.com.br/v1/cep/{}'.format(cep1)
			res1=requests.get(url1);req1=res1.json()
			resl1=f'\n{vm}-={az}[{cn}+{az}]{br}CONSULTA FEITA PELO PROGRAMA Zp4in3l\n{vm}-={az}[{cn}+{az}]{br}by: Zorrinho\n{vm}-={az}[{cn}bairro{az}]{br}{req1["bairro"]}o\n{vm}-={az}[{cn}cidade{az}]{br}{req1["cidade"]}o\n{vm}-={az}[{cn}logradouro{az}]{br}{req1["logradouro"]}o\n{vm}-={az}[{cn}Informações de estado{az}]{br}{req1["estado_info"]}o\n{vm}-={az}[{cn}cep{az}]{br}{req1["cep"]}o\n{vm}-={az}[{cn}Informações de cidade{az}]{br}{req1["cidade_info"]}'
			print(resl1)
			exit()
		else:
			print(f' {vm}[!] valor invalido \n digite apenas numeros \n {f}ex: {ng}01010-010 {f}')
	elif n1=='2' or n1=='02':
		cep2=input(f'{vm}--=={f}{az}[{cn}fonte VIACEP{az}]{f} \n{vm}-=={f}{az}[{cn} ip {az}] {am}+=>{f}')
		if len(cep2) == 9:
			url2='https://viacep.com.br/ws/{}/json/'.format(cep2)
			res2=requests.get(url2);req2=res2.json()
			resl2=f'\n{vm}-={az}[{cn}+{az}]{br}CONSULTA FEITA PELO PROGRAMA Zp4in3l\n{vm}-={az}[{cn}+{az}]{br}by: Zorrinho\n{vm}-={az}[{cn}bairro{az}]{br}{req2["bairro"]}\n{vm}-={az}[{cn}logradouro{az}]{br}{req2["logradouro"]}\n{vm}-={az}[{cn}cep{az}]{br}{req2["cep"]}\n{vm}-={az}[{cn}complemento{az}]{req2["complemento"]}\n{vm}-={az}[{cn}uf{az}]{br}{req2["uf"]}\n{vm}-={az}[{cn}ibge{az}]{br}{req2["ibge"]}\n{vm}-={az}[{cn}gia{az}]{br}{req2["gia"]}\n{vm}-={az}[{cn}ddd{az}]{br}{req2["ddd"]}\n{vm}-={az}[{cn}siafi{az}]{br}{req2["siafi"]}'
			print(resl2)
			exit()
		else:
			print(f' {vm}[!] valor invalido \n digite apenas numeros \n {f}ex: {ng}01001000 {f}')
	elif n1=='3' or n1=='03':
		cep3=input(f'{vm}--=={f}{az}[{cn}fonte APICEP{az}]{f} \n{vm}-=={f}{az}[{cn} ip {az}] {am}+=>{f}')
		if len(cep3) == 9:
			url3='https://ws.apicep.com/cep/{}.json'.format(cep3)
			res3=requests.get(url3);req3=res3.json()
			resl3=f'\n{vm}-={az}[{cn}+{az}]{br}CONSULTA FEITA PELO PROGRAMA Zp4in3l\n{vm}-={az}[{cn}+{az}]{br}by: Zorrinho\n{vm}-={az}[{cn}status{az}]{br}{req3["status"]}\n{vm}-={az}[{cn}ok{az}]{br}{req3["ok"]}\n{vm}-={az}[{cn}cep{az}]{br}{req3["code"]}\n{vm}-={az}[{cn}state{az}]{br}{req3["state"]}\n{vm}-={az}[{cn}city{az}]{br}{req3["city"]}\n{vm}-={az}[{cn}distrito{az}]{br}{req3["district"]}\n{vm}-={az}[{cn}rua{az}]{br}{req3["address"]}\n{vm}-={az}[{cn}statusText{az}]{br}{req3["statusText"]}'
			print(resl3)
			exit()
def cnpj():
	cpnj1=input(f'{vm}--=={f}{az}[{cn} fonte RECEITA FEDERAL {az}]{f} \n{vm}--=={f}{az}[ {cn}cpnj{az} ]{f} {am}+=>{f} ')                           
	url1='https://www.receitaws.com.br/v1/cnpj/{}'.format(cpnj1)
	res=requests.get(url1);req1=res.json()
	br1=f'\n{vm}-={az}[{cn}+{az}]{br}CONSULTA FEITA PELO PROGRAMA Zp4in3l\n{vm}-={az}[{cn}+{az}]{br}by: Zorrinho\n{vm}-={az}[{cn}Data Situacao{az}]{br}{req1["data_situacao"]}\n{vm}-={az}[{cn}motivo_situacao{az}]{br}{req1["motivo_situacao"]}\n{vm}-={az}[{cn}tipo{az}]{br}{req1["tipo"]}\n{vm}-={az}[{cn}complemento{az}]{br}{req1["complemento"]}\n{vm}-={az}[{cn}nome{az}]{br}{req1["nome"]}\n{vm}-={az}[{cn}telefone{az}]{br}{req1["telefone"]}\n{vm}-={az}[{cn}status{az}]{br}{req1["status"]}\n{vm}-={az}[{cn}email{az}]{br}{req1["email"]}\n{vm}-={az}[{cn}data Situacao especial{az}]{br}{req1["data_situacao_especial"]}\n{vm}-={az}[{cn}atividade_pricipal{az}]{br}{req1["atividade_principal"]}\n{vm}-={az}[{cn}tipo{az}]{br}{req1["atividades_secundarias"]}'
	print(br1)
	#00000000000191
def cpf():
	cpf1=input(f'{vm}--=={f}{az}[{cn} fonte TRACKEAR {az}]{f} \n{vm}--=={az}[ {cn}cpf{az} ] {am}+=>{f} ')
	url1='http://api.trackear.com.br/basepv/cpf/{}/noip'.format(cpf1)
	res=requests.get(url1);req1=res.json()
	br2=f'\n{vm}-={az}[{cn}+{az}]{br}CONSULTA FEITA PELO PROGRAMA Zp4in3l\n{vm}-={az}[{cn}+{az}]{br}by: Zorrinho\n{vm}-={az}[{cn}cpf{az}]{br}{req1["cpf"]}\n{vm}-={az}[{cn}sexo{az}]{br}{req1["sexo"]}\n{vm}-={az}[{cn}nascimento{az}]{br}{req1["dtNascimento"]}\n{vm}-={az}[{cn}idade{az}]{br}{req1["idade"]}\n{vm}-={az}[{cn}nome{az}]{br}{req1["nome"]}\n{vm}-={az}[{cn}delay{az}]{br}{req1["delay"]}\n{vm}-={az}[{cn}code{az}]{br}{req1["code"]}'
	print(br2)
def numero():
	number=input(f'{vm}--=={f}{az}[{cn} fonte APILAYER {az}]{f} \n{vm}--=={az}[ {cn}number{az} ] {am}+=>{f} ')
	url1='http://apilayer.net/api/validate?access_key=8c830d7095b0888b0b6941b01dac1a1e&number={}&country_code=BR&format=1'.format(number)
	res=requests.get(url1);req1=res.json()
	br2=f'\n{vm}-={az}[{cn}+{az}]{br}CONSULTA FEITA PELO PROGRAMA Zp4in3l\n{vm}-={az}[{cn}+{az}]{br}by: Zorrinho\n{vm}-={az}[{cn}valid{az}]{br}{req1["valid"]}\n{vm}-={az}[{cn}formato local{az}]{br}{req1["local_format"]}\n{vm}-={az}[{cn}country prefix{az}]{br}{req1["country_prefix"]}\n{vm}-={az}[{cn}country code{az}]{br}{req1["country_code"]}\n{vm}-={az}[{cn}country name{az}]{br}{req1["country_name"]}\n{vm}-={az}[{cn}location{az}]{br}{req1["location"]}\n{vm}-={az}[{cn}line type{az}]{br}{req1["line_type"]}'
	print(br2)
def localidades():
	loc1=input(f'{vm}--=={f}{az}[{cn} fonte IBGE {az}]{f} \n{vm}--=={az}[ {cn}estado{az} ] {am}+=>{f} ')
	url1='https://servicodados.ibge.gov.br/api/v1/localidades/estados/{}'.format(loc1)
	res=requests.get(url1);req1=res.json()
	br2=f'\n{vm}-={az}[{cn}+{az}]{br}CONSULTA FEITA PELO PROGRAMA Zp4in3l\n{vm}-={az}[{cn}+{az}]{br}by: Zorrinho\n{vm}-={az}[{cn}id{az}]{br}{req1["id"]}\n{vm}-={az}[{cn}estado{az}]{br}{req1["sigla"]}\n{vm}-={az}[{cn}nome{az}]{br}{req1["nome"]}\n{vm}-={az}[{cn}região{az}]{br}{req1["regiao"]}'
	print(br2)
def menu():
	print(f"""{cn}
	 /﹋\_
	(҂`_´) {br}- {vd}By: Zorro{cn}
	 <;︻╦╤─ ҉ - - - - - - - - - - - - -{vm}
	--=== >> {br}[   {vd}Zp4in3l{br}  ]
	{br}- {az}[{cn}01{az}] {br}ip         {br}-
	{br}- {az}[{cn}02{az}] {br}cep        {br}-
	{br}- {az}[{cn}03{az}] {br}cnpj       {br}-
	{br}- {az}[{cn}04{az}] {br}cpf        {br}-
	{br}- {az}[{cn}05{az}] {br}numero     {br}-
	{br}- {az}[{cn}06{az}] {br}localidade {br}-
	""")
try:
	menu()
	inpu=input(f'- {am}=+>{f} ')
except KeyboardInterrupt:
	exit()
except:
	print(f'{vm}- [!] error! valor invalido !! {f}')
try:
	if inpu=='1' or inpu=='01':
		clear();ban();ip()
	elif inpu=='2' or inpu=='02':
		clear();ban();cep()
	elif inpu=='3' or inpu=='03':
		clear();ban();cnpj()
	elif inpu=='4' or inpu=='04':
		clear();ban();cpf()
	elif inpu=='5' or inpu=='05':
		clear();ban();numero()
	elif inpu=='6' or inpu=='06':
		clear();ban();localidades()
	elif inpu=='0' or inpu=='00':
		exit()
	else:
		print(f'{vm}- [!] error! valor invalido !! {f}')
except:
	exit()