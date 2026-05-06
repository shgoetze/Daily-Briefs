# Daily Briefs — Claude Instructions

## Workflow

When asked to compile a Pre-Market Brief:

1. Research using WebSearch (Yahoo Finance, Reuters, CNBC, aggregators — no WSJ/Bloomberg full articles).
2. Write the brief to `briefs/YYYY-MM-DD-brief.md` following the format in `README.md`.
3. Commit and **push directly to `main`** — no PR needed.
   ```
   git add briefs/YYYY-MM-DD-brief.md
   git commit -m "Add daily market brief for YYYY-MM-DD"
   git push origin main
   ```
4. Pushing to `main` automatically triggers `.github/workflows/email-brief.yml`, which emails the brief to shgoetze@gmail.com. No further action required.

## Branch

Always push briefs directly to `main`. Do not create a feature branch or open a PR for routine brief generation.

## Brief format

See `README.md` for the full output spec. Key constraints:
- Large-cap movers: market cap > $10B, price move > 5% prior session only.
- Descriptions ≤ 15 words per item.
- Include a Rates Brief section (10Y yield, FOMC, PCE).
- List every source URL in the Sources section.
