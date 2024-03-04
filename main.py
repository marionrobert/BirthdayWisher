##################### Normal Starting Project ######################
import datetime as dt
import pandas
import smtplib

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
now = dt.datetime.now()
today = (now.month, now.day)
print("today -->", today)
import random
import os

# HINT 2: Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")
# print(data)

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
birthdays_dict = {(data_row.month, data_row.day):data_row for (index, data_row) in data.iterrows()}
# print("birthday_dict -->", birthdays_dict)

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today in birthdays_dict:
    # If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        letter = letter_file.read()
        letter_with_name = letter.replace("[NAME]", birthday_person["name"])

    # Send the letter generated in step 3 to that person's email address.
    MY_EMAIL = os.environ["MY_EMAIL"]
    GMAIL_SERVER = "smtp.gmail.com"
    MY_PASSWORD = os.environ["MY_PASSWORD"]

    with smtplib.SMTP(GMAIL_SERVER, 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Open it!\n\n{letter_with_name}")




