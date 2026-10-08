import json
import os
import smtplib
from email.message import EmailMessage
from http.server import BaseHTTPRequestHandler

TO_EMAIL = os.environ.get("CONTACT_TO_EMAIL", "singhpratibha72963@gmail.com")
SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "465"))
SMTP_USER = os.environ.get("SMTP_USER", "")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "")

def send_email(data):
    if not SMTP_USER or not SMTP_PASSWORD:
        raise RuntimeError("Email service is not configured.")

    msg = EmailMessage()
    msg["Subject"] = f"New Portfolio Enquiry — {data['project_type']}"
    msg["From"] = SMTP_USER
    msg["To"] = TO_EMAIL
    msg["Reply-To"] = data["email"]

    msg.set_content(
        f"""New enquiry from Pratibha's portfolio

Name: {data['name']}
Email: {data['email']}
Project type: {data['project_type']}

Message:
{data['message']}
"""
    )

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.login(SMTP_USER, SMTP_PASSWORD)
        smtp.send_message(msg)

class handler(BaseHTTPRequestHandler):
    def _send(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self._send(200, {"ok": True})

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length)
            data = json.loads(raw or "{}")

            required = ["name", "email", "project_type", "message"]
            if any(not str(data.get(k, "")).strip() for k in required):
                return self._send(400, {"error": "Please complete all fields."})

            if "@" not in data["email"]:
                return self._send(400, {"error": "Please enter a valid email address."})

            # Send the enquiry to Pratibha by email.
            send_email(data)
            return self._send(200, {"ok": True})

        except Exception as exc:
            # Do not expose SMTP credentials or internal errors to visitors.
            print("CONTACT_FORM_ERROR:", repr(exc))
            return self._send(
                500,
                {"error": "Unable to send your enquiry right now. Please email Pratibha directly."}
            )
