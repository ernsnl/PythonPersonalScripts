import threading
import praw
import time
import datetime
import os


def beginProcess(fileName):
    redditFile  = open(fileName, "r")
    subReddits = redditFile.readlines()
    threads = []
    for content in subReddits:
        threadObj = threading.Thread(target=BeginReddit, args=[content])
        threadObj.start()
        threads.append(threadObj)

    for thread in threads:
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
        submissions = r.get_subreddit(subreddit_name=subreddit).get_hot(limit=25, params={"before": after_param})
        if(peek(submissions)):
            if not os.path.exists("D:\\Projects\\PyhtonBrowsing\\main\\RedditBrowsing\\" + subreddit):
                 os.mkdir("D:\\Projects\\PyhtonBrowsing\\main\\RedditBrowsing\\" + subreddit)
            outputFile = open(os.path.join("D:\\Projects\\PyhtonBrowsing\\main\\RedditBrowsing\\"+ subreddit + "\\" +subreddit+ "_" + str(datetime.datetime.today().day)+
                              "_" + str(datetime.datetime.today().month)+
                              "_" + str(datetime.datetime.today().year) +
                              "_" + str(datetime.datetime.today().hour) +
                              "_" + str(datetime.datetime.today().minute) +".txt"), "w")
            after_param = ""
            for x in submissions:
                if(after_param == ""):
                    after_param = "t3_" + x.id
                outputFile.write("Title: " + x.title + "\n" + "Url: "+ x.url + '\n')
            outputFile.close()
        time.sleep(sleepTime)

def peek(iterable):
    try:
        first = next(iterable)
    except StopIteration:
        return False
    return True

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

beginProcess("D:\\Projects\\PyhtonBrowsing\\main\\RedditBrowsing\\PythonBrowsingInfo.txt")# Your Text File Comes Here




