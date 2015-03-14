#!/usr/bin/env python3
# usage: python3 HistoricalDataRequest.py <host-ip>
import argparse
import json
import ssl
import sys
import urllib.request
data = {
	"securities": ["IBM US Equity", "AAPL US Equity"],
	"fields": ["PX_LAST", "OPEN", "EPS_ANNUALIZED"]
}

def request_this():
	req = urllib.request.Request('https://http-api.openbloomberg.com/request?ns=blp&service=refdata&type=ReferenceDataRequest')
	req.add_header('Content-Type', 'application/json')
	ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
	ctx.load_verify_locations('b.crt')
	ctx.load_cert_chain('client.crt', 'client.key')
	https_sslv23_handler = urllib.request.HTTPSHandler(context=ctx)
	opener = urllib.request.build_opener(https_sslv23_handler)
	urllib.request.install_opener(opener)
	try:
		res = opener.open(req, data=json.dumps(data).encode("ascii"))
		print(res.read())
	except Exception as e:
		e
		print(e)
		return 1
	return 0
