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


line = cn + '━' * 56



lg = f'''{cn}
 ,,
`""*$b..
     ""*$o.
         "$$o.
           "*$$o.
              "$$$o.
                "$$$$bo...       ..o:
                  "$$$$$$$$booocS$$$    ..    ,.
               ".    "*$$$$SP     V$o..o$$. .$$$b
                "$$o. .$$$$$o. ...A$$$$$$$$$$$$$$b
          ""bo.   "*$$$$$$$$$$$$$$$$$$$$P*$$$$$$$$:
             "$$.    V$$$$$$$$$P"**""*"'   VP  * "l
               "$$$o.4$$$$$$$$X
                "*$$$$$$$$$$$$$AoA$o..oooooo..           .b
                       .X$$$$$$$$$$$P""     ""*oo,,     ,$P
                      $$P""V$$$$$$$:    .        ""*****"
                    .*"    A$$$$$$$$o.4;      .
                         .oP""   "$$$$$$b.  .$;
                                  A$$$$$$$$$$P
                                  "  "$$$$$P"
                                      $$P*"
                                     .$"
                                     "
'''




def clear():
	os.system('clear')

