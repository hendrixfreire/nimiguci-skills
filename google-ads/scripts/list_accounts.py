#!/usr/bin/env python3
"""List all Google Ads accounts inside the configured MCC."""

import requests
import json
import os

WORKSPACE = '/root/.openclaw/workspace/projects/google-ads/config'

with open(os.path.join(WORKSPACE, 'google-ads-token.json')) as f:
    token = json.load(f)

with open(os.path.join(WORKSPACE, 'google-ads-config.json')) as f:
    config = json.load(f)

access_token = token['access_token']
dev_token = config['developer_token']
manager_customer_id = str(config.get('customer_id', '')).replace('-', '')

headers = {
    'Authorization': f'Bearer {access_token}',
    'developer-token': dev_token,
    'Content-Type': 'application/json',
    'login-customer-id': manager_customer_id,
}

print('Google Ads Accounts in MCC')
print('=' * 60)
print(f'MCC: {manager_customer_id}')
print()

query_url = f'https://googleads.googleapis.com/v20/customers/{manager_customer_id}/googleAds:searchStream'
query = {
    'query': (
        'SELECT customer_client.id, customer_client.descriptive_name, '
        'customer_client.manager, customer_client.status, customer_client.level '
        'FROM customer_client ORDER BY customer_client.level, customer_client.descriptive_name'
    )
}

resp = requests.post(query_url, headers=headers, json=query)
if resp.status_code != 200:
    print(f'Erro ao listar contas: {resp.status_code}')
    print(resp.text[:1000])
    raise SystemExit(1)

for chunk in resp.json():
    for result in chunk.get('results', []):
        cc = result.get('customerClient', {})
        kind = 'MCC' if cc.get('manager') else 'Conta'
        print(f"{cc.get('id')}: {cc.get('descriptiveName')} | {kind} | {cc.get('status')}")

print()
print('Use --account ID, nome exato, ou parte do nome com query.py')
