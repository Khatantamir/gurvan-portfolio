from __future__ import annotations
import os
import pandas as pd
import matplotlib.pyplot as plt

PROCESSED_DAILY = os.path.join("data", "processed", "fact_marketing_daily.csv")
REPORTS_DIR = os.path.join("reports")

def _ensure_dirs() -> None:
    os.makedirs(REPORTS_DIR, exist_ok=True)

def main() -> None:
    _ensure_dirs()
    df = pd.read_csv(PROCESSED_DAILY)
    df["date"] = pd.to_datetime(df["date"])
    daily = df.groupby("date", as_index=False).agg(spend=("spend","sum"), revenue=("revenue","sum"))

    plt.figure()
    plt.plot(daily["date"], daily["spend"])
    plt.title("Total Spend Over Time")
    plt.xlabel("Date"); plt.ylabel("Spend")
    plt.tight_layout()
    plt.savefig(os.path.join(REPORTS_DIR, "spend_over_time.png"), dpi=160)
    plt.close()

    plt.figure()
    plt.plot(daily["date"], daily["revenue"])
    plt.title("Total Revenue Over Time")
    plt.xlabel("Date"); plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(os.path.join(REPORTS_DIR, "revenue_over_time.png"), dpi=160)
    plt.close()

    print("[OK] Saved charts in /reports")

if __name__ == "__main__":
    main()
