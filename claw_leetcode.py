#-*- coding=utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import string
import os

origin_url = "https://leetcode.com"
question_list_page = "/problemset/algorithms"

s = requests.Session()
qs = requests.Session()

def fetch_problem_content_and_write_to_file(child):
    ex_url_tag = child.find("a")
    ex_url = ex_url_tag['href']
    ex_name = ex_url_tag.text               #题目名
    ex_new_name = '-'.join(ex_name.split(' '))
    td_list = child.find_all("td")
    ex_num = td_list[1].text                #题目题号
    ex_difficulty = td_list[4].text         #题目难度

    qr = qs.get(origin_url + ex_url)
    qsoup = BeautifulSoup(qr.text, "lxml")
    qUntilDesc = qsoup.find_all("meta", limit = 3)
    print qUntilDesc[2]['content']

    exfilename = ex_num.zfill(3) + '-' + ex_new_name + ".txt"
    if(ex_difficulty == "Easy"):
        ex_output = open("./LEETCODE_EASY/" + exfilename, "w")
    elif(ex_difficulty == "Medium"):
        ex_output = open("./LEETCODE_MEDIUM/" + exfilename, "w")
    elif(ex_difficulty == "Hard"):
        ex_output = open("./LEETCODE_HARD/" + exfilename, "w")
    ex_output.write(qUntilDesc[2]['content'])
    ex_output.close()




def fetch_problem_url():
    if(not os.path.exists("./LEETCODE_EASY/")):
        os.makedirs("./LEETCODE_EASY/")
    if(not os.path.exists("./LEETCODE_MEDIUM/")):
        os.makedirs("./LEETCODE_MEDIUM/")
    if(not os.path.exists("./LEETCODE_HARD/")):
        os.makedirs("./LEETCODE_HARD/")
    
    r = s.get(origin_url + question_list_page)
    soup = BeautifulSoup(r.text, "lxml")
    pre_sibling = soup.find("div", id = "cong", class_ = "hide container")
    ex_container = pre_sibling.find_next_sibling("div", class_ = "container")
    ex_list = ex_container.find("table", id = "problemList").find("tbody")
    only_once = True
    for child in ex_list.find_all("tr"):
        if(only_once):
            fetch_problem_content_and_write_to_file(child)
            only_once = False

if __name__ == "__main__":
    fetch_problem_url()


