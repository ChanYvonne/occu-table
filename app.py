from flask import Flask, render_template
import csv, random

app = Flask(__name__)

occupations = {}


total_percentage = None # They don't quite add to 100%

with open('data/occupations.csv','r') as csvfile:
    words = csv.reader(csvfile)
    for row in words:
        if row[0] == "Total":
            total_percentage = float(row[1])
        elif row[0] != "Job Class":
            # "Job Class" is the first row, with only headings
            occupations[row[0]] = [float(row[1]),str(row[2])]


            
def selectOccupation():
    randplace = random.random() * total_percentage
    curplace = 0.0
    last_job = None
    for job in occupations:
        curplace += occupations[job][0]
        last_job = job
        if curplace >= randplace:
            return job
    
    # This code is virtually never reached (at least not in millions of cases)
    # But if it does due to the selection of `randplace` and floating point
    # imprecision, just return a random job
    return random.choice(occupations.keys())


@app.route("/occupations")
def randomoccup():
    return render_template('whatjob.html',title="Occupations",collection=occupations,job = selectOccupation())

if __name__ == "__main__":
    app.debug = True
    app.run()
