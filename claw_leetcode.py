#-*- coding=utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import string

origin_url = "https://leetcode.com/"
question_list_page = "problemset/algorithms"

s = requests.Session()

def fetch_problem_url():
    r = s.get(origin_url + question_list_page)
    soup = BeautifulSoup(r.text, "lxml")
    pre_sibling = soup.find("div", id = "cong", class_ = "hide container")
    ex_container = pre_sibling.find_next_sibling("div", class_ = "container")
    ex_list = ex_container.find("table", id = "problemList").find("tbody")
    only_once = True
    for child in ex_list.find_all("tr"):
        if(only_once):
            ex_url = child.find("a")['href']
            print ex_url
            only_once = False

if __name__ == "__main__":
    fetch_problem_url()


