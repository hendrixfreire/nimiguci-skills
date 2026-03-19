#!/usr/bin/env python3
"""
Google Ads Query Tool - Brazilian Format Edition
Execute custom GAQL queries against Google Ads API with Brazilian number formatting.

Usage:
    python3 query.py "SELECT campaign.name, metrics.cost_micros FROM campaign"
    python3 query.py --account 5150697270 "SELECT metrics.impressions FROM campaign"
    python3 query.py --account "Iguatemi 365" "SELECT metrics.cost_micros FROM campaign"
    python3 query.py --account anh "SELECT metrics.clicks FROM campaign"
"""

import json
import requests
import sys
import os
import re
from datetime import datetime, timezone, timedelta

WORKSPACE = '/root/.openclaw/workspace/projects/google-ads/config'

ACCOUNT_ALIASES = {
    'allset': '1329326896',
    'mcc': '1329326896',
    'manager': '1329326896',
    'anh': '2936758199',
    'probeef': '2936758199',
    'nutron': '2936758199',
    'extra': '7076922734',
    'extrapower': '7076922734',
    'flying': '1310225479',
    'horse': '1310225479',
    'flyinghorse': '1310225479',
    'cargill': '6811989892',
    'fundacao': '6811989892',
    'fundaçãocargill': '6811989892',
    'fundacaocargill': '6811989892',
    'iguatemi': '9236797141',
    'iguatemi-performance': '9236797141',
    'performance': '9236797141',
    'iguatemi365': '1523987447',
    '365': '1523987447',
    'nbc': '4341174946',
    'universal': '4341174946',
    'nbcuniversal': '4341174946',
}

def brazilian_format(value, is_currency=False):
    """Format number in Brazilian style: 1.234,56"""
    if isinstance(value, float):
        # Format with comma as decimal separator
        formatted = f"{value:,.2f}"
        # Replace comma with temporary, then dot with comma, then temp with dot
        formatted = formatted.replace(',', 'X').replace('.', ',').replace('X', '.')
        if is_currency:
            return f"R$ {formatted}"
        return formatted
    elif isinstance(value, int):
        formatted = f"{value:,}"
        return formatted.replace(',', '.')
    return str(value)

def parse_currency_from_micros(micros):
    """Convert micros to reais and format Brazilian style."""
    reais = float(micros) / 1_000_000
    return brazilian_format(reais, is_currency=True)

def load_json(path):
    with open(path) as f:
        return json.load(f)


def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def refresh_access_token(token):
    auth = load_json(os.path.join(WORKSPACE, 'google-ads-auth.json'))
    installed = auth.get('installed', {})

    resp = requests.post(
        'https://oauth2.googleapis.com/token',
        data={
            'client_id': installed.get('client_id'),
            'client_secret': installed.get('client_secret'),
            'refresh_token': token.get('refresh_token'),
            'grant_type': 'refresh_token'
        },
        timeout=30,
    )

    if resp.status_code != 200:
        raise RuntimeError(f'Falha ao renovar token OAuth ({resp.status_code}): {resp.text[:300]}')

    new_data = resp.json()
    token['access_token'] = new_data['access_token']
    token['expires_in'] = new_data.get('expires_in', 3599)
    token['token_type'] = new_data.get('token_type', 'Bearer')
    token['scope'] = new_data.get('scope', token.get('scope'))
    now = datetime.now(timezone.utc)
    token['expires_at'] = (now + timedelta(seconds=token['expires_in'] - 60)).isoformat()
    token['refreshed_at'] = now.isoformat()

    save_json(os.path.join(WORKSPACE, 'google-ads-token.json'), token)
    return token


def token_is_expired(token):
    expires_at = token.get('expires_at')
    if not expires_at:
        return True
    try:
        return datetime.now(timezone.utc) >= datetime.fromisoformat(expires_at)
    except Exception:
        return True


def token_refresh_older_than_24h(token):
    refreshed_at = token.get('refreshed_at')
    if not refreshed_at:
        return True
    try:
        return (datetime.now(timezone.utc) - datetime.fromisoformat(refreshed_at)) >= timedelta(hours=24)
    except Exception:
        return True


