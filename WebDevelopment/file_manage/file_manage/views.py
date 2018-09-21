#coding:utf-8

"""
desc:文件管理相关视图函数
author:Yabea
date:2018-06-25
"""

from flask import render_template, request, redirect, jsonify, url_for, session, Blueprint
from sqlalchemy.sql import or_

from flask import jsonify
from flask import current_app as app, render_template, request, redirect, abort, jsonify, url_for, session, Blueprint, \
    Response, send_file
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

views = Blueprint('views', __name__)

@views.route('/')
def homepage():
    return render_template('homepage.html')
