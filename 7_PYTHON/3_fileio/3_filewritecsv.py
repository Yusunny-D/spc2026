import csv

# data = [
#     ['Name', 'Age', 'City'], # 헤딩 첫 줄
#     ['John', 25, 'Seoul'],
#     ['James', 23, 'Busan'],
#     ['Bob', 24, 'Seoul'],
# ]

filename = 'data.csv'

# with open(filename, 'w', newline='') as file:
#     csv_wirter = csv.writer(file)
#     csv_wirter.writerows(data)

data2 = [
    {'Name': 'John', 'Age': 25, 'City': 'Seoul'},
    {'Name': 'James', 'Age': 23, 'City': 'Busan'},
    {'Name': 'Bob', 'Age': 24, 'City': 'Seoul'},
]

with open(filename, 'w', newline='') as file:
    # headers = ['Name', 'Age', 'City']
    headers = data2[0].keys()
    csv_wrirter = csv.DictWriter(file, fieldnames=headers)
    csv_wrirter.writeheader()
    csv_wrirter.writerows(data2)
