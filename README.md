# Automated Marketing Performance Data Pipeline

## Overview
This project demonstrates a fully automated marketing analytics data pipeline designed to track performance, compute KPIs, and generate visual reports.

The entire workflow runs automatically using GitHub Actions and simulates real-world data engineering practices.

---

## Problem
Marketing teams often struggle to understand:
- Which channels generate the most value
- How ad spend translates into revenue
- How performance changes over time

Manual reporting is time-consuming and error-prone.

---

## Solution
This project automates the full analytics lifecycle:

1. Generate raw marketing funnel data
2. Transform data into clean KPI tables
3. Generate visual performance reports
4. Automatically commit outputs using CI/CD

All steps run on demand or on a scheduled basis via GitHub Actions.

---

## Automated Workflow (CI/CD)
The pipeline is executed using **GitHub Actions**:

- Manual trigger support
- Scheduled weekly runs
- Automatic commit of generated outputs

### Pipeline Steps
- `fetch_data.py` → Generate raw funnel data
- `transform.py` → Compute KPIs (CTR, CVR, ROAS)
- `make_charts.py` → Create charts and visual reports

---

## Output Artifacts
Each pipeline run produces:

- Raw datasets in `data/raw/`
- Processed KPI tables in `data/processed/`
- Visual reports in `reports/`

These outputs are committed automatically by the workflow.

---

## Why This Matters
This project demonstrates:
- Data engineering fundamentals
- Automation and CI/CD pipelines
- Reproducible analytics workflows
- Business-focused KPI analysis

---

## National Importance Context (EB-NIW)
Automated analytics pipelines like this improve efficiency, reduce operational costs, and enable data-driven decision-making.

Such systems are critical for scaling small and mid-sized businesses and increasing economic productivity.
