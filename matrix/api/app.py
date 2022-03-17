# -*- coding: utf-8 -*-
"""
@Time    : 2022/3/17 15:01
@Author  : zhou_yihe
@File    : app.py
@Software: PyCharm
@Describe:
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
