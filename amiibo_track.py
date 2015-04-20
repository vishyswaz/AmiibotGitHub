# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:39:10 2015

@author: Vishal
"""
import time
import praw
import os
import sys

max_links = 10

def contains(link):
    return link in marked
    
def push(link):
    if len(marked) > max_links:
        marked.pop(0)
    marked.append(link)

def login(r,user,pw):
    r.login(user,pw)
    print "logging into bot account"
    
def hasNotable(title):
    return ("go" in title or "available" in title or "order" in title or "instock" in title
                or "up" in title or "has" in title or "@" in title or "at" in title)
    
def track(r):
    while True:
        print "retrieving subreddit..."
        sub = r.get_subreddit('amiibo')
        print "retrieving submissions..."
        for submission in sub.get_new(limit=10):
            for key, bro in tracking.iteritems():
                print "Checking title of post for "+bro
                title = submission.title.lower().replace(" ","")
                link = submission.permalink
                if key in title and hasNotable(title):
                    if not contains(link):
                        r.send_message('viciouspenguincookie','Amiibo Notification!',bro + " might be available! \n\n" + link)
                        print "Notified user"                    
                        push(link) 
                        time.sleep(2)                
        print "Sleeping..."
        time.sleep(60*2)

r = praw.Reddit(user_agent='/r/amiibo tracking 0.4 by /u/viciouspenguincookie')
print "reddit object initiated"
tracking = {'lucina':'Lucina','pac':'Pac Man','pac-man':'Pac Man','robin':'Robin','falcon':'Captain Falcon',
            'jiggly':'Jigglypuff','ness':'Ness','wave4':'Wave 4','splatoon':'Splatoon','inkling':'Splatoon','marth':'Marth'}

username = os.getenv('BOTNAME','None')
password = os.getenv('BOTPASS','None')

marked = []

if username is 'None' or password is 'None':
    print "Environment variables not set"
    print sys.prefix
    sys.exit()
else:
    login(r,username,password)
    track(r)
    



