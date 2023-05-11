

import csv
import requests
from bs4 import BeautifulSoup
from student_id import student_id

WINDOWMODE = 1
SEMID = 2
BATCHID = 260
FROMDATE = '2023-02-15'
TODATE = '2023-05-10'
STUDENTID = student_id
PAPERID = 4834
URL_LIST = {
    student_code: f"https://www.brainwareuniversity.ac.in/univ_academics/centre-report-student-attendance-status-details.php?windowmode={WINDOWMODE}&semid={SEMID}&batchid={BATCHID}&fromdate={FROMDATE}&todate={TODATE}&studentid={student_id}&paperid={PAPERID}" for student_code, student_id in STUDENTID.items()}


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

fieldnames = ['Student_Code', 'Class', 'Date', 'Teacher',
              'Attendance Status']

with open("student.csv", 'w', newline='', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for student_code, student_attendance_url in URL_LIST.items():
        try:
            response = requests.get(student_attendance_url)
            if response.status_code != 200:
                print(
                    f'Response status code for {student_attendance_url} is {response.status_code}. Skipping...')
                continue

            soup = BeautifulSoup(response.content, 'html.parser')

            data = soup.find('table', {'id': 'report_table'})
            table = data.find_all('table')[1]

            rows = table.find_all('tr')
            header_row = rows[0]
            headers = [header.text.strip()
                       for header in header_row.find_all('td')]

            headers.insert(0, fieldnames[0])

            for row in rows[1:-1]:
                values = [value.text.strip() for value in row.find_all('td')]
                values[0] = values[0].split('->')[1].strip()
                values.insert(0, student_code)

                data_dict = dict(zip(headers, values))

                print(data_dict)
                writer.writerow(data_dict)

        except requests.exceptions.RequestException as e:
            print(
                f'Error occurred while requesting {student_attendance_url}. Error message: {str(e)}')
            continue
