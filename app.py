from flask import Flask, abort, render_template, request

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

APPOINTMENT_SLOTS = [
    {"time": "9:00 AM", "available": True},
    {"time": "10:00 AM", "available": True},
    {"time": "11:00 AM", "available": False},
    {"time": "1:00 PM", "available": True},
    {"time": "2:00 PM", "available": True},
    {"time": "3:00 PM", "available": True},
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


@app.route("/book")
def book():
    raw_service_id = request.args.get("service_id")
    selected_service = None
    if raw_service_id is not None:
        try:
            service_id = int(raw_service_id)
        except ValueError:
            abort(404)

        selected_service = next(
            (item for item in SERVICES if item["id"] == service_id),
            None,
        )
        if selected_service is None:
            abort(404)

    return render_template(
        "book.html",
        SERVICES=SERVICES,
        selected_service=selected_service,
        appointment_slots=APPOINTMENT_SLOTS,
    )


@app.route("/book/review")
def booking_review():
    raw_service_id = request.args.get("service_id")
    if raw_service_id is None:
        abort(404)

    try:
        service_id = int(raw_service_id)
    except ValueError:
        abort(404)

    service = next(
        (item for item in SERVICES if item["id"] == service_id),
        None,
    )
    if service is None:
        abort(404)

    return render_template(
        "review_confirm.html",
        service=service,
        appointment_date=request.args.get("appointment_date", ""),
        appointment_time=request.args.get("appointment_time", ""),
    )
