# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 21:44:37 2023

@author: SOba
"""

from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Remove(MethodView):
    def get(self):
        return render_template('index.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.remove(request.form['name'], request.form['code'], request.form['floor'], request.form['room'], request.form['rating'])
        return redirect(url_for('index'))