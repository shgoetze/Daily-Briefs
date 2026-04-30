# Daily Market Brief

A structured daily market analysis routine that compiles pre-market intelligence for equities, earnings, and geopolitical events affecting global markets.

## Overview

This repository automates the compilation of a "Pre-Market Brief" — a morning market summary identifying significant movers, earnings reports, and geopolitical catalysts. The brief is designed for quick consumption before market open and is delivered via email.

## Role & Purpose

**Role:** Pre-Market Financial Analyst

**Objective:** Generate a daily market brief that captures:
- Large-cap stock movers from the prior trading day
- Upcoming earnings reports (today/tomorrow)
- Geopolitical events affecting oil, chips, or forex markets
- Sourced, verified information in under 5 minutes

## Output Format

The brief is formatted in Markdown and contains the following sections:

### 1. Top Movers (Large Cap Only)
- **Criteria:** Market cap > $10B; price movement > 5% (yesterday)
- **Fields per entry:** Ticker | % Move | Verified Reason
- **Reason examples:** Earnings beat, CEO fired, FDA approval, acquisition announcement
- **Limit:** 3–5 stocks
- **Fallback:** If no significant movers exist, state "No significant large-cap movement."

### 2. Reporting Today/Tomorrow
- **Scope:** Companies releasing earnings before market open (today) or after close (yesterday)
- **Fields:** Company Name | Ticker | Report Timing (pre/post)
- **Limit:** List all material reporters; no strict count limit

### 3. Geopolitical Brief
- **Scope:** 2–3 major geopolitical events from the last 24 hours
- **Focus:** Events specifically impacting oil, chips (semiconductors), or forex markets
- **Format:** Event description | Market impact (brief)
- **Description limit:** Under 15 words per item

### 4. Sources
- **Requirement:** List all URLs consulted
- **Approved sources:** Yahoo Finance, Reuters, CNBC (non-paywalled summaries only)
- **Forbidden sources:** WSJ (full articles), Bloomberg (full articles)
- **Strategy:** Use aggregators for restricted content

## Constraints & Guidelines

| Constraint | Requirement |
|-----------|------------|
| **Source Access** | No WSJ or Bloomberg full articles (paywall risk); use aggregators only |
| **Description Length** | ≤15 words per item |
| **No Movers Fallback** | State "No significant large-cap movement" if none exist |
| **Market Cap Floor** | $10B+ only for Top Movers section |
| **Price Move Threshold** | >5% movement for inclusion |
| **Geopolitical Relevance** | Oil, chips, or forex impact only |
| **Timeframe** | Prior 24 hours (or prior trading day for stock movers) |

## Workflow

1. **Search** Yahoo Finance, Reuters, and CNBC for market data
2. **Filter** for large-cap stocks (>$10B) with >5% movement yesterday
3. **Verify** reasons for moves using multiple sources
4. **Identify** earnings reporters today/tomorrow (pre/post market)
5. **Scan** geopolitical news for oil, chips, or forex relevance
6. **Compile** findings in Markdown format
7. **Email** summary with subject line: `Daily Market Brief`

## Directory Structure

```
daily-market-brief/
├── README.md                    # This file
├── briefs/                      # Archived daily briefs
│   ├── 2025-04-30-brief.md
│   ├── 2025-05-01-brief.md
│   └── ...
├── template.md                  # Blank brief template
├── scripts/                     # (Optional) Automation scripts
│   └── generate_brief.py        # Email & aggregation helper
└── sources.md                   # Curated source URLs (non-paywalled)
```

## Example Output

```markdown
# Daily Market Brief — April 30, 2025

## Top Movers (Large Cap)
| Ticker | Move | Reason |
|--------|------|--------|
| NVDA | +7.2% | Beats Q1 earnings; raised FY guidance on AI demand |
| TSLA | -6.1% | Misses delivery forecast; Elon defers Cybertruck ramp |
| JPM | +4.8% | Q1 earnings beat; releases higher capital deployment plan |

## Reporting Today/Tomorrow
| Company | Ticker | Timing |
|---------|--------|--------|
| Tesla | TSLA | Post-market (today) |
| Meta | META | Pre-market (tomorrow) |

## Geopolitical Brief
- **Taiwan Chip Exports**: New US export controls delay $2B+ semiconductor shipments. Bullish chip futures.
- **Oil Rig Outage**: Nigerian offshore platform down 250K bbl/day; WTI futures +$1.20/bbl.
- **Yuan Weakness**: PBOC cuts reserve ratios; CNY/USD approaches 7.30. DXY +0.3%.

## Sources
- https://finance.yahoo.com/
- https://www.reuters.com/markets/
- https://www.cnbc.com/us-markets/
```

## Email Delivery

**Subject:** `Daily Market Brief`

**To:** [Configure recipient email address]

**Send Time:** Pre-market (recommend 06:00–07:00 ET)

**Format:** Markdown rendered as HTML (if using email templating)

## Getting Started

1. Clone this repository
2. Copy `template.md` to `briefs/` with today's date: `YYYY-MM-DD-brief.md`
3. Complete the brief using approved sources
4. Email the compiled brief (or automate via script)
5. Archive the brief in the `briefs/` folder

## Tips for Efficiency

- **Bookmark sources:** Yahoo Finance, Reuters Markets, CNBC Markets
- **Search operators:** Use `[ticker] earnings` and `geopolitics oil/chips` for faster discovery
- **Verify reason:** Cross-reference stock moves against 2+ sources before including
- **Aggregators:** Use MarketWatch, SeekingAlpha, Investor's Business Daily for restricted content
- **Time block:** Aim for 5-minute completion target

## Automation (Optional)

If building automation, consider:
- Yahoo Finance API (free, no auth required)
- Web scraping (Reuters, CNBC) with BeautifulSoup
- Email integration (SMTP)
- Scheduled execution (cron/GitHub Actions)

## Compliance Notes

- Keep internal to your organization unless distributed with compliance approval
- Verify all sources are non-paywalled or aggregated content
- Do not reproduce copyrighted material from WSJ, Bloomberg, or other premium sources
- Check any templated scripts against your RIA's compliance requirements

## Changelog

- **v1.0** (2025-04-30): Initial repository structure and workflow documentation

---

*Maintained by: [Your Name]*  
*Last Updated: 2025-04-30*
