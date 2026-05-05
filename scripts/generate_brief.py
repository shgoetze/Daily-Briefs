#!/usr/bin/env python3
"""Generate today's pre-market brief and write to briefs/YYYY-MM-DD-brief.md."""

import datetime
import pathlib
import sys

import anthropic

SYSTEM_PROMPT = """You are a Pre-Market Financial Analyst.

Compile a "Pre-Market Brief" by searching Yahoo Finance, Reuters, CNBC, and
non-paywalled aggregators (MarketWatch, Seeking Alpha, etc.). Avoid WSJ and
Bloomberg full articles directly (paywall risk).

Output ONLY the markdown brief, with no preamble or commentary outside it.

Format:

# Daily Market Brief — <Month> <Day>, <Year>

*Reference period: trading day <Weekday>, <Month> <Day>, <Year>.*

## Top Movers (Large Cap, > $10B, > 5%)

| Ticker | Move | Verified Reason |
|--------|------|-----------------|
| TICK | +X% | <under 15 words> |

3-5 entries. If none qualify, state "No significant large-cap movement."

## Reporting Today / After Close Last Session

| Company | Ticker | Timing |
|---------|--------|--------|
| Name | TICK | Pre-market (today) / Post-market (today/yesterday) |

## Geopolitical Brief (Last 24h)

- 2-3 bullets focused on oil, chips, or forex impact, under 15 words each.

## Rates Brief

- 10Y UST yield level + recent change.
- FOMC commentary, PCE data, or Fed-speak from last 24-72h.
- 3-5 bullets total.

## Sources

- [Title](URL)
- list every URL consulted

Constraints:
- Large caps > $10B with > 5% prior-session moves only for Top Movers.
- Each bullet/cell description < 15 words.
- Verify reasons against multiple sources.
- Use the web_search tool to gather current data.
"""


def generate_brief(today: datetime.date) -> str:
    client = anthropic.Anthropic()
    weekday = today.strftime("%A")

    user_msg = (
        f"Today is {weekday}, {today.strftime('%B %d, %Y')}. "
        "Compile today's Pre-Market Brief. The reference trading day is the "
        "most recent prior session (yesterday, or Friday if today is Monday). "
        "Use web search to verify current data and cite every source URL."
    )

    messages = [{"role": "user", "content": user_msg}]
    text_parts: list[str] = []

    for _ in range(10):
        response = client.messages.create(
            model="claude-opus-4-7",
            max_tokens=16000,
            thinking={"type": "adaptive"},
            output_config={"effort": "high"},
            system=[
                {
                    "type": "text",
                    "text": SYSTEM_PROMPT,
                    "cache_control": {"type": "ephemeral"},
                }
            ],
            tools=[
                {
                    "type": "web_search_20260209",
                    "name": "web_search",
                    "max_uses": 15,
                }
            ],
            messages=messages,
        )

        for block in response.content:
            if block.type == "text":
                text_parts.append(block.text)

        if response.stop_reason == "pause_turn":
            messages.append({"role": "assistant", "content": response.content})
            continue
        break

    return "\n\n".join(p.strip() for p in text_parts if p.strip()).strip()


def main() -> int:
    today = datetime.datetime.now(datetime.timezone.utc).date()
    brief = generate_brief(today)
    if not brief:
        print("Empty brief returned from model.", file=sys.stderr)
        return 1

    out_dir = pathlib.Path("briefs")
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / f"{today.isoformat()}-brief.md"
    out_path.write_text(brief + "\n")
    print(f"Wrote {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
