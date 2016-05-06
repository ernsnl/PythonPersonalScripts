import threading
import praw
import time
import datetime


def beginProcess(fileName):
    redditFile  = open(fileName, "r")
    subReddits = redditFile.readlines()
    threads = []
    for content in subReddits:
        threadObj = threading.Thread(target=BeginReddit, args=[content])
        threads.append(threadObj)

    for thread in threads:
        thread.start()
        thread.join()

    redditFile.close()
    print("Done")

def BeginReddit(args):
    subreddit = args.split(' ')[0]
    print(subreddit)
    howLong = args.split(' ')[1]
    sleepTime = sleepDuration(int(howLong))
    user_agent = "PersonalScrapping by /u/ernsnl"
    after_param = ""
    while(True):
        r = praw.Reddit(user_agent=user_agent)
        submissions = r.get_subreddit(subreddit_name=subreddit).get_hot(limit=25, params={"after": after_param})
        outputFile = open(subreddit+ "_" + str(datetime.datetime.today().day)+
                          "_" + str(datetime.datetime.today().month)+
                          "_" + str(datetime.datetime.today().year) +
                          "_" + str(datetime.datetime.today().hour) +
                          "_" + str(datetime.datetime.today().minute) +".txt", "w")
        for x in submissions:
            outputFile.write("Title: " + x.title + "\n" + "Url: "+ x.url + '\n')
            after_param = "t3_" + x.id
        print(after_param)
        outputFile.close()
        time.sleep(sleepTime)



def sleepDuration(x):
    return {
        0: 1, # Every Second
        1: 60, # Every Minute
        2: 60 * 60, # Every Hour
        3: 60 * 60 * 24, # Every Day
        4: 60 * 60 * 24 * 7, # Every Week
        5: 60 * 60 * 24 * 30, # Every Month
        6: 60 * 60 * 24 * 365 # Every Year
    }[x]

beginProcess("PythonBrowsingInfo.txt")# Your Text File Comes Here




