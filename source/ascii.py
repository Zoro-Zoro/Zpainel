import time
import os



# letras
vm = '\033[1;31m' # Vermelho
vd = '\033[1;32m' # Verde
am = '\033[1;33m' # Amarelo
az = '\033[1;34m' # Azul
br = '\033[1;37m' # Branco
cn = '\033[1;36m' # Ciano
rx = '\033[0;35m' # Roxo
pt = '\033[1;30m' # Preto


# Padrão
f = '\033[0m'


line = pt + '━' * 56



lg = f'''{pt}
 _____               _            __
/__  /  ____  ____ _(_)___  ___  / /
  / /  / __ \/ __ `/ / __ \/ _ \/ /
 / /__/ /_/ / /_/ / / / / /  __/ /
/____/ .___/\__,_/_/_/ /_/\___/_/
    /_/
'''




def clear():
	os.system('clear')

