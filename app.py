from flask import Flask, render_template
from utils import randomoccupoto

app = Flask(__name__)
 
 
@app.route("/occupations")
def randomoccup():
    dict = randomoccupoto.jobs()
    randjob = randomoccupoto.selectOccupation()
    return render_template('whatjob.html',title="Occupations",collection=dict,job = randjob)

if __name__ == "__main__":
    app.debug = True
    app.run()
