# import pandas as pd
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, wait
from csv import *
import csv
import datetime

#D2 - old code
def aapl_filse(path):
    counter = 0
    vol = []
    high_price = []
    low_price = []
    line_in_csv = []
    with open(path) as csv_file:
        reader = DictReader(csv_file)

        for item in reader:
            # Inserts the date of each row
            date = item['Date']
            date = datetime.datetime.strptime(date, "%d-%m-%Y")

            # enter the first year in variable
            if counter == 0:
                date_year = date.year

            if date.year == date_year:
                vol.append(float(item['Volume']))
                high_price.append(float(item['High']))
                low_price.append(float(item['Low']))
                counter = 1
            else:
                # When we come to a new year, we enter all the details and reset the variables for the next year
                line_in_csv.append({'Year': date_year,
                                    'Avg Price': (sum(high_price) + sum(low_price)) / (
                                            len(high_price) + len(low_price)),
                                    'Min Price': min(low_price), 'Max Price': max(high_price),
                                    'Avg Volume': sum(vol) / len(vol), 'Min Volume': min(vol), 'Max Volume': max(vol)})
                high_price = []
                low_price = []
                vol = []
                date_year = date.year

    with open('C:\\Users\\user\\Desktop\\eduprojects\\ebook\\aple2.csv', "w") as csv_f:
        writer = csv.DictWriter(csv_f, ['Year', 'Avg Price', 'Min Price', 'Max Price', 'Avg Volume',
                                        'Min Volume', 'Max Volume'])
        writer.writeheader()
        for row in line_in_csv:
            writer.writerow(row)


# # E 5
def aple(path):
    with open(path) as csv_file:
        reader = DictReader(csv_file)
        counter = 0
        line_in_csv = {}
        for item in reader:
            date = item['Date']
            date = datetime.datetime.strptime(date, "%d-%m-%Y")
            if date.year not in line_in_csv.keys():
                line_in_csv[date.year] = []
            line_in_csv[date.year].append(item)
        return line_in_csv

def aple2(year_dict: list[dict], year):
    with open(f'C:\\Users\\user\\Desktop\\eduprojects\\ebook\\allyears\\AAPL_{year}.csv', "w") as f:
        writer = csv.DictWriter(f, ['Date', 'Low', 'Open', 'Volume', 'High', 'Close', 'Adjusted Close'])
        writer.writeheader()
        for row in year_dict:
            writer.writerow(row)
    # with open(f'C:\\Users\\user\\Desktop\\eduprojects\\ebook\\allyears\\AAPL_{year}.csv',"r") as df:
    #     df = pd.read_csv(df)
    #     Date = "Avg"
    #     Low = df['Low'].mean()
    #     Open = df['Open'].mean()
    #     Volume = df['Volume'].mean()
    #     High = df['High'].mean()
    #     Close = df['Close'].mean()
    #     Adjusted =df['Adjusted Close'].mean()
    #     with open(f'C:\\Users\\user\\Desktop\\eduprojects\\ebook\\allyears\\AAPL_{year}.csv', "a") as f:
    #         writer_mean = csv.writer(f)
    #         writer_mean.writerow([Date,Low, Open, Volume, High, Close, Adjusted])
        f.close()

if __name__ == '__main__':
    start = datetime.datetime.utcnow()
    by_year = aple('C:\\Users\\user\\Desktop\\eduprojects\\ebook\\aple.csv')
    executor = ThreadPoolExecutor(max_workers=36)
    futures = []
    for year in by_year:
        future = executor.submit(aple2, by_year[year], year)
        futures.append(future)

    done, not_done = wait(futures,return_when= concurrent.futures.ALL_COMPLETED)
    print(f"done: {len(done)}")
    print(f"not done: {len(not_done)}")
    end = datetime.datetime.utcnow()
    print(f"Time took for several: {(end - start).total_seconds()}s---------------------------------------")

