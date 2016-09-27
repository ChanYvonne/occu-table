from flask import Flask, render_template
from utils import randomoccupoto

app = Flask(__name__)

occupations = {}
 
@app.route("/occupations")
def randomoccup():
    return render_template('whatjob.html',title="Occupations",collection=randomoccupoto.occupations(),job = randomoccupoto.selectOccupation())

if __name__ == "__main__":
    app.debug = True
    app.run()
