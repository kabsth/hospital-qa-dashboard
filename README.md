# Healthcare Data QA Dashboard (Streamlit)

## Project Overview

This project is an **interactive Data Quality Assurance (QA) dashboard** built using **Streamlit** to analyze healthcare appointment data.

The dashboard focuses on identifying **data inconsistencies, missing values, duplicates, and anomalies** while providing actionable insights into patient appointment behavior, including **no-show trends**.

---

## Objectives

* Perform **data validation and quality checks** on healthcare records
* Identify **missing, duplicate, and inconsistent data**
* Analyze **patient no-show patterns**
* Build an **interactive dashboard** for real-time data exploration

---

## Features

* Data cleaning and preprocessing
* Missing values detection
* Duplicate records identification
* Invalid data checks (e.g., negative ages)
* No-show analysis
* Interactive filters (Gender, No-show status)
* Visualizations (histograms, count plots)
* Streamlit-based interactive UI

---

## Tech Stack

* **Python**
* **Pandas** – Data manipulation and analysis
* **NumPy** – Numerical operations
* **Seaborn & Matplotlib** – Data visualization
* **Streamlit** – Interactive dashboard development

---

## Project Structure

```
hospital-qa-dashboard/
│
├── app.py                # Streamlit dashboard application
├── data.csv              # Dataset (Kaggle healthcare dataset)
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## Dataset

* **Source:** Kaggle – Medical Appointment No Shows Dataset
* **Records:** ~110,000 patient records
* **Key Features:**

  * Patient demographics (Age, Gender)
  * Appointment details
  * Health conditions (Diabetes, Hypertension, etc.)
  * No-show indicator

---

## Data Quality Checks Implemented

* Missing value detection
* Duplicate record identification
* Invalid age detection (e.g., negative values)
* Data type validation (date conversions)
* Consistency checks across fields

---

## Key Insights

* Distribution of patient ages
* No-show trends by gender
* Overall data quality metrics
* Identification of problematic records

---

## How to Run the Project

### Clone the repository

```
git clone https://github.com/YOUR_USERNAME/hospital-qa-dashboard.git
cd hospital-qa-dashboard
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run the Streamlit app

```
streamlit run app.py
```

---


## Future Improvements

* Add more advanced QA checks (outlier detection, anomaly detection)
* Integrate SQL-based validation queries
* Deploy the app using Streamlit Cloud
* Add more interactive filters and KPIs

---
