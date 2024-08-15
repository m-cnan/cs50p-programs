# importing required libraries
import requests
import sys

if len(sys.argv)==2:
    try:
        response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        total=float(response["bpi"]["USD"]["rate_float"])*float(sys.argv[1])
        print(f"${total:,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")
    