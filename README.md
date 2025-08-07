# 🛒 E-Commerce ETL Pipeline Project

This project demonstrates an end-to-end data pipeline simulating e-commerce sales data. It highlights skills in Python-based data generation, SQL-based transformations in Snowflake, and data visualization using Tableau Public.

---

## 📌 Project Overview

**Goal:** Build a scalable ETL pipeline to simulate, process, and analyze sales data for a fictional e-commerce business.

**Stack Used:**
- 🐍 Python (Faker, Pandas, Colab)
- ❄️ Snowflake (Data Warehouse)
- 📊 Tableau Public (Dashboards)
<img width="1298" height="1388" alt="ECommerce Orders Dashboard" src="https://github.com/user-attachments/assets/02fd3155-ed5d-4408-9eb4-6da9d9fffc00" />
- 📝 GitHub (Documentation & Version Control)

---

## 🧱 Pipeline Architecture

```text
+----------------+      +-------------+      +-------------+      +------------------+
| Python (Faker) | -->  | orders.csv  | -->  | Snowflake   | -->  | Tableau Dashboards |
+----------------+      +-------------+      +-------------+      +------------------+
    [Extract]              [Raw File]         [Transform]              [Visualize]
