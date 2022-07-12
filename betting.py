#Python
import http.client
import json
import yaml
from flask import Flask, render_template,request
from sml import leagues,teams_info,result,MoneyLine
app = Flask(__name__)
@app.route('/')
def index():
 return render_template('index.html', foobar=leagues)
@app.route('/teams',methods=['POST','GET'])
def teams():
    results=dict()
    datefrom='2022-01-01'
    dateto='2022-06-01'
    teams_name ,teams_address ,teams_ids=teams_info(leagues[int(request.form["name_input"])])
    HeadToHead,odds = MoneyLine(leagues[int(request.form["name_input"])],request.form["match_input"])

    for i,v in teams_ids.items():
         results[i]=result(v,datefrom,dateto) 
    return render_template('base.html', foobar=teams_ids,coobar=results,matches=HeadToHead,odd=odds)
if __name__ == '__main__':
 app.run(debug=True)  