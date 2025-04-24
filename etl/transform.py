import pandas as pd
import openpyxl
from datetime import datetime

df = pd.read_excel("data/extracted_holidays.xlsx")

df['formatted_date'] = df['date'].apply(lambda x: datetime.strptime(x, "%A, %B %d, %Y").strftime("%Y-%m-%d"))

df.to_excel("data/formatted_holidays.xlsx", index=False)

insert_query_list = [] 
for index, row in df.iterrows():
    holiday = str(row["holiday"]).replace("'", r"\'").replace("`", r"\`")
    detail = str(row["detail"]).replace("'", r"\'").replace("`", r"\`")
    insert_query = (
        f"INSERT INTO Holidays (country_code, holiday, holiday_detail, date, created_by, updated_by, created_at, updated_at) "
        f"VALUES ('{row['iso2_code']}', '{holiday}', '{detail}', '{row['formatted_date']}', 'System', 'System', NOW(), NOW());"
    )
    insert_query_list.append(insert_query)

holidays_sql_batch = "\n".join(insert_query_list)

with open(f"data/formatted_holidays.sql", "w", encoding="utf-8") as file:
    file.write(holidays_sql_batch)


