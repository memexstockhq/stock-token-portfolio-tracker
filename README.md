# Stock Token Portfolio Tracker

[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Chains](https://img.shields.io/badge/Chains-RH%20%7C%20BSC%20%7C%20EVM-lightgrey)](configs/)

**Know exactly where you stand**

Portfolio tracker for stock tokens: P&L, cost basis, exposure by chain/ticker, tax-lot tracking, CSV import/export and TUI + web views.

## Quick start

```bash
git clone https://github.com/cervemone/stock-token-portfolio-tracker.git
cd stock-token-portfolio-tracker
pip install -r requirements.txt   # or: npm install
python -m src.main --help
```

## Layout

```
  core/
  importers/
  reporting/
  ui/
  api/
  tests/
  docs/
  scripts/
  configs/
  examples/
  data/
  integrations/
```

## Related

- `stock-token-index` — the registry this repo builds on
- `stock-analyst-agent` — the agent that consumes this data
- `rh-stock-token-sdk` — SDK for BNB Chain stock tokens

## License

MIT
