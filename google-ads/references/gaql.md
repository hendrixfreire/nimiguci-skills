# Google Ads GAQL Reference

Common GAQL (Google Ads Query Language) patterns for querying Google Ads data.

## Account Information

```sql
-- List accessible customers
SELECT customer.id, customer.descriptive_name FROM customer
```

## Campaign Queries

### Basic Campaign Info
```sql
SELECT 
    campaign.id,
    campaign.name,
    campaign.status,
    campaign.advertising_channel_type
FROM campaign
```

### Campaigns with Performance Metrics (All Time)
```sql
SELECT 
    campaign.id,
    campaign.name,
    campaign.status,
    metrics.impressions,
    metrics.clicks,
    metrics.cost_micros,
    metrics.conversions,
    metrics.ctr
FROM campaign
```

### Campaigns with Date Range (Last 30 Days)
```sql
SELECT 
    campaign.id,
    campaign.name,
    campaign.status,
    segments.date,
    metrics.impressions,
    metrics.clicks,
    metrics.cost_micros
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
```

### Campaigns by Status
```sql
-- Only enabled campaigns
SELECT campaign.id, campaign.name FROM campaign WHERE campaign.status = 'ENABLED'

-- Only paused campaigns
SELECT campaign.id, campaign.name FROM campaign WHERE campaign.status = 'PAUSED'

-- Exclude removed campaigns
SELECT campaign.id, campaign.name FROM campaign WHERE campaign.status != 'REMOVED'
```

## Ad Group Queries

```sql
SELECT 
    ad_group.id,
    ad_group.name,
    ad_group.status,
    campaign.name
FROM ad_group
```

## Ad Queries

```sql
SELECT 
    ad.id,
    ad.type,
    ad_group.name,
    campaign.name
FROM ad
```

## Keyword Queries

```sql
SELECT 
    ad_group_criterion.criterion_id,
    ad_group_criterion.keyword.text,
    ad_group_criterion.keyword.match_type,
    ad_group.name,
    campaign.name
FROM ad_group_criterion
WHERE ad_group_criterion.type = 'KEYWORD'
```

## Search Terms (Query Report)

```sql
SELECT 
    search_term_view.search_term,
    metrics.impressions,
    metrics.clicks,
    metrics.cost_micros,
    metrics.conversions
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

## Date Range Options

- `DURING LAST_7_DAYS`
- `DURING LAST_14_DAYS`
- `DURING LAST_30_DAYS`
- `DURING THIS_MONTH`
- `DURING LAST_MONTH`
- `DURING THIS_QUARTER`
- `DURING LAST_QUARTER`
- `BETWEEN 'YYYY-MM-DD' AND 'YYYY-MM-DD'`

## Common Metrics

| Metric | Description |
|--------|-------------|
| `metrics.impressions` | Number of impressions |
| `metrics.clicks` | Number of clicks |
| `metrics.cost_micros` | Cost in micros (divide by 1,000,000 for dollars) |
| `metrics.ctr` | Click-through rate (0.0 to 1.0) |
| `metrics.average_cpc` | Average cost per click |
| `metrics.conversions` | Number of conversions |
| `metrics.cost_per_conversion` | Cost per conversion |
| `metrics.conversion_rate` | Conversion rate |

## Common Campaign Status Values

- `ENABLED` - Active and running
- `PAUSED` - Paused by user
- `REMOVED` - Deleted/archived
