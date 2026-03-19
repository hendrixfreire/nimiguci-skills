#!/usr/bin/env python3
import requests
import json
import os

WORKSPACE = '/root/.openclaw/workspace/projects/google-ads/config'

def brazilian_format(value, is_currency=False):
    """Format number in Brazilian style: 1.234,56"""
    if isinstance(value, float):
        formatted = f"{value:,.2f}"
        formatted = formatted.replace(',', 'X').replace('.', ',').replace('X', '.')
        if is_currency:
            return f"R$ {formatted}"
        return formatted
    elif isinstance(value, int):
        formatted = f"{value:,}"
        return formatted.replace(',', '.')
    return str(value)

with open(os.path.join(WORKSPACE, 'google-ads-token.json')) as f:
    token = json.load(f)

with open(os.path.join(WORKSPACE, 'google-ads-config.json')) as f:
    config = json.load(f)

access_token = token['access_token']
dev_token = config['developer_token']
customer_id = '5150697270'

headers = {
    'Authorization': f'Bearer {access_token}',
    'developer-token': dev_token,
    'Content-Type': 'application/json'
}

query_url = f'https://googleads.googleapis.com/v20/customers/{customer_id}/googleAds:searchStream'

print('Unico Skill - Campanhas')
print('=' * 50)

query = {'query': '''
    SELECT 
        campaign.id,
        campaign.name,
        campaign.status,
        metrics.cost_micros,
        metrics.impressions,
        metrics.clicks
    FROM campaign
    WHERE segments.date DURING LAST_30_DAYS
'''}

resp = requests.post(query_url, headers=headers, json=query)

if resp.status_code == 200:
    data = json.loads(resp.text)
    
    campaigns = []
    total_cost = 0
    total_impressions = 0
    total_clicks = 0
    
    for chunk in data:
        for result in chunk.get('results', []):
            c = result.get('campaign', {})
            m = result.get('metrics', {})
            cost = float(m.get('costMicros', 0)) / 1_000_000
            impressions = int(m.get('impressions', 0))
            clicks = int(m.get('clicks', 0))
            
            if cost > 0 or impressions > 0 or clicks > 0:
                campaigns.append({
                    'name': c.get('name'),
                    'status': c.get('status'),
                    'impressions': impressions,
                    'clicks': clicks,
                    'cost': cost
                })
                total_cost += cost
                total_impressions += impressions
                total_clicks += clicks
    
    if campaigns:
        for c in campaigns:
            status_icon = '●' if c['status'] == 'ENABLED' else '○'
            print(f"{status_icon} {c['name']}")
            print(f"   Gasto: {brazilian_format(c['cost'], is_currency=True)}")
            print(f"   Impressões: {brazilian_format(c['impressions'])}")
            print(f"   Cliques: {brazilian_format(c['clicks'])}")
            print()
        
        print('-' * 50)
        print(f"Total - Gasto: {brazilian_format(total_cost, is_currency=True)}")
        print(f"Total - Impressões: {brazilian_format(total_impressions)}")
        print(f"Total - Cliques: {brazilian_format(total_clicks)}")
    else:
        print('Nenhuma campanha com atividade nos últimos 30 dias.')
else:
    print(f'Erro: {resp.status_code}')
