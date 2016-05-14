#!/bin/sh
npm install
bower install
pip install -r requirements.txt
grunt dist
