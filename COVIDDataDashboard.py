import csv
import matplotlib.pyplot as plt
covid_data = []

def add_covid_record():
    city = input("Enter city name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    cases = int(input("Enter new cases: "))
    recoveries = int(input("Enter recoveries: "))
    deaths = int(input("Enter deaths: "))

    record = {
        'city': city,
        'date': date,
        'cases': cases,
        'recoveries': recoveries,
        'deaths': deaths
    }

    covid_data.append(record)
    print("Record added successfully!\n")


def plot_city_trend():
    city = input("Enter city to visualize: ")

    # Filter and sort records by date
    city_records = [r for r in covid_data if r['city'].lower() == city.lower()]
    if not city_records:
        print("No data for this city.")
        return

    city_records.sort(key=lambda r: r['date'])

    dates = [r['date'] for r in city_records]
    cases = [r['cases'] for r in city_records]
    recoveries = [r['recoveries'] for r in city_records]
    deaths = [r['deaths'] for r in city_records]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, cases, label='Cases', color='red', marker='o')
    plt.plot(dates, recoveries, label='Recoveries', color='green', marker='o')
    plt.plot(dates, deaths, label='Deaths', color='gray', marker='o')

    plt.title(f'COVID-19 Trend in {city.title()}')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def view_all_records():
    if not covid_data:
        print("No records found.")
        return

    print("\n📋 COVID Records:")
    for r in covid_data:
        print(f"{r['date']} | {r['city']} | Cases: {r['cases']}, Recoveries: {r['recoveries']}, Deaths: {r['deaths']}")

from collections import defaultdict

def show_summary():
    if not covid_data:
        print("No data to summarize.")
        return

    total_cases = sum(r['cases'] for r in covid_data)
    total_recoveries = sum(r['recoveries'] for r in covid_data)
    total_deaths = sum(r['deaths'] for r in covid_data)

    print(f"\n📊 Summary:")
    print(f"Total Cases: {total_cases}")
    print(f"Total Recoveries: {total_recoveries}")
    print(f"Total Deaths: {total_deaths}")
def detect_risk_zones(threshold=100):
    city_cases = defaultdict(int)

    for r in covid_data:
        city_cases[r['city']] += r['cases']

    print(f"\n⚠️ High-Risk Cities (Cases > {threshold}):")
    found = False
    for city, total in city_cases.items():
        if total > threshold:
            print(f"{city}: {total} cases")
            found = True

    if not found:
        print("No high-risk zones.")

def save_to_csv(filename='covid_data.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['city', 'date', 'cases', 'recoveries', 'deaths'])
        writer.writeheader()
        writer.writerows(covid_data)
    print("Data saved to CSV.")

def load_from_csv(filename='covid_data.csv'):
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            covid_data.clear()
            for row in reader:
                row['cases'] = int(row['cases'])
                row['recoveries'] = int(row['recoveries'])
                row['deaths'] = int(row['deaths'])
                covid_data.append(row)
        print("Data loaded from CSV.")
    except FileNotFoundError:
        print("No saved data found.")

while True:
    print("\n=== COVID Data Dashboard ===")
    print("1. Add COVID Record")
    print("2. View All Records")
    print("3. Show Summary")
    print("4. Detect Risk Zones")
    print("5. Save to CSV")
    print("6. Load from CSV")
    print("7. Plot City Trend")
    print("8. Exit")




    choice = input("Choose an option: ")

    if choice == '1':
        add_covid_record()
    elif choice == '2':
        view_all_records()
    elif choice == '3':
        show_summary()
    elif choice == '4':
        detect_risk_zones()
    elif choice == '5':
        save_to_csv()
    elif choice == '6':
        load_from_csv()
    elif choice == '7':
        plot_city_trend()
    elif choice == '8':
        print("Exiting dashboard.")
        break

    else:
        print("Invalid choice.")
