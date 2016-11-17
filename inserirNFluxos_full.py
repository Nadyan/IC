import httplib2
import json
import urllib
from pprint import pprint
import requests
import urllib2
from urllib2 import HTTPError


####### [ CONFIG ] ########
node = "268891663797772"  # Especifica o Node que sera incluido o Fluxo (openflow:<node>)
qntFluxos = 8000          # Especifica a quantidade de fluxos a serem inseridos
qntTabelas = 2            # Especifica a quantidade de tabelas a serem preenchidas
###########################

data = {
            "table": {
                "id": 0,
                "flow":[]
            }
        }
       
for i in range(qnt):
    # Caracteristicas do fluxo
    # O fluxo possui campos preenchidos com dados aleatorios
    # Com o objetivo de ocupar os campos da tabela

    data['table']['flow'].insert(i, {
        'id': str(i+1),
        'actions': ['OUTPUT=1'],
        'hard_timeout': '1000',
        'idle_timeout': '1000',
        'priority': '10',
        'nwSrc': '10.10.10.202', # IP de origem
        'nwDst': '10.10.10.250', # IP de destino
        'n_bytes': '5',
        'n_packets': '10',
        'protocol': 'tcp'
    })



### Para adicionar em n tabelas 
### !! Se usar, comente tudo o que tiver abaixo do for, else, comente o for !!
#for i in range(qtdTables):
#    url = 'http://admin:admin@10.10.10.202:8181/restconf/config/opendaylight-inventory:nodes/node/openflow' + node + '/table/' + i
#    headers = {'Authorization': 'Bearer admin:admin', "Content-Type": "application/json"}    
#    response = requests.put(url, data=json.dumps(data), headers=headers)


# Endereco local
#url = 'http://admin:admin@localhost:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:' + node + '/table/0'

# Endereco Remoto
url = 'http://admin:admin@10.10.10.202:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:' + node + '/table/0'


headers = {'Authorization': 'Bearer admin:admin', "Content-Type": "application/json"}

#Realiza a chamada
response = requests.put(url, data=json.dumps(data), headers=headers)







"""
	para deletar os fluxos, no terminal colocar o comando:
	curl --noproxy localhost -u admin:admin -X DELETE 'http://localhost:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:268891663797772/table/0'

	ou se nao esta no localhost:
	curl --noproxy <IPcontroller> -u admin:admin -X DELETE 'http://<IPcontroller>:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:268891663797772/table/0'
"""

