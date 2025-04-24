# 🌍 World Holidays ETL Project

This project is an end-to-end **ETL (Extract, Transform, Load)** pipeline that collects, processes, and stores public holiday data from around the world.

---

## 🚀 Project Overview

This project implements a complete ETL pipeline that collects and processes worldwide public holiday data.

- **Extract**: Scrapes holiday data from a public website.
- **Transform**: Cleans and structures the raw data for consistency.
- **Load**: Saves the cleaned data into an Excel or CSV file for easy access and then loads it into a database for production use.

---

## ✨ Features

- 🔎 Scrapes holiday data from a live website using BeautifulSoup.
- 🧹 Cleans and formats the data using pandas.
- 📊 Saves the final structured data into an Excel file.
- 🧪 Modular design with separate scripts for each ETL phase.
- ▶️ Includes a `run_etl.py` script to execute the entire pipeline with a single command.

---

## 🛠️ Technologies Used

- Python 3
- BeautifulSoup (for HTML parsing)
- Requests (for making HTTP requests)
- argparse (for CLI support)
- pandas (for data handling)
- openpyxl (for Excel file export)

---

## 🌐 Data Source

Holiday data is scraped from [calendarific.com](https://calendarific.com)

## 🔧 Setup Instructions

1. Clone the repository:
```bash
    git clone git@github.com:sumitgit1912/world-holidays-etl.git
    cd world-holidays-etl
```

2. Install the required packages:
```bash
    pip install -r requirements.txt
```

## 🧾 Usage
Run the full ETL pipeline
```bash
    python run_etl.py
```

## 📁 Project Structure
```bash
world-holidays-etl/
├── etl/
│   ├── extract.py         # Extracts raw holiday data
│   ├── transform.py       # Cleans and structures the data
│   ├── load.py            # Saves data to Excel and/or database
│   └── run_etl.py         # Runs the full ETL pipeline
├── data/                  # Folder for storing output files
│   ├── extracted_holidays.xlsx   # Raw holiday data output file
│   ├── formatted_holidays.xlsx   # Formatted output file
│   └── formatted_holidays.sql    # SQL queries for database insertion
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```