def load_credentials():
    token = load_json(os.path.join(WORKSPACE, 'google-ads-token.json'))
    config = load_json(os.path.join(WORKSPACE, 'google-ads-config.json'))

    if token_is_expired(token) or token_refresh_older_than_24h(token):
        token = refresh_access_token(token)

    return token, config


def normalize_account_name(value):
    value = str(value or '').strip().lower()
    value = re.sub(r'\[.*?\]', ' ', value)
    value = re.sub(r'[^a-z0-9à-ÿ]+', ' ', value, flags=re.IGNORECASE)
    return ' '.join(value.split())


def list_accessible_accounts(token, config):
    dev_token = config['developer_token']
    manager_customer_id = str(config.get('customer_id', '')).replace('-', '')
    query_url = f'https://googleads.googleapis.com/v20/customers/{manager_customer_id}/googleAds:searchStream'
    payload = {
        'query': (
            'SELECT customer_client.id, customer_client.descriptive_name, '
            'customer_client.manager, customer_client.status, customer_client.level '
            'FROM customer_client ORDER BY customer_client.level, customer_client.descriptive_name'
        )
    }
    headers = {
        'Authorization': f"Bearer {token['access_token']}",
        'developer-token': dev_token,
        'Content-Type': 'application/json',
        'login-customer-id': manager_customer_id,
    }
    resp = requests.post(query_url, headers=headers, json=payload, timeout=60)
    if resp.status_code == 401:
        token = refresh_access_token(token)
        headers['Authorization'] = f"Bearer {token['access_token']}"
        resp = requests.post(query_url, headers=headers, json=payload, timeout=60)
    if resp.status_code != 200:
        raise RuntimeError(f'Falha ao listar contas ({resp.status_code}): {resp.text[:300]}')

    accounts = []
    for chunk in resp.json():
        for result in chunk.get('results', []):
            cc = result.get('customerClient', {})
            accounts.append({
                'id': str(cc.get('id', '')).replace('-', ''),
                'name': cc.get('descriptiveName', ''),
                'status': cc.get('status', ''),
                'manager': bool(cc.get('manager', False)),
                'level': int(cc.get('level', 0) or 0),
            })
    return accounts


def resolve_customer_id(account_input, token, config):
    if not account_input:
        return '5150697270'

    raw = str(account_input).strip()
    digits = raw.replace('-', '').replace(' ', '')
    if digits.isdigit():
        return digits

    alias_key = re.sub(r'[^a-z0-9à-ÿ]+', '', raw.lower(), flags=re.IGNORECASE)
    if alias_key in ACCOUNT_ALIASES:
        return ACCOUNT_ALIASES[alias_key]

    accounts = list_accessible_accounts(token, config)
    needle = normalize_account_name(raw)
    exact = [a for a in accounts if normalize_account_name(a['name']) == needle]
    if len(exact) == 1:
        return exact[0]['id']

    partial = [a for a in accounts if needle and needle in normalize_account_name(a['name'])]
    if len(partial) == 1:
        return partial[0]['id']

    if len(exact) > 1 or len(partial) > 1:
        matches = exact if len(exact) > 1 else partial
        match_text = ', '.join(f"{a['name']} ({a['id']})" for a in matches[:10])
        raise RuntimeError(f'Nome de conta ambíguo: "{raw}". Matches: {match_text}')

    available = ', '.join(f"{a['name']} ({a['id']})" for a in accounts[:10])
    raise RuntimeError(f'Conta não encontrada para "{raw}". Exemplos disponíveis: {available}')


