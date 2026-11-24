import csv, json

records = []

with open('students.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        records.append(row)

with open('studednts.json', 'w') as json_file:
    json.dump(records, json_file, indent=4)

print("CSV file converted tp JSON")