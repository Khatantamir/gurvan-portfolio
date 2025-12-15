from __future__ import annotations
import os
import pandas as pd

RAW_PATH = os.path.join("data", "raw", "marketing_funnel_raw.csv")
PROCESSED_DIR = os.path.join("data", "processed")

def _ensure_dirs() -> None:
    os.makedirs(PROCESSED_DIR, exist_ok=True)

def data_quality_checks(df: pd.DataFrame) -> dict:
    checks = {}
    checks["rows"] = int(df.shape[0])
    checks["missing_by_col"] = df.isna().sum().to_dict()
    checks["duplicate_rows"] = int(df.duplicated().sum())
    # basic sanity checks
    checks["negative_spend"] = int((df["spend"] < 0).sum())
    checks["negative_revenue"] = int((df["revenue"] < 0).sum())
    return checks

def compute_kpis(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df["cpc"] = df["spend"] / df["clicks"].replace(0, pd.NA)
    df["cpl"] = df["spend"] / df["leads"].replace(0, pd.NA)
    df["cpa"] = df["spend"] / df["sales"].replace(0, pd.NA)
    df["roas"] = df["revenue"] / df["spend"].replace(0, pd.NA)
    df["ctr"] = df["clicks"] / df["impressions"].replace(0, pd.NA)
    df["lead_rate"] = df["leads"] / df["clicks"].replace(0, pd.NA)
    df["close_rate"] = df["sales"] / df["leads"].replace(0, pd.NA)
    return df

def build_daily_fact(df: pd.DataFrame) -> pd.DataFrame:
    # already daily; keep consistent columns
    cols = [
        "date","channel","spend","impressions","clicks","leads","sales","revenue",
        "cpc","cpl","cpa","roas","ctr","lead_rate","close_rate"
    ]
    out = df[cols].copy()
    out["date"] = out["date"].dt.date.astype(str)
    return out

def build_channel_summary(df: pd.DataFrame) -> pd.DataFrame:
    g = df.groupby("channel", as_index=False).agg(
        spend=("spend","sum"),
        impressions=("impressions","sum"),
        clicks=("clicks","sum"),
        leads=("leads","sum"),
        sales=("sales","sum"),
        revenue=("revenue","sum"),
    )
    g["roas"] = g["revenue"] / g["spend"].replace(0, pd.NA)
    g["cpc"] = g["spend"] / g["clicks"].replace(0, pd.NA)
    g["cpl"] = g["spend"] / g["leads"].replace(0, pd.NA)
    g["cpa"] = g["spend"] / g["sales"].replace(0, pd.NA)
    g["ctr"] = g["clicks"] / g["impressions"].replace(0, pd.NA)
    g["lead_rate"] = g["leads"] / g["clicks"].replace(0, pd.NA)
    g["close_rate"] = g["sales"] / g["leads"].replace(0, pd.NA)
    return g

def main() -> None:
    _ensure_dirs()

    if not os.path.exists(RAW_PATH):
        raise FileNotFoundError(
            f"Missing raw data at {RAW_PATH}. Run: python src/fetch_data.py"
        )

    df = pd.read_csv(RAW_PATH)
    checks = data_quality_checks(df)

    # basic cleaning
    df = df.drop_duplicates()
    df["spend"] = df["spend"].clip(lower=0)
    df["revenue"] = df["revenue"].clip(lower=0)

    df = compute_kpis(df)

    daily_fact = build_daily_fact(df)
    channel_summary = build_channel_summary(df)

    daily_path = os.path.join(PROCESSED_DIR, "fact_marketing_daily.csv")
    channel_path = os.path.join(PROCESSED_DIR, "summary_by_channel.csv")
    checks_path = os.path.join(PROCESSED_DIR, "data_quality_checks.json")

    daily_fact.to_csv(daily_path, index=False)
    channel_summary.to_csv(channel_path, index=False)

    # write checks as JSON without extra deps
    import json
    with open(checks_path, "w", encoding="utf-8") as f:
        json.dump(checks, f, ensure_ascii=False, indent=2)

    print(f"[OK] Processed daily fact: {daily_path} rows={len(daily_fact)}")
    print(f"[OK] Channel summary: {channel_path} rows={len(channel_summary)}")
    print(f"[OK] Quality checks: {checks_path}")

if __name__ == "__main__":
    main()
