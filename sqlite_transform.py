import csv
import sqlite3

import pandas as pd

conn = sqlite3.connect('Walmart_Train.db')
c = conn.cursor()  # Connection to the newly create SQlite3 database

original_train = open('raw_train.csv', 'r')
original_test = open('raw_test.csv', 'r')  # Open raw data files

df_train = pd.read_csv(original_train, keep_default_na=True,
                       error_bad_lines=False).dropna()  # Clean raw data files using pandas dataframes. Drops rows with null values
df_test = pd.read_csv(original_test, keep_default_na=True, error_bad_lines=False).dropna()

df_train.to_sql('Train', conn, if_exists='append', index=False)  # Imports the clean pandas dataframes into the database
df_test.to_sql('Test', conn, if_exists='append', index=False)

departments = ["FINANCIAL SERVICES",  # List of Walmart department names
               "SHOES",
               "PERSONAL CARE",
               "PAINT AND 2",
               "DSD GROCERY",
               "MEAT - FRESH & FROZEN",
               "DAIRY",
               "PETS AND SUPPLIES",
               "HOUSEHOLD CHEMICALS/SUPP",
               "IMPULSE MERCHANDISE",
               "PRODUCE",
               "CANDY, TOBACCO, COOKIES",
               "GROCERY DRY GOODS",
               "BOYS WEAR",
               "FABRICS AND CRAFTS",
               "JEWELRY AND SUNGLASSES",
               "MENS WEAR",
               "ACCESSORIES",
               "HOME MANAGEMENT",
               "FROZEN FOODS",
               "SERVICE DELI",
               "INFANT CONSUMABLE HARDLINES",
               "PRE PACKED DELI",
               "COOK AND DINE",
               "PHARMACY OTC",
               "LADIESWEAR",
               "COMM BREAD",
               "BAKERY",
               "HOUSEHOLD PAPER GOODS",
               "CELEBRATION",
               "HARDWARE",
               "BEAUTY",
               "AUTOMOTIVE",
               "BOOKS AND MAGAZINES",
               "SEAFOOD",
               "OFFICE SUPPLIES",
               "LAWN AND GARDEN",
               "SHEER HOSIERY",
               "WIRELESS",
               "BEDDING",
               "BATH AND SHOWER",
               "HORTICULTURE AND ACCESS",
               "HOME DECOR",
               "TOYS",
               "INFANT APPAREL",
               "LADIES SOCKS",
               "PLUS AND MATERNITY",
               "ELECTRONICS",
               "GIRLS WEAR, 4-6X  AND 7-14",
               "BRAS & SHAPEWEAR",
               "LIQUOR,WINE,BEER",
               "SLEEPWEAR/FOUNDATIONS",
               "CAMERAS AND SUPPLIES",
               "SPORTING GOODS",
               "PLAYERS AND ELECTRONICS",
               "PHARMACY RX",
               "MENSWEAR",
               "OPTICAL - FRAMES",
               "SWIMWEAR/OUTERWEAR",
               "OTHER DEPARTMENTS",
               "MEDIA AND GAMING",
               "FURNITURE",
               "OPTICAL - LENSES",
               "SEASONAL",
               "LARGE HOUSEHOLD GOODS",
               "1-HR PHOTO",
               "CONCEPT STORES",
               "HEALTH AND BEAUTY AIDS",
               "PAINT AND ACCESSORIES"]

num1 = range(1, 8)  # Numbers to encode days of the week as integers instead
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for x, y in zip(num1, days):  # Replaces days of the week with numbers in database
    c.execute('UPDATE TRAIN SET Weekday = ? WHERE Weekday = ?', (x, y))
    c.execute('UPDATE TEST SET Weekday = ? WHERE Weekday = ?', (x, y))
    conn.commit()

num2 = range(1, 70)
for x, y in zip(num2, departments):  # Replaces department with encoded number in database
    c.execute('UPDATE TRAIN SET DepartmentDescription = ? WHERE DepartmentDescription = ?', (x, y))
    c.execute('UPDATE TEST SET DepartmentDescription = ? WHERE DepartmentDescription = ?', (x, y))
    conn.commit()

with open('train_ml.csv', 'w') as f:  # Export a cleaned .csv data file from the database
    train = c.execute('SELECT * FROM Train')
    writer = csv.writer(f)
    writer.writerow(
            ['TripType', 'VisitNumber', 'Weekday', 'Upc', 'ScanCount', 'DepartmentDescription', 'FinelineNumber'])
    writer.writerows(train)

with open('test_ml.csv', 'w') as f1:
    test = c.execute('SELECT * FROM Test')
    writer = csv.writer(f1)
    writer.writerow(['VisitNumber', 'Weekday', 'Upc', 'ScanCount', 'DepartmentDescription', 'FinelineNumber'])
    writer.writerows(test)

original_test.close()
original_train.close()
