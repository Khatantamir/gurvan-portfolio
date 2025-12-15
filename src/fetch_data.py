from __future__ import annotations
import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

RAW_DIR = os.path.join("data", "raw")

def _ensure_dirs() -> None:
    os.makedirs(RAW_DIR, exist_ok=True)

def generate_dummy_marketing_data(days: int = 120, seed: int = 42) -> pd.DataFrame:
    """
    Creates a realistic dummy dataset representing a simple marketing funnel:
    spend -> clicks -> leads -> sales -> revenue across channels.
    No PII.
    """
    rng = np.random.default_rng(seed)
    end = datetime.utcnow().date()
    start = end - timedelta(days=days - 1)
    dates = pd.date_range(start=start, end=end, freq="D")

    channels = ["facebook_ads", "google_ads", "organic"]
    rows = []
    for d in dates:
        for ch in channels:
            base_spend = {"facebook_ads": 120, "google_ads": 150, "organic": 0}[ch]
            spend = max(0, base_spend + rng.normal(0, 25))
            clicks = int(max(0, (spend * rng.uniform(3.5, 6.0)) + rng.normal(0, 40))) if spend > 0 else int(rng.uniform(40, 140))
            ctr = rng.uniform(0.008, 0.04) if ch != "organic" else rng.uniform(0.02, 0.08)
            # crude impression estimate
            impressions = int(max(clicks / max(ctr, 1e-6), clicks))
            cpc = spend / clicks if clicks > 0 else 0

            lead_rate = {"facebook_ads": 0.03, "google_ads": 0.045, "organic": 0.06}[ch]
            leads = int(max(0, clicks * (lead_rate + rng.normal(0, 0.01))))

            close_rate = {"facebook_ads": 0.10, "google_ads": 0.12, "organic": 0.14}[ch]
            sales = int(max(0, leads * (close_rate + rng.normal(0, 0.02))))

            avg_sale = {"facebook_ads": 90, "google_ads": 110, "organic": 95}[ch]
            revenue = max(0, sales * (avg_sale + rng.normal(0, 10)))

            rows.append({
                "date": d.date().isoformat(),
                "channel": ch,
                "spend": round(float(spend), 2),
                "impressions": impressions,
                "clicks": clicks,
                "leads": leads,
                "sales": sales,
                "revenue": round(float(revenue), 2),
            })

    df = pd.DataFrame(rows)
    return df

def main() -> None:
    _ensure_dirs()
    df = generate_dummy_marketing_data(days=180, seed=42)
    out_path = os.path.join(RAW_DIR, "marketing_funnel_raw.csv")
    df.to_csv(out_path, index=False)
    print(f"[OK] Wrote raw data: {out_path} rows={len(df)}")

if __name__ == "__main__":
    main()
