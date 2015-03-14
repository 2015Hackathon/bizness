import requests

certificate = ('client.crt', 'client.key')

url = 'https://http-api.openbloomberg.com/'

parameters = dict (
	ns = blp
	service = refdata
	type = HistoricalDataRequest
)

r = requests.get(url = url, cert = certificate, params = parameters)