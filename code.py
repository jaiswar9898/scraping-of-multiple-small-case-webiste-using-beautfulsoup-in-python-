from itertools import count
from turtle import title
from bs4 import BeautifulSoup as bs
import requests
import  pandas as pd
import csv
import re 
from collections import OrderedDict 

count = 1
titles = []
manages=[]
while count != 700:
      url = f"https://www.smallcase.com/discover/all?count={count}"
      response = requests.get(url)
      html = response.content
      soup = bs(html, "lxml")
      for h2 in soup.find_all("h2", class_="SmallcaseCard__title__2M7E_ ellipsis mr8 SmallcaseCard__size-auto__NxnIC"):
            titles.append(h2.get_text(strip=True))
      aT = titles
      mylist = list(OrderedDict.fromkeys(aT)) 
      # print(mylist)
      # print(len(mylist))
      for h3 in soup.find_all("span", class_="SmallcaseCard__hide-on-larger-size__1cICV SmallcaseCard__size-auto__NxnIC MetaData__managers-name__2RV67 text-light MetaData__text-13-mobile__2_k-R"):
            manages.append(h3.get_text(strip=True))
      aM = manages
      mylistManagers = list(OrderedDict.fromkeys(aM)) 
      print(mylistManagers)
      print(len(mylistManagers))
      count = count + 1







indeed = pd.DataFrame({
# 'Titles': mylist,
'Managed By': mylistManagers,
})


#add dataframe to csv file named 'movies.csv'
indeed.to_csv('indeed.csv')