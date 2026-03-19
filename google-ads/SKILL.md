---
name: google-ads
description: Query Google Ads account data using the Google Ads API with Brazilian number formatting. Use when the user asks to query, fetch, retrieve, or get data from Google Ads, including campaigns, ad groups, ads, keywords, metrics, performance data, or account information. Also use for Google Ads reporting, campaign analysis, or any Google Ads data retrieval tasks. Outputs data in Brazilian format (R$ 1.234,56) and only returns requested metrics.
---

# Google Ads Skill (Brazilian Format)

Query Google Ads data with Brazilian number formatting (R$ 1.234,56).

## Key Features

- **Brazilian formatting**: Numbers use dot for thousands, comma for decimals (1.234,56)
- **Currency**: Displayed as R$ 1.234,56
- **Only requested data**: Only returns metrics explicitly asked for
- **Always returns data**: Aggregates totals across all campaigns

## Prerequisites

Credential files in workspace root:
- `projects/google-ads/config/google-ads-auth.json` - OAuth client credentials
- `projects/google-ads/config/google-ads-token.json` - OAuth tokens  
- `projects/google-ads/config/google-ads-config.json` - Developer token

## Usage

### Query Specific Metrics

```bash
cd /root/.openclaw/workspace/skills/google-ads/scripts

# Only cost
python3 query.py "SELECT metrics.cost_micros FROM campaign WHERE segments.date DURING LAST_30_DAYS"
# Output: R$ 14.670,67

# Only impressions
python3 query.py "SELECT metrics.impressions FROM campaign WHERE segments.date DURING LAST_30_DAYS"  
# Output: 56.377

# Multiple metrics
python3 query.py "SELECT metrics.cost_micros, metrics.impressions, metrics.clicks FROM campaign WHERE segments.date DURING LAST_30_DAYS"
# Output:
# Cost Micros: R$ 14.670,67
# Impressions: 56.377
# Clicks: 6.849
```

### List Campaigns with Activity

```bash
python3 list_campaigns.py
```

### List Accounts

```bash
python3 list_accounts.py
```

## Number Formatting

| Format | Example |
|--------|---------|
| Currency | R$ 14.670,67 |
| Numbers | 56.377 |
| Decimals | 12,15% |

## Account Access Notes

- The effective set of accessible accounts depends on the OAuth user and Google Ads hierarchy.
- The query script now resolves accounts from `customers:listAccessibleCustomers` first, which is more reliable across agents than assuming only one manager traversal path.
- Use `--account ID` or `--account <name/alias>` to target a specific account.
- If one agent can access an account and another cannot, compare token, MCC routing, and whether `login-customer-id` is being forced.

## API

- Version: Google Ads API v20
- Endpoint: searchStream
