import schedule
import time

def show_text():
    print("Hi.")
    print("I am running a code every 5 seconds.")

schedule.every(5).seconds.do(show_text)

while 1:
    schedule.run_pending()
    time.sleep(1)
