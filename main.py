import os
import time
import requests
from faker import Faker
from data.menu import *


fake = Faker()
by_zorro = f'\n{vm}-={az}[{cn}+{az}] {br}CONSULTA FEITA PELO PROGRAMA Zp4in3l\n{vm}-={az}[{cn}+{az}] {br}by: Zorrinho\n'
IP = {'ipgeolocation': 'https://api.ipgeolocation.io/ipgeo?apiKey=be35b8be10834da8af67daff92154013&ip={}',
      'ip': 'http://ip-api.com/json/{}',
      'ipfind': 'https://api.ipfind.com/?ip={}&auth=f56dbef6-8fd8-4105-af74-a220f9a71610'}
CEP = {'postmon': 'https://api.postmon.com.br/v1/cep/{}',
       'viacep': 'https://viacep.com.br/ws/{}/json/',
       'apicep': 'https://ws.apicep.com/cep/{}.json'}


def ip():
    print(f'{vm}--={f}{az}[{cn}CONSULTA IP{az}]{f}\n')
    for c, item in enumerate(IP.keys()):
        print(f'- {az}[{f}{cn}0{c+1}{az}] {br}{item}')
    n1 = str(input(f'\n {am}=+> '))
    clear()
    for num, api in enumerate(IP.values()):
        if n1 == f'{num+1}' or n1 == f'0{num+1}':
            ip = input(f'{vm}-=={f}{az}[{cn} ip {az}] {am}+=>{f}')
            res = requests.get(api.format(ip)).json()
            print(by_zorro)
            for key, item in res.items():
                print(f'{vm}-= {az}[{cn}{key}{az}] {br}{item}')


def cep():
    print(f'{vm}--={f}{az}[{cn}CONSULTA CEP{az}]{f}')
    for c, item in enumerate(CEP.keys()):
        print(f'- {az}[{f}{cn}0{c+1}{f}{az}] {br}{item}{f}')
    n1 = str(input(f'\n {am}=+> '))
    for num, cep in enumerate(CEP.values):
        if n1 == f'{num+1}' or n1 == f'0{num+1}':
            cep1 = input(f'{vm}-=={f}{az}[{cn} ip {az}] {am}+=> {f}')
            if len(cep1) == 9:
                res = requests.get(cep.format(cep1)).json()
                print(by_zorro)
                for key, value in res.items():
                    print(f'{vm}-={az}[{cn}{key}{az}]{br}{value}')
            else:
                print(f' {vm}[!] valor invalido \n digite apenas numeros \n {f}ex: {vd}01010-010 {f}')


def cnpj():
    print(f'{vm}--=={f}{az}[{cn} fonte RECEITA FEDERAL {az}]')
    cnpj = input(f'{f} \n{vm}--=={f}{az}[ {cn}cpnj{az} ]{f} {am}+=>{f} ')
    res = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}').json()
    print(by_zorro)
    print(by_zorro)
    for key, item in res.items():
        print(f'{vm}-= {az}[{cn}{key}{az}] {br}{item}')


def cpf():
    cpf1 = input(f'{vm}--=={f}{az}[{cn} fonte TRACKEAR {az}]{f} \n{vm}--=={az}[ {cn}cpf{az} ] {am}+=>{f} ')
    url1 = 'http://api.trackear.com.br/basepv/cpf/{}/noip'.format(cpf1)
    res = requests.get(url1).json()
    print(by_zorro)
    for key, item in res.items():
        print(f'{vm}-= {az}[{cn}{key}{az}] {br}{item}')


def numero():
    number = input(f'{vm}--=={f}{az}[{cn} fonte APILAYER {az}]{f} \n{vm}--=={az}[ {cn}number{az} ] {am}+=>{f} ')
    res = requests.get(f'http://apilayer.net/api/validate?access_key=8c830d7095b0888b0b6941b01dac1a1e&number={number}&country_code=BR&format=1').json()
    print(by_zorro)
    for key, item in res.items():
        print(f'{vm}-= {az}[{cn}{key}{az}] {br}{item}')


def localidades():
    loc1 = input(f'{vm}--=={f}{az}[{cn} fonte IBGE {az}]{f} \n{vm}--=={az}[ {cn}estado{az} ] {am}+=>{f} ')
    res = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{loc1}').json()
    print(by_zorro)
    for key, item in res.items():
        print(f'{vm}-= {az}[{cn}{key}{az}] {br}{item}')


