import httplib2
import json
import urllib
from pprint import pprint
import requests
import urllib2
from urllib2 import HTTPError


####### [ CONFIG ] #######
node = "268891663797772"    # Especifica o Node que sera incluido o Fluxo (openflow:<node>)
qnt = 8000                  # Especifica a quantidade de fluxos a serem inseridos
##########################

data = {
            "table": {
                "id": 0,
                "flow":[]
            }
        }
       
for i in range(qnt):
    data['table']['flow'].insert(i, {
        'id': str(i+1),
        'actions': 'drop',
        'hard_timeout': '1000',
        'idle_timeout': '1000',
        'priority': '10',
        'matches': {
            'ip': None,
            'nw_dst': '10.10.10.250' 
        },
        'n_bytes': '0',
        'n_packets': '0'
    })
    

#url = 'http://admin:admin@localhost:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:' + node + '/table/0'      # Local
url = 'http://admin:admin@10.10.10.202:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:' + node + '/table/0'    # Remoto

headers = {'Authorization': 'Bearer admin:admin', "Content-Type": "application/json"}

#Realiza a chamada
response = requests.put(url, data=json.dumps(data), headers=headers)







"""
	para deletar os fluxos, no terminal colocar o comando:
	curl --noproxy localhost -u admin:admin -X DELETE 'http://localhost:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:268891663797772/table/0'

	ou se nao esta no localhost:
	curl --noproxy 10.10.10.202 -u admin:admin -X DELETE 'http://10.10.10.202:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:268891663797772/table/0'
"""

