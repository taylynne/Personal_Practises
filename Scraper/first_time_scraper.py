# Name / title says it all.
# really wasn't sure where to scrape at tho tbh

from bs4 import BeautifulSoup
import requests
import csv

# gets source code, as text
source = requests.get('https://stackoverflow.com/questions/tagged/python').text # add .txt to get source file from response obj

soup = BeautifulSoup(source, 'lxml')

csv_file = open('stack_questions.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Questions", "Summary", "Link", "Number_of_Answers",])

for base in soup.find_all('div', class_='question-summary'):
    inquiry = base.h3.a.text
    print(inquiry)

    i_summary = base.find('div', class_='excerpt').text
    i_summary = i_summary.strip()
    print(i_summary)

    # this will need to be revised with "https://stackoverflow.com"
    i_link = base.h3.a['href']
    i_link = "https://stackoverflow.com" + i_link
    print(i_link)

    try:
        # depending on if the question has any answers, the class changes. @.@
        num_answers = base.find('div', class_='status unanswered').text
    except Exception as e:
        try:
            num_answers = base.find('div', class_='status answered').text
        except Exception as e: # BUT OFC I FOUND ANOTHER DAMNABLE CLASS. WHY.
            num_answers = base.find('div', class_='status answered-accepted').text
    num_answers = num_answers[:2] + " " + num_answers[2:]

    print(num_answers)

    print("")

    csv_writer.writerow([inquiry, i_summary, i_link, num_answers])

csv_file.close()