def nome():
    api = "http://ghostcenter.xyz/api/nome/"
    usu = input(f'{vm}--=={f}{az}[{cn} fonte GHOSTCENTER {az}]{f} \n{vm}--=={az}[ {cn}nome{az} ] {am}+=>{f} ').split()
    usu = "%20".join(usu)
    req = eval(requests.get(api + usu).text)
    for item in req['dados']:
        for key, value in item.items():
            print(f'{vm}-={az}[{cn}{key}{az}]{br}{value}')
        print(by_zorro)


def covid():
    cov1 = input(f'{vm}--=={f}{az}[{cn} fonte IBGE {az}]{f} \n{vm}--={az}[ {cn}estado - Sigla{az} ] {am}+=>{f} ')
    res = requests.get(f'https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{cov1}').json()
    print(by_zorro)
    for key, item in res.items():
        print(f'{vm}-= {az}[{cn}{key}{az}] {br}{item}')


def mip():
    res = requests.get('https://api.ipify.org')
    print(by_zorro)
    print(f'{vm}-={az}[{cn}IP{az}]{br}{res}')


def linkwpp():
    num = input(f"{vm}--=={f}{az}[{cn} fonte WHATSAPP {az}]{f} \n{vm}--={az}[ {cn}numero{az} ] {am}+=>{f} ")
    msg = str(input(f"{vm}--={az}[ {cn}uma mensagem{az} ] {am}+=>{f}")).split()
    msg = '%20'.join(msg)
    url1 = 'https://api.whatsapp/send?phone=55'
    txt = '&text='
    result = f'{url1}' + num + txt + msg
    print(
        f"\n{vm}-={az}[{cn}+{az}]{br}CONSULTA FEITA PELO PROGRAMA Zp4in3l \n{vm}-={az}[{cn}+{az}]{br}by: Zorrinho \n{vm}-={az}[{cn}LINK{az}]{br}{result}")


def cpfg():
    url = 'https://www.4devs.com.br/ferramentas_online.php'
    res = requests.post(url, {"acao": "gerar_cpf", "pontuacao": "S"}).text
    b2 = f'{br}[{vd}CPF{br}] {res}'
    print(b2)


def cnpjg():
    url = 'https://www.4devs.com.br/ferramentas_online.php'
    res = requests.post(url, {"acao": "gerar_cnpj", "pontuacao": "S"}).text
    b2 = f'{br}[{vd}CNPJ{br}] {res}'
    print(b2)


def contag():
    url = 'https://www.4devs.com.br/ferramentas_online.php'
    res = requests.post(url, {"acao": "gerar_conta_bancaria", "banco": "", "estado": ""}).text
    b6 = f'{br}[{vd}RESULT{br}]\n{res}'
    print(b6)


def nomesg():
    url = 'https://www.4devs.com.br/ferramentas_online.php'
    res = requests.post(url, {"acao": "gerar_nome", "raca": "orc", "sexo": "M"}).text
    b7 = f'{br}[{vd}RESULT{br}]\n{res}'
    print(b7)


def nickg():
    url = 'https://www.4devs.com.br/ferramentas_online.php'
    res = requests.post(url, {"acao": "gerar_nicks", "raca": "orc", "sexo": "M"}).text
    b3 = f'{br}[{vd}RESULT{br}]\n{res}'
    print(b3)


def rgg():
    url = 'https://www.4devs.com.br/ferramentas_online.php'
    res = requests.post(url, {"acao": "gerar_rg", "pontuacao": "S"}).text
    b8 = f'{br}[{vd}RG{br}] {res}'
    print(b8)


while True:
    try:
        opc = menu()
        inpu = input(f'- {am}=+>{f} ')
        if inpu == '1' or inpu == '01':
            clear()
            ip()
        elif inpu == '2' or inpu == '02':
            clear()
            cep()
        elif inpu == '3' or inpu == '03':
            clear()
            cnpj()
        elif inpu == '4' or inpu == '04':
            clear()
            cpf()
        elif inpu == '5' or inpu == '05':
            clear()
            numero()
        elif inpu == '6' or inpu == '06':
            clear()
            localidades()
        elif inpu == '7' or inpu == '07':
            clear()
            nome()
        elif inpu == '8' or inpu == '08':
            clear()
            covid()
        elif inpu == '9' or inpu == '09':
            clear()
            mip()
        elif inpu == '99' or inpu == '99':
            clear()
            time.sleep(6)
            os.system('termux-open-url https://youtube.com/channel/UCTRSuQ_j0qwRKxI9mMioeyg')
        elif inpu == '0' or inpu == '00':
            print(f'{vm}-={az}[{cn}!!{az}] {br}Obrigado por escolher o Zp4in3l :)')
            exit()
        else:
            print(f'{vm}- [!] error! valor invalido !! {f}')
    except KeyboardInterrupt:
        print(f'{vm}Saindo')
        exit()
