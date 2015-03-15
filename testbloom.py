# from current_data_dynamic import request_this
# import ast
# import json

# bloomberg_json = request_this(["AAPL US Equity"],["PX_LAST"])
# bloomberg_dict = ast.literal_eval(bloomberg_json)
# #bloomberg_info = bloomberg_json["data"][0]["securityData"]["fieldData"]["PX_LAST"]

# print(bloomberg_dict["data"][0]["securityData"][0]["fieldData"]["PX_LAST"])

import csv

def get_ab_in_csv(inputC, filename):
	f = open(filename, newline = '')
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		if inputC == row[0] or inputC == row[1]:
			return row[0]
	return 0

def get_ab(inputC):
	if (0 != get_ab_in_csv(inputC, 'c1.csv')):
		return get_ab_in_csv(inputC, 'c1.csv')
	else:
		return get_ab_in_csv(inputC, 'c2.csv')