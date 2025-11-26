import urllib.request, json
url='http://localhost:5500/wallet/add'
payload=json.dumps({'name':'Alice','group_id':101,'amount':100}).encode()
req=urllib.request.Request(url,data=payload,headers={'Content-Type':'application/json'})
try:
    resp=urllib.request.urlopen(req)
    print('OK', resp.read().decode())
except urllib.error.HTTPError as e:
    body=e.read().decode()
    print('HTTPError', e.code, body)
except Exception as e:
    print('Error', e)
