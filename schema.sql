PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE CHECK (length(trim(username)) > 0),
    password_hash TEXT NOT NULL CHECK (length(password_hash) > 0),
    role TEXT NOT NULL CHECK (role IN ('admin', 'staff', 'client'))
);

CREATE TABLE services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE CHECK (length(trim(name)) > 0),
    description TEXT NOT NULL CHECK (length(trim(description)) > 0),
    duration_minutes INTEGER NOT NULL CHECK (duration_minutes > 0),
    price_cents INTEGER NOT NULL CHECK (price_cents >= 0),
    active INTEGER NOT NULL DEFAULT 1 CHECK (active IN (0, 1))
);

CREATE TABLE appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    service_id INTEGER NOT NULL,
    client_name TEXT NOT NULL CHECK (length(trim(client_name)) > 0),
    client_email TEXT,
    client_phone TEXT,
    date TEXT NOT NULL CHECK (
        date(date) IS NOT NULL
        AND date = date(date, '+0 days')
        AND date GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
    ),
    time TEXT NOT NULL CHECK (
        time GLOB '[0-2][0-9]:[0-5][0-9]'
        AND substr(time, 1, 2) BETWEEN '00' AND '23'
    ),
    status TEXT NOT NULL DEFAULT 'Pending'
        CHECK (status IN ('Pending', 'Confirmed', 'Completed', 'Canceled')),
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL,
    FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE RESTRICT
);

CREATE INDEX idx_appointments_date_time ON appointments(date, time);
CREATE INDEX idx_appointments_user_id ON appointments(user_id);
CREATE INDEX idx_appointments_service_id ON appointments(service_id);

INSERT INTO services (id, name, description, duration_minutes, price_cents) VALUES
    (1, 'Haircut', 'Professional haircut', 45, 3500),
    (2, 'Hair Coloring', 'Hair coloring and treatment', 120, 9000),
    (3, 'Hair Styling', 'Professional hair styling', 60, 5000),
    (4, 'Manicure', 'Nail care and treatment', 45, 3000),
    (5, 'Pedicure', 'Professional foot care and treatment', 60, 4500),
    (6, 'Facial', 'Skin cleansing and facial treatment', 60, 6500);

INSERT INTO appointments (
    user_id,
    service_id,
    client_name,
    date,
    time,
    status,
    notes
) VALUES
    (NULL, 1, 'Sample Client A', '2026-11-25', '09:00', 'Pending', 'Illustrative sample appointment.'),
    (NULL, 2, 'Sample Client B', '2026-11-26', '10:30', 'Confirmed', 'Illustrative sample appointment.'),
    (NULL, 4, 'Sample Client C', '2026-11-27', '13:00', 'Pending', 'Illustrative sample appointment.'),
    (NULL, 6, 'Sample Client D', '2026-11-28', '14:30', 'Confirmed', 'Illustrative sample appointment.');
