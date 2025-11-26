#!/usr/bin/env python3
import time
import urllib.request
import json

# Wait a bit for Flask to start
time.sleep(3)

try:
    print("Testing API endpoints...")
    
    # Test 1: Home endpoint
    url = "http://localhost:5500/"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())
    print(f"✓ GET {url}")
    print(f"  Response: {data}")
    
    # Test 2: Create a group
    url = "http://localhost:5500/group/create"
    payload = json.dumps({"group_id": 1, "members": ["Alice", "Bob", "Charlie"]}).encode()
    req = urllib.request.Request(url, data=payload, method="POST", headers={"Content-Type": "application/json"})
    response = urllib.request.urlopen(req)
    print(f"✓ POST {url}")
    print(f"  Response: {response.read().decode()}")
    
    # Test 3: Get summary
    url = "http://localhost:5500/group/summary/1"
    response = urllib.request.urlopen(url)
    print(f"✓ GET {url}")
    print(f"  Response: {response.read().decode()}")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
