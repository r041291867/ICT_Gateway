#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import sys
import configparser
from flask_restful import Resource, Api
from datetime import date,datetime as dt, timedelta 
import io
import pymysql
import logging
import re
import textwrap
import requests
import time
import numpy as np 
import traceback
from decimal import * 
import json

class Common(Resource):

    def BeforeNWeekDate(weeknum):
       # 取得今日星期幾
        wday=int(time.strftime("%w",time.localtime()))

        # 取得上週日日期後再往前推週數*7天就是n週前的星期日
        beforendays=weeknum*7
        after_enddate=(dt.now()-timedelta(days=wday))-timedelta(days=beforendays)
        return(after_enddate.strftime("%Y-%m-%d"))