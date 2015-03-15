from current_data_dynamic import request_this
import ast
import json

bloomberg_json = request_this(["AAPL US Equity"],["PX_LAST"])
bloomberg_dict = ast.literal_eval(bloomberg_json)
#bloomberg_info = bloomberg_json["data"][0]["securityData"]["fieldData"]["PX_LAST"]

print(bloomberg_dict["data"][0]["securityData"][0]["fieldData"]["PX_LAST"])