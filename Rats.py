import csv

date_to_interest = {}
my_path = "C:\\Users\\Admin\\Downloads\\BR (1).csv"
with open(my_path, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)

    headers = next(csvreader)

    for row in csvreader:
        date_str = row[headers.index("TIME_PERIOD")]

        interest_value = row[headers.index("OBS_VALUE")]

        interest_rate = float(interest_value)

        year, month, day = date_str.split('-')

        if day == '01':
            key = f"{year}-{month}"
            date_to_interest[key] = interest_rate

print(date_to_interest)

my_data = {}
my_data["avg"] = None
my_data["total"] = None
my_data["min"] = None
my_data["max"] = None
my_data["start"] = None
my_data["end"] = None


def get_rate_by_date(start_date_str, end_date_str):

    filtered_data = {}

    for date, rate in date_to_interest.items():
        if start_date_str <= date <= end_date_str:
            filtered_data[date] = rate

    rates = list(filtered_data.values())

    my_data["avg"] = sum(rates) / len(rates)
    my_data["total"] = sum(rates)
    my_data["min"] = min(rates)
    my_data["max"] = max(rates)
    my_data["start"] = filtered_data[min(filtered_data.keys())]
    my_data["end"] = filtered_data[max(filtered_data.keys())]



start_date_str = "1994-10"
end_date_str = "2024-08"
get_rate_by_date(start_date_str, end_date_str)

print(my_data)
