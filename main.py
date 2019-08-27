# Main method to run the program on loop
# usage is following

# email(Item_Name, Min_Price, Max_Price, Sender_Email, Receiver_Email, Sender_Password)
# All param are Strings
import emailing
import time
# import scraper as scraper

from apscheduler.schedulers.blocking import BlockingScheduler

# end time should be after 2 days so 2 * 86400 = 172,800 seconds
day = 86400

# end = time.time() + (2 * day)
# for testing we can use 20 seconds total time before ending for end time
end = time.time() + 20

sched = BlockingScheduler()
id_list = []

# for testing lets use interval seconds as 5
@sched.scheduled_job('interval', seconds=5)
def timed_job():
    emailing.email("iphone x", "600", "800", id_list, "kijiji.bot.alert@gmail.com", input("Enter your email: "),
                   input("Enter sending email password: "))

    #   items_list = scraper.scraper("iphone x", "600", "900", id_list)
    #   for item in items_list:
    #       print(item.title)

    print(time.time())
    print(end)
    if time.time() > end:
        for ids in id_list:
            print(ids)
        sched.shutdown(wait=False)


sched.start()
