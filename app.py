from datetime import datetime
import sys
from elasticsearch import Elasticsearch
es = Elasticsearch([sys.argv[1]])
print(es.info())

from docker import Client
cli = Client(base_url='unix://var/run/docker.sock')
print (cli.info())