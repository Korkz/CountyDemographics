from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json 

app = Flask(__name__)

@app.route("/")
def render_index():
    return render_template('index.html', options=get_state_options())

@app.route("/response")
def render_response():
    state = request.args['state']
    return render_template('response.html', options = get_state_options(), funFact = fun_fact_by_state(state))
    
def get_state_options():
    listOfStates = []
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    for county in counties:
        if not(county["State"] in listOfStates):
            listOfStates.append(county["State"])
    options = ""
    for s in listOfStates:
        options = options + Markup("<option value=\"" + s + "\">" + s + "</option>")
    return options 

def fun_fact_by_state(state):
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    most=0
    most_county = "empty"
    for x in counties:
        if x["State"] == state:
            under_18 = x["Age"]["Percent Under 18 Years"]
            if under_18 > most:
                most = under_18
                most_county = x["County"]
        
         #    occupied = x["Housing"]["Households"] / x["Housing"]["Housing Units"]
#             occupied = occupied * 100.00 
#             if occupied > highest:
#                 highest = occupied
#                 highCounty = x["County"]
#             elif occupied == 0:
#     	        lowest = lowest
#             elif occupied < lowest:
#                 lowest = occupied
#                 lowCounty = x["County"]
#         highest = round(highest, 2)
#         lowest = round(lowest, 2)
    	
    return "The county with the highest percent of under 18 year olds is " + most_county + " with " + str(most) + "%" 

                                   
if __name__=="__main__":
    app.run(debug=false)
