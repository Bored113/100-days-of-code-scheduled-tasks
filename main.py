##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import pandas
import random
import os

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")

# Turn csv data into a dictionary
df = pandas.read_csv('birthdays.csv')
email_dict = df.to_dict(orient='records')
# print(email_dict)

# Extract letter templates
letters = []
for i in range(3):
    with open(f'letter_templates/letter_{i + 1}.txt', "r") as text:
        letter = text.read()
        letters.append(letter)
# print(letters)

# Extract today's month and date
now = dt.datetime.now()
today_month = now.month
today_day = now.day


# Loop through email list and find people whose birthday is "today"
for person in email_dict:
    if person['month'] == today_month and person['day'] == today_day:
        message = random.choice(letters)
        merged_message = message.replace('[NAME]', person['name'])
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person['email'],
                msg=f'Subject:Happy Birthday!\n\n{merged_message}'
            )
