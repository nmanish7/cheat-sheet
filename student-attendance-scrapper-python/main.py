import csv
import requests
from bs4 import BeautifulSoup

WINDOWMODE = 1
SEMID = 2
BATCHID = 262
FROMDATE = '2023-02-15'
TODATE = '2023-04-28'
STUDENTID = 14951
PAPERID = [
    4753,
    4825,
    4828,
    4831,
    4834,
    5587,
    5590
]

URL_LIST = [
    f"https://www.brainwareuniversity.ac.in/univ_academics/centre-report-student-attendance-status-details.php?windowmode={WINDOWMODE}&semid={SEMID}&batchid={BATCHID}&fromdate={FROMDATE}&todate={TODATE}&studentid={STUDENTID}&paperid={paperid}" for paperid in PAPERID]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
# URL_LIST = []
# for URL in URL_LIST:

#     response = requests.get(URL, headers=headers)

#     soup = BeautifulSoup(response.content, 'html.parser')

#     data = soup.find('table', {'id': 'report_table'})
#     table = data.find_all('table')[1]

#     rows = table.find_all('tr')
#     header_row = rows[0]
#     headers = [header.text.strip() for header in header_row.find_all('td')]

#     data_dict = {}

#     fieldnames = ['Class', 'Date', 'Teacher', 'Attendance Status']
#     with open("student.csv", 'a', newline='') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()

#         for row in rows[1:-1]:
#             values = [value.text.strip() for value in row.find_all('td')]
#             values[0] = values[0].split('->')[1].strip()
#             data = dict(zip(headers, values))
#             data_dict.update(data)

#             print(data_dict)
#             writer.writerow(data_dict)


# import requests
# from bs4 import BeautifulSoup
# import csv

# URL_LIST = ['url1', 'url2', 'url3']
fieldnames = ['Class', 'Date', 'Teacher', 'Attendance Status']

with open("student.csv", 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for URL in URL_LIST:
        try:
            response = requests.get(URL)
            if response.status_code != 200:
                print(
                    f'Response status code for {URL} is {response.status_code}. Skipping...')
                continue

            soup = BeautifulSoup(response.content, 'html.parser')

            data = soup.find('table', {'id': 'report_table'})
            table = data.find_all('table')[1]

            rows = table.find_all('tr')
            header_row = rows[0]
            headers = [header.text.strip()
                       for header in header_row.find_all('td')]

            for row in rows[1:-1]:
                values = [value.text.strip() for value in row.find_all('td')]
                values[0] = values[0].split('->')[1].strip()
                data_dict = dict(zip(headers, values))

                print(data_dict)
                writer.writerow(data_dict)

        except requests.exceptions.RequestException as e:
            print(
                f'Error occurred while requesting {URL}. Error message: {str(e)}')
            continue
