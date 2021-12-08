# letras
vm = '\033[1;31m'  # Vermelho
vd = '\033[1;32m'  # Verde
am = '\033[1;33m'  # Amarelo
az = '\033[1;34m'  # Azul
br = '\033[1;37m'  # Branco
cn = '\033[1;36m'  # Ciano
rx = '\033[0;35m'  # Roxo
pt = '\033[1;30m'  # Preto


# fundos
fve = '\033[1;41m'  # Vermelho
fvd = '\033[1;42m'  # Verde
fam = '\033[1;43m'  # Amarelo
faz = '\033[1;44m'  # Azul
fbr = '\033[1;47m'  # Branco
fcy = '\033[1;46m'  # Ciano
frx = '\033[0;45m'  # Roxo


# Padrão
f = '\033[0m'

ascii = f'''{cn}
	           ___====-_  _-====___
            _--^^^#####/./      \.\#####^^^--_
         _-^##########/./ (    ) \.\##########^-_
        -############/./  |\^^/|  \.\############-
      _/############/./   (@::@)   \.\############\_
     /#############(.(     \  /     ).)#############\,
    -###############\.\    (oo)    /./###############-
   -#################\.\  / VV \  /./#################-
  -###################\.\/      \/./###################-
  _#/|##########/\#####(    /\    )#####/\##########|\#_
  |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
  `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
     `   `  `      `   / | |  | | \   '      '  '   '
                      (  | |  | |  )
                     __\ | |  | | /__
                    (vvv(VVV)(VVV)vvv)'''


def clear():
    import os
    os.system("clear")


def menu():
    clear()
    function = {'Consultas': ['ip', 'cep', 'cnpj', 'cpf', 'número', 'localidades', 'nome', 'covid', 'Meu ip'],
                'Gerador': ['CPF', 'CNPJ', 'Conta Bancaria', 'Nome', 'Nick', 'Veiculo', 'RG']}
    print(ascii)
    line = cn + '━' * 56
    print(line)
    for c, key in enumerate(function.keys()):
        print(f'{az:^28}[{cn}0{c+1}{az}] {br}{key:^10}')
    print(line)
    opc = input(f'{am} =+> {vd}').replace('0', '')
    clear()
    print(ascii)
    print(line)
    if opc == '1':
        for c, item in enumerate(function['Consultas']):
            print(f'{az:^28}[{cn}0{c+1}{az}] {br}{item:^10}')
        print(line)
    elif opc == '2':
        for c, item in enumerate(function['Consultas']):
            print(f'{az:^28}[{cn}0{c+1}{az}] {br}{item:^10}')
        print(line)
    else:
        print(f'{vm}Comando não identificado!')
        menu()
    return opc
