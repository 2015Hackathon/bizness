curl -X POST 'https://http-api.openbloomberg.com/request?ns=blp&service=refdata&type=HistoricalDataRequest' \
    --cacert bloomberg.crt \
    --cert   hack_the_burgh_spring_2015_003.crt    \
    --key    hack_the_burgh_spring_2015_003.key    \
    --data @- <<EOF
{ "securities": ["IBM US Equity", "AAPL US Equity"],
  "fields": ["PX_LAST", "OPEN"],
  "startDate": "20120101",
  "endDate": "20120105",
  "periodicitySelection": "DAILY" }
EOF