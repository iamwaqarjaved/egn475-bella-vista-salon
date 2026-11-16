from flask import Flask, abort, render_template

SERVICES = [
    {
        "id": 1,
        "name": "Haircut",
        "description": "Professional haircut",
        "duration_minutes": 45,
        "price_cents": 3500,
    },
    {
        "id": 2,
        "name": "Hair Coloring",
        "description": "Hair coloring and treatment",
        "duration_minutes": 120,
        "price_cents": 9000,
    },
    {
        "id": 3,
        "name": "Hair Styling",
        "description": "Professional hair styling",
        "duration_minutes": 60,
        "price_cents": 5000,
    },
    {
        "id": 4,
        "name": "Manicure",
        "description": "Nail care and treatment",
        "duration_minutes": 45,
        "price_cents": 3000,
    },
    {
        "id": 5,
        "name": "Pedicure",
        "description": "Professional foot care and treatment",
        "duration_minutes": 60,
        "price_cents": 4500,
    },
    {
        "id": 6,
        "name": "Facial",
        "description": "Skin cleansing and facial treatment",
        "duration_minutes": 60,
        "price_cents": 6500,
    },
]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/services")
def services():
    return render_template("services.html", services=SERVICES)


@app.route("/services/<int:service_id>")
def service_detail(service_id):
    service = next(
        (item for item in SERVICES if item["id"] == service_id),
        None,
    )
    if service is None:
        abort(404)

    return render_template("service_detail.html", service=service)
