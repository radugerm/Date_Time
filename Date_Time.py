import datetime

import Ordinal_Numbers


def get_time():
    dates = input("How much data do you want to enter? ")
    count = 0
    th = Ordinal_Numbers.th
    while count <int(dates):
        try:

            date_entry = input('Enter a date in YYYY.MM.DD format: ')
            year, month, day = map(int, date_entry.split('.'))
            date = datetime.date(year, month, day)

            time = input("Enter time in HH:MM ")
            hour, min,  = map(int, time.split(":"))

            print("Thank you very much. I will notify them!")

            YEAR = datetime.date.today().year
            MONTH = datetime.date.today().month
            DATE = datetime.date.today().day
            HOUR = datetime.datetime.now().hour
            MINUTE = datetime.datetime.now().minute

            first_date= datetime.datetime(year, month, day, hour,min)
            second_date =datetime.datetime(YEAR,MONTH,DATE,HOUR,MINUTE)


            if first_date <= second_date:

                print("count=" ,count)
                return (f"The {th[count]} date has been reached! {first_date} now it's {second_date}")
            count +=1



        except:
            return ("Something you did wrong, pay attention to the format and type")
        count +=1
        count -= 1


print(get_time())










