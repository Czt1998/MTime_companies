# codeing utf-8
import sys
from imp import reload
reload(sys)

def main():
    years = [2010,2011,2012,2013,2014,2015,2016,2017]
    for year in years:
        with open(year + ".txt","r")as f:
