"""CCC181 Week 2: a "Hello, Flask" starter app.

Run it with:
    flask --app app run --debug
then open http://127.0.0.1:5000
"""
from flask import Flask, render_template

app = Flask(__name__)

# Sample data for the demo. A real app would load this from a database later.
SERVICES = [
    {"id": 1, "name": "Consultation"},
    {"id": 2, "name": "Medical certificate"},
]

TICKETS = [
    {"number": 1, "name": "Ana", "email": "ana@school.edu", "service_id": 1, "status": "waiting"},
    {"number": 2, "name": "Ben", "email": "ben@school.edu", "service_id": 2, "status": "waiting"},
]


@app.route("/")
def index():
    # render_template looks inside the templates/ folder and passes
    # keyword arguments to the template as variables.
    return render_template("index.html", name="Ana", tickets=TICKETS)


@app.route("/queue/<int:ticket_id>")
def ticket(ticket_id):
    t = next((t for t in TICKETS if t["number"] == ticket_id), None)
    if t is None:
        abort(404)
    service = next(s for s in SERVICES if s["id"] == t["service_id"])
    return render_template("ticket.html", ticket=t, service=service)


@app.route("/hello")
def hello():
    # The plain-string version from the Routes slide.
    return "Hello, CCC181!"


if __name__ == "__main__":
    # Lets you also start the app with: python app.py
    app.run(debug=True)
