# This is an attempt to check the daily deal on audible
# and then see if it is a book I want (or would like)
# and then email me the link, description and price.
# I'll have to figure out:
#
# 1. how to navigate a website with selenium (and then click a link)
# 2. scrape certain information and compare it to ... list of books I want/genres/authors I like
# 3. cron job (win equiv) to have it run once a day in the background
# 4. send the email with all of the information.
#

import smtplib, ssl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv
import re
import requests

# all login information
login_info = open('login_information.txt').read().splitlines()

username, aud_pwd, gmail, gmail_pwd = login_info

# starting the web browser
driver = webdriver.Chrome(r'C:/Users/Justine/Downloads/chromedriver_win32/chromedriver.exe')
driver.get("https://www.audible.com")

# logging into audible
sign_in_link = driver.find_element_by_class_name('ui-it-sign-in-link')
sign_in_link.click()

si_username = driver.find_element_by_partial_link_text('username')
si_username.click()

logging_in = driver.find_element_by_id('ap_email')
logging_in.send_keys(username)
logging_in = driver.find_element_by_id('ap_password')
logging_in.send_keys(aud_pwd)
logging_in.send_keys(Keys.RETURN)

# navigating to the daily deal
daily_deal = driver.find_element_by_partial_link_text('DAILY DEAL')
daily_deal.click()
dd_url = driver.current_url

# source code as text
# dd_source = requests.get(dd_url).text
# this is wrong -- if only because you HAVE to be logged in to get the correct PRICE information

content = driver.find_element_by_xpath('//*') 
daily_soup = BeautifulSoup(content.get_attribute('innerHTML'), "lxml")

csv_file = open('audible_dd.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Author', 'Genre 1', 'Genre 2', 'Cost'])

genre, genre2, author, title, price = '', '', '', '', ''

for data in daily_soup.find_all('div', id='center-1'):
    # genre
    fd_genre = data.find('nav').a
    genre = fd_genre.text
    genre2 = fd_genre.find_next('a').text
    print(genre)
    print(genre2)

    # Title, author
    title = data.find('li', class_='bc-list-item').h1.text
    print(title)

    author = data.find('li', class_='authorLabel').a.text
    print(author)

    # Price
    price = data.find('div', id='adbl-primary-button-area').div.span.button.span.text
    price = price.strip()[-4:] # need to strip first, then slice; too much damn white space.
    print(price)

    csv_writer.writerow([title, author, genre, genre2, price])

csv_file.close()
# So.. after getting the csv file set up and coded in.. I go to bed, and fucking gestalt moment of I didn't even have to do this!

# Todo compare the items from above to items in files (author.txt title.txt genre.txt); also set it up to email if price is below x.xx

# with open('author.txt', 'r') as watch_list:
#     for line in watch_list:
#         line = line.split('\\n')
#         line[0] = line[0].strip()
#         if line[0] == author:
#             print("This works?") # this does work, figure out more for why and how to simplify bc that's a lot of lines; I tried splitting, but not stripping so maybe try that too

def compare_info(item, file):
    with open(file, 'r') as watch_list:
        for line in watch_list:
            line = line.split('\\n')
            line[0] = line[0].strip()
            if line[0] == item:
                print("Alrighty this works now I need to set it up to send an email.")

compare_info(author, 'author.txt')
compare_info(genre2, 'genre.txt')
compare_info(title, 'title.txt')

# todo email the final 'results'

