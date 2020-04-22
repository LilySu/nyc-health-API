from flask import Flask
from flask import jsonify
import pandas as pd
import markdown
import requests
import os


app = Flask(__name__)

@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) + '/README.md','r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)

@app.route("/boro")
def boro():
    df = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/boro.csv')
    df.fillna(0, inplace=True)
    return jsonify(df.to_dict('records')),200

@app.route("/by-age")
def byage():
    df = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/by-age.csv')
    df.fillna(0, inplace=True)
    return jsonify(df.to_dict('records')),200

@app.route("/by-sex")
def bysex():
    df = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/by-sex.csv')
    df.fillna(0, inplace=True)
    return jsonify(df.to_dict('records')),200

@app.route("/case-hosp-death")
def casehospdeath():
    df = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/case-hosp-death.csv')
    df.fillna(0, inplace=True)
    return jsonify(df.to_dict('records')),200

@app.route("/probable-confirmed-dod")
def probableconfirmeddod():
    df = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/probable-confirmed-dod.csv')
    df.fillna(0, inplace=True)
    return jsonify(df.to_dict('records')),200

@app.route("/summary")
def summary():
    df = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/summary.csv')
    df.fillna(0, inplace=True)
    return jsonify(df.to_dict('records')),200

@app.route("/tests-by-zcta")
def testsbyzcta():
    df = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/tests-by-zcta.csv')
    df.fillna(0, inplace=True)
    return jsonify(df.to_dict('records')),200