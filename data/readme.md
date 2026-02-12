# Data Dictionary

## Raw Data

### `cbn_rates/`
- **Source:** Central Bank of Nigeria
- **Update frequency:** Daily
- **Fields:**
  - `date`: Date of rate (YYYY-MM-DD)
  - `currency`: Currency code (USD, GBP, EUR)
  - `buying_rate`: CBN buying rate
  - `selling_rate`: CBN selling rate

### `api_rates/`
- **Source:** ExchangeRate-API
- **Update frequency:** Hourly
- **Fields:**
  - `timestamp`: ISO 8601 timestamp
  - `base_currency`: NGN
  - `rates`: Dictionary of exchange rates

## Processed Data

### `combined_rates.csv`
- Merged CBN + API data
- **Fields:**
  - `date`: Date
  - `usd_cbn_official`: Official CBN rate
  - `usd_market`: Market rate from API
  - `spread`: Difference between official and market
  - `gbp_market`: GBP rate
  - `eur_market`: EUR rate