def query_google_ads(gaql_query, customer_id=None):
    token, config = load_credentials()

    dev_token = config['developer_token']
    manager_customer_id = str(config.get('customer_id', '')).replace('-', '')
    customer_id = resolve_customer_id(customer_id, token, config)

    query_url = f'https://googleads.googleapis.com/v20/customers/{customer_id}/googleAds:searchStream'
    payload = {'query': gaql_query}

    def do_request(access_token, include_login_customer=True):
        headers = {
            'Authorization': f'Bearer {access_token}',
            'developer-token': dev_token,
            'Content-Type': 'application/json'
        }
        if include_login_customer and manager_customer_id and manager_customer_id != customer_id:
            headers['login-customer-id'] = manager_customer_id
        return requests.post(query_url, headers=headers, json=payload, timeout=60)

    # First try manager-routed request.
    resp = do_request(token['access_token'], include_login_customer=True)

    if resp.status_code == 401:
        token = refresh_access_token(token)
        resp = do_request(token['access_token'], include_login_customer=True)

    # Fallback: some accessible customers work only through direct OAuth access without
    # forcing the manager path via login-customer-id.
    if resp.status_code == 403:
        resp = do_request(token['access_token'], include_login_customer=False)

    if resp.status_code == 200:
        return json.loads(resp.text)

    print(f'Erro: {resp.status_code}')
    print(resp.text[:500])
    return None

def extract_requested_fields(query):
    """Extract fields the user asked for from the GAQL query."""
    fields = []
    
    # Extract SELECT fields
    select_match = re.search(r'SELECT\s+(.+?)\s+FROM', query, re.IGNORECASE | re.DOTALL)
    if select_match:
        select_part = select_match.group(1)
        # Split by comma but handle nested structures
        raw_fields = [f.strip() for f in select_part.split(',')]
        for field in raw_fields:
            field = field.strip()
            if field:
                fields.append(field)
    
    return fields

def format_value(field_name, value):
    """Format value based on field type."""
    if 'cost_micros' in field_name.lower() or 'costmicros' in field_name.lower():
        return parse_currency_from_micros(value)
    elif 'impressions' in field_name.lower() or 'clicks' in field_name.lower() or 'conversions' in field_name.lower():
        return brazilian_format(int(value))
    elif isinstance(value, float):
        return brazilian_format(value)
    elif isinstance(value, int):
        return brazilian_format(value)
    return str(value)

def snake_to_camel(snake_str):
    """Convert snake_case to camelCase."""
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def format_results(data, requested_fields):
    """Format and print results showing only requested fields."""
    if not data:
        return
    
    all_results = []
    for chunk in data:
        all_results.extend(chunk.get('results', []))
    
    if not all_results:
        print('Nenhum resultado encontrado.')
        return
    
    # Aggregate totals for metrics
    totals = {}
    
    for result in all_results:
        for field in requested_fields:
            if 'metrics.' in field:
                # Extract metric value - convert snake_case to camelCase for API
                metric_name_snake = field.replace('metrics.', '')
                metric_name_camel = snake_to_camel(metric_name_snake)
                value = result.get('metrics', {}).get(metric_name_camel, 0)
                if field not in totals:
                    totals[field] = 0
                totals[field] += float(value) if isinstance(value, (int, float, str)) else 0
    
    # Print totals if metrics were requested
    if totals:
        print()
        for field in requested_fields:
            if field in totals:
                formatted = format_value(field, totals[field])
                # Clean field name for display
                display_name = field.replace('metrics.', '').replace('_', ' ').title()
                print(f"{display_name}: {formatted}")
        print()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    customer_id = None
    args = sys.argv[1:]

    if '--list-accounts' in args:
        token, config = load_credentials()
        reverse_aliases = {}
        for alias, cid in ACCOUNT_ALIASES.items():
            reverse_aliases.setdefault(cid, []).append(alias)
        for account in list_accessible_accounts(token, config):
            marker = 'MCC' if account['manager'] else 'Conta'
            aliases = ', '.join(sorted(reverse_aliases.get(account['id'], [])))
            suffix = f" | aliases: {aliases}" if aliases else ''
            print(f"{account['name']} | {account['id']} | {marker} | {account['status']}{suffix}")
        sys.exit(0)

    if '--account' in args:
        idx = args.index('--account')
        customer_id = args[idx + 1]
        args = args[:idx] + args[idx+2:]

    query = ' '.join(args)
    requested_fields = extract_requested_fields(query)

    try:
        results = query_google_ads(query, customer_id)
        if results:
            format_results(results, requested_fields)
    except RuntimeError as e:
        print(f'Erro: {e}')
        sys.exit(1)
