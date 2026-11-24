import os
import re
from datetime import date, datetime

from flask import Flask, abort, render_template, request

import db

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

APPOINTMENTS = [
    {
        "id": 1,
        "customer_name": "Maria Rodriguez",
        "email": "maria@example.com",
        "phone": "202-555-0101",
        "service_name": "Haircut",
        "appointment_date": "November 12, 2026",
        "appointment_date_iso": "2026-11-12",
        "appointment_time": "9:00 AM",
        "duration_minutes": 45,
        "status": "Pending",
    },
    {
        "id": 2,
        "customer_name": "Sofia Martinez",
        "email": "sofia@example.com",
        "phone": "202-555-0102",
        "service_name": "Hair Coloring",
        "appointment_date": "November 13, 2026",
        "appointment_date_iso": "2026-11-13",
        "appointment_time": "10:00 AM",
        "duration_minutes": 120,
        "status": "Confirmed",
    },
    {
        "id": 3,
        "customer_name": "Elena Garcia",
        "email": "elena@example.com",
        "phone": "202-555-0103",
        "service_name": "Hair Styling",
        "appointment_date": "November 8, 2026",
        "appointment_date_iso": "2026-11-08",
        "appointment_time": "1:00 PM",
        "duration_minutes": 60,
        "status": "Completed",
    },
    {
        "id": 4,
        "customer_name": "Andrea Lopez",
        "email": "andrea@example.com",
        "phone": "202-555-0104",
        "service_name": "Manicure",
        "appointment_date": "November 9, 2026",
        "appointment_date_iso": "2026-11-09",
        "appointment_time": "2:00 PM",
        "duration_minutes": 45,
        "status": "Canceled",
    },
    {
        "id": 5,
        "customer_name": "Carlos Rivera",
        "email": "carlos@example.com",
        "phone": "202-555-0105",
        "service_name": "Pedicure",
        "appointment_date": "November 12, 2026",
        "appointment_date_iso": "2026-11-12",
        "appointment_time": "10:00 AM",
        "duration_minutes": 60,
        "status": "Confirmed",
    },
    {
        "id": 6,
        "customer_name": "Isabella Torres",
        "email": "isabella@example.com",
        "phone": "202-555-0106",
        "service_name": "Facial",
        "appointment_date": "November 12, 2026",
        "appointment_date_iso": "2026-11-12",
        "appointment_time": "1:00 PM",
        "duration_minutes": 60,
        "status": "Pending",
    },
]

app = Flask(__name__)
os.makedirs(app.instance_path, exist_ok=True)
app.config["DATABASE"] = os.path.join(app.instance_path, "salon.sqlite")
db.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/services")
def services():
    return render_template("services.html", services=SERVICES)


@app.route("/services/admin")
def services_admin():
    return render_template("services_admin.html", services=SERVICES)


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


@app.route("/appointments")
def appointment_history():
    contact_query = request.args.get("contact", "").strip()
    if contact_query:
        normalized_contact = contact_query.casefold()
        normalized_phone = re.sub(r"\D", "", contact_query)
        appointments = [
            appointment
            for appointment in APPOINTMENTS
            if appointment["email"].casefold() == normalized_contact
            or (
                normalized_phone
                and re.sub(r"\D", "", appointment["phone"]) == normalized_phone
            )
        ]
    else:
        appointments = APPOINTMENTS.copy()

    return render_template(
        "appointments.html",
        appointments=appointments,
        contact_query=contact_query,
    )


@app.route("/calendar")
def staff_calendar():
    selected_date = request.args.get("date", "2026-11-12")
    try:
        parsed_date = date.fromisoformat(selected_date)
    except ValueError:
        abort(400)

    appointments = [
        appointment
        for appointment in APPOINTMENTS
        if appointment["appointment_date_iso"] == selected_date
    ]
    appointments.sort(
        key=lambda appointment: datetime.strptime(
            appointment["appointment_time"],
            "%I:%M %p",
        )
    )

    return render_template(
        "calendar.html",
        appointments=appointments,
        selected_date=selected_date,
        human_readable_date=(
            f"{parsed_date:%B} {parsed_date.day}, {parsed_date.year}"
        ),
    )
