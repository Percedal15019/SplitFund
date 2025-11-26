import urllib.request, json, sys
BASE='http://127.0.0.1:5500'

print('1) Test name+group_id path:')
payload = {'name':'Alice','group_id':101,'amount':50}
req = urllib.request.Request(BASE+'/wallet/add', data=json.dumps(payload).encode(), headers={'Content-Type':'application/json'})
try:
    resp = urllib.request.urlopen(req, timeout=5)
    print('  OK', resp.read().decode())
except urllib.error.HTTPError as e:
    print('  HTTP', e.code, e.read().decode())
except Exception as e:
    print('  ERR', e)

print('\n2) Test wallet_id path (use first wallet for group 101):')
sys.path.insert(0,'BackEnd')
from models.database import SessionLocal
from models.wallet import Wallet
from models.users import User

db=SessionLocal()
w=db.query(Wallet).filter(Wallet.group_id==101).first()
if w:
    print('  Found wallet id', w.id, 'user_id', w.user_id)
    payload={'wallet_id': w.id, 'amount': 25}
    req = urllib.request.Request(BASE+'/wallet/add', data=json.dumps(payload).encode(), headers={'Content-Type':'application/json'})
    try:
        resp = urllib.request.urlopen(req, timeout=5)
        print('  OK', resp.read().decode())
    except urllib.error.HTTPError as e:
        print('  HTTP', e.code, e.read().decode())
    except Exception as e:
        print('  ERR', e)
else:
    print('  No wallet found for group 101 to test wallet_id path')

print('\nWallets for group 101:')
wallets=db.query(Wallet).filter(Wallet.group_id==101).all()
for w in wallets:
    u=db.query(User).filter(User.id==w.user_id).first()
    print(' ', w.id, u.name, w.balance)
db.close()
