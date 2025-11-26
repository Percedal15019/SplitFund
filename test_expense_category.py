#!/usr/bin/env python3
import time
import urllib.request
import json

# Wait a bit for Flask to start
time.sleep(2)

try:
    print("=== Testing Add Expense with Category ===\n")
    
    # First, create a group
    print("1. Creating group...")
    url = "http://localhost:5500/group/create"
    payload = json.dumps({"group_id": 101, "members": ["Alice", "Bob", "Charlie"]}).encode()
    req = urllib.request.Request(url, data=payload, method="POST", headers={"Content-Type": "application/json"})
    response = urllib.request.urlopen(req)
    print(f"   ✓ {response.read().decode()}\n")
    
    # Add wallet balance
    print("2. Adding wallet balance...")
    for name in ["Alice", "Bob", "Charlie"]:
        url = "http://localhost:5500/wallet/add"
        payload = json.dumps({"name": name, "group_id": 101, "amount": 500}).encode()
        req = urllib.request.Request(url, data=payload, method="POST", headers={"Content-Type": "application/json"})
        response = urllib.request.urlopen(req)
        print(f"   ✓ {name}: {response.read().decode()}")
    
    print()
    
    # Add expense with category
    print("3. Adding expense with category...")
    url = "http://localhost:5500/expense/split"
    payload = json.dumps({
        "group_id": 101,
        "payer": "Alice",
        "participants": ["Alice", "Bob", "Charlie"],
        "amount": 300,
        "split_type": "equal",
        "category": "food"
    }).encode()
    req = urllib.request.Request(url, data=payload, method="POST", headers={"Content-Type": "application/json"})
    response = urllib.request.urlopen(req)
    result = response.read().decode()
    print(f"   ✓ {result}\n")
    
    # Get detailed summary
    print("4. Getting detailed summary...")
    url = "http://localhost:5500/group/summary/detailed/101"
    response = urllib.request.urlopen(url)
    summary = json.loads(response.read().decode())
    print(f"   ✓ Summary fetched")
    print(f"\n   Details:")
    for user, info in summary.items():
        print(f"\n   User: {user}")
        print(f"     Present balance: {info['present_balance']}")
        print(f"     Total spent: {info['total_spent']}")
        if info['spent_where']:
            print(f"     Spent where:")
            for tx in info['spent_where']:
                print(f"       - Payer: {tx['payer']}, Amount: {tx['deduction']}, Category: {tx.get('category', 'N/A')}")
        if info['paid_for']:
            print(f"     Paid for:")
            for tx in info['paid_for']:
                print(f"       - Total: {tx['total_amount']}, Category: {tx.get('category', 'N/A')}")
    
    print("\n✓ All tests passed!")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
