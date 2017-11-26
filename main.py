#/usr/bin/env python
# -*- python: utf-8 -*-

import requests
import json
import pymongo
from config import *
from requests import RequestException

clinet = pymongo.MongoClient(MONGO_URL,connect=False)
db = clinet[MONGO_DB]

def GET_JSON_DATA(start_url):

    try:
        r = requests.get(start_url,headers=headers).text
    except RequestException as e :
        raise e

    return json.loads(r)

def GET_DATA_FROM_JSON(Json):

    url_list = []
    Art_number = []
    for data in Json:

        url = data['url']
        number = data['postsCount']
        url_list.append(url)
        Art_number.append(number)
    return url_list,Art_number

def GET_TITLE(Json):
    title_list = []
    LikesCount = []

    for data in Json:
        title_list.append(data['title'])
        LikesCount.append(data['likesCount'])
    List = dict(zip(title_list,LikesCount))
    print(List)
    Save_to_Mongo(List)


def Save_to_Mongo(List):
    try:
        if db[MONGO_TABLE].insert(List):
            print("插入成功！")
    except Exception:
        pass

def main():

    Data = GET_JSON_DATA(start_url)
    url_data, num_data = GET_DATA_FROM_JSON(Data)
    num_data = [((i / 10 + 0.5) * 10) // 10 for i in num_data]
    for i in range(8):
        for index in range(1, int(num_data[i])):
            base_url = 'https://zhuanlan.zhihu.com/api/columns{}/posts?limit=20&offset={}'.format(url_data[i],
                                                                                                  index * 10)
            print(base_url)
            D = GET_JSON_DATA(base_url)
            GET_TITLE(D)



if __name__ == '__main__':
    for i in range(4):
        main()



