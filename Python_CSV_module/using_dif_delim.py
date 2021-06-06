# SangTengkorak
import csv

# with open('quote_wrapping.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)} : ')
#             line_count += 1
#         print(f'\t{row["name"]} works in {row["address"]}, and was born in {row["date joined"]}.')
#         line_count += 1
#     print(f'Processed {line_count} lines.')

with open('escape_char.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',', escapechar='|')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)} : ')
            line_count += 1
        print(f'\t{row["name"]} works in {row["address"]}, and was born in {row["date joined"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')