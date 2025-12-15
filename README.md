# Automated Marketing Performance Data Pipeline

## Overview
This project demonstrates a **fully automated marketing analytics data pipeline** that tracks performance, computes key KPIs, and generates visual reports.

The entire workflow runs automatically using **GitHub Actions**, reflecting real-world data engineering and analytics automation practices.

---

## Problem
Marketing teams often struggle to:
- Identify which channels generate the most value
- Understand how ad spend translates into revenue
- Monitor performance trends over time

Manual reporting is time-consuming, error-prone, and difficult to scale.

---

## Solution
This project automates the **end-to-end analytics lifecycle**:

1. Generate raw marketing funnel data  
2. Transform raw data into clean KPI tables  
3. Generate visual performance reports  
4. Automatically commit outputs using CI/CD automation  

All steps run **on demand or on a scheduled basis** via GitHub Actions.

---

## Automated Workflow (CI/CD)
The pipeline is executed using **GitHub Actions** to ensure reproducibility and automation.

### Workflow Capabilities
- Manual trigger support (`workflow_dispatch`)
- Scheduled weekly execution
- Automatic commit of generated data and reports

### Pipeline Steps
- `fetch_data.py` → Generates raw marketing funnel data  
- `transform.py` → Computes KPIs (CTR, Conversion Rate, ROAS)  
- `make_charts.py` → Creates charts and visual performance reports  

---

## Output Artifacts
Each pipeline run produces the following artifacts:

- **Raw datasets** stored in `data/raw/`  
- **Processed KPI tables** stored in `data/processed/`  
- **Visual reports** stored in `reports/`  

All outputs are **automatically committed** back to the repository by the workflow.

---

## Sample Visual Outputs
*(Generated automatically by the pipeline)*

![Marketing Spend Over Time](reports/spend_over_time.png)
![Revenue Over Time](reports/revenue_over_time.png)

> If additional charts are added to `reports/`, they will appear automatically after each pipeline run.

---

## Why This Matters
This project demonstrates practical skills in:

- Data engineering fundamentals  
- CI/CD-driven analytics automation  
- Reproducible and scalable data workflows  
- Business-focused KPI analysis  

It reflects how modern analytics systems support marketing optimization and strategic decision-making.

---

## National Importance Context (EB-NIW)
Automated analytics pipelines like this reduce manual reporting effort, improve decision-making speed, and enable **data-driven resource allocation at scale**.

Such systems help small and mid-sized businesses improve productivity, competitiveness, and economic efficiency—aligning with broader U.S. national interest objectives.

---

## Tech Stack
- Python (Pandas, Matplotlib)
- GitHub Actions (CI/CD)
- Automated data pipelines
- Marketing analytics KPIs

---

## How to Run
The pipeline can be executed in two ways:

1. **Manually** via GitHub Actions → *Run workflow*  
2. **Automatically** via scheduled weekly execution  

No local setup is required.

---

## Project Status
- ✅ Fully automated pipeline  
- ✅ CI/CD workflow verified  
- ✅ Data and reports generated automatically  
- ✅ EB-NIW–ready project structure  
