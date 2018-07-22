# -*-coding:utf-8-*-
"""
"""
from pymongo import MongoClient
import datetime
import requests
import os

def data_save_info(datas):
    # conn = MongoClient('192.168.235.55', port=27017)
    # db = conn['admin']
    # db.authenticate("admin", "123456")
    # db = conn['team_behind_sc']
    # table = db['Filmmaker_page']
    # table.insert(datas)
    conn = MongoClient()
    db = conn.mydb
    db.col.insert(datas)

def data_save_company(datas):
    # conn = MongoClient('192.168.235.55', port=27017)
    # db = conn['admin']
    # db.authenticate("admin", "123456")
    # db = conn['team_behind_sc']
    # table = db['Film_company']
    # table.insert(datas)
    conn = MongoClient()
    db = conn.mydb
    db.col.insert(datas)

if __name__ == '__main__':
    datas = None
    data_save_info(datas)
    data_save_company(datas)