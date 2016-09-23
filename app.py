from flask import Flask, render_template
import csv, random

app = Flask(__name__)

occupations = {}
randjob = ""

with open('occupations.csv','r') as csvfile:
    words = csv.reader(csvfile)
    for row in words:
        if row[0] != "Job Class" and row[0] != "Total":
            occupations[row[0]] = float(row[1])

randplace = random.random()*100
curplace = 0.0
for job in occupations:
    percentage = occupations[job]
    if curplace >= randplace:
        randjob = job
        break
    curplace += percentage

@app.route("/occupations")
def randomoccup():
    return render_template('whatjob.html',title="Occupations",collection=occupations,job = randjob)

if __name__ == "__main__":
    app.debug = True
    app.run()
