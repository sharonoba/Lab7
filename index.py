# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 21:36:47 2023

@author: SOba
"""

from flask import render_template
from flask.views import MethodView
import gbmodel

class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()
        entries = [dict(name=row[0], code=row[1], floor=row[2], room=row[3], rating=row[4] ) for row in model.select()]
        return render_template('index.html',entries=entries)