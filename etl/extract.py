from bs4 import BeautifulSoup
import requests
import pandas as pd
import argparse
from dotenv import load_dotenv
import os

load_dotenv()

base_url = os.getenv("BASE_URL")

def get_country_details(url):
    """Fetch all country blocks from the base URL."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find_all('div', class_="col-xs-12 col-md-4")

def extract_country_info(detail):
    """Extract country name, ISO2 code, and full URL to its holiday page."""
    link_tag = detail.find('a')
    iso2_code = detail.find('code')

    if not link_tag or not iso2_code:
        return None

    country_name = link_tag.text.strip()
    iso2 = iso2_code.text.strip()
    relative_link = link_tag.get('href')
    full_url = f"{base_url}{relative_link.lstrip('/')}"
    return country_name, iso2, full_url

def scrape_holidays(country, iso2, holidays_url):
    """Scrape holidays for a specific country from its holiday page."""
    holidays = []
    try:
        response = requests.get(holidays_url)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find('table', class_="table table-hover table-striped table-bordered holiday-list")

        if not table:
            return holidays

        tbody = table.find('tbody')
        for row in tbody.find_all('tr'):
            row_data = [country, iso2]
            row_data.extend(cell.text.strip() for cell in row.find_all('td'))
            holidays.append(row_data)
    except Exception as e:
        print(f"Error scraping {country}: {e}")

    return holidays

def scrape_all_holidays():
    """Main function to orchestrate scraping for all countries."""
    all_holidays = []
    country_details = get_country_details(base_url)

    for detail in country_details:
        info = extract_country_info(detail)
        if info:
            country, iso2, holidays_url = info
            holidays = scrape_holidays(country, iso2, holidays_url)
            all_holidays.extend(holidays)

    columns = ['country', 'iso2_code', 'holiday', 'date', 'detail']
    return pd.DataFrame(all_holidays, columns=columns)

def save_to_file(df, filename, file_format):
    """Save the DataFrame to a file in CSV or Excel format."""
    if file_format == 'csv':
        df.to_csv(filename, index=False)
    elif file_format == 'excel':
        df.to_excel(filename, index=False)
    print(f"Saved to {filename}")

# if __name__ == "__main__":
parser = argparse.ArgumentParser(description="Scrape worldwide holidays from calendarific.com")
parser.add_argument("--format", choices=['csv', 'excel'], default='csv', help="Output file format")
parser.add_argument("--output", default="extracted_holidays", help="Output filename without extension")
args = parser.parse_args()

df = scrape_all_holidays()
df = scrape_all_holidays()
filename = f"data/{args.output}.{'csv' if args.format == 'csv' else 'xlsx'}"
save_to_file(df, filename, args.format)
