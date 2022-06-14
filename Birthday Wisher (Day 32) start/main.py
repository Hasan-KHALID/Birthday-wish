# import smtplib
#
# my_email = "testpro0987@gmail.com"
# password = "Khasan0007"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="testpro0987@yahoo.com",
#                         msg="Subject:hello\n\nthis the body")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
#
# print(year)
#
# date_of_birth = dt.datetime(year= , )

import smtplib
import datetime as dt
import random

MY_EMAIL = "testpro0987@gmail.com"
MY_PASSWORD = "Khasan0007"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readline()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Sunday "
                                                                       f"Motibation\n\n{quote}")

