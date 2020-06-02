import datetime as dt
from pytz import timezone

# Registrar de inicio do script
inicio_script = dt.datetime.now().astimezone(timezone('America/Sao_Paulo'))

# Registrar log de inicio
fim_script = dt.datetime.now().astimezone(timezone('America/Sao_Paulo'))

## Grava o log de inicio e termino em um txt ##
formato = '%Y-%m-%d %H:%M:%S'

texto_inicio = 'Script iniciou: '+str(inicio_script.strftime(formato))+'\n'
texto_fim = 'Script finalizou: '+str(fim_script.strftime(formato))+'\n'
total = 'Tempo de execucao: '+str(fim_script - inicio_script)+'\n'+str('-'*50)+'\n'

arq = open('./log_Avaliacoes.txt', 'a')
arq.write(texto_inicio+texto_fim+total)
arq.close()