import io
import os
import subprocess
import tempfile
from logging.config import dictConfig

from dotenv import load_dotenv
from flask import Flask, request, send_file

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)


load_dotenv()

app = Flask(__name__)


@app.route("/")
def document():
    app.logger.info('owi !')
    token = request.args.get("token", None)

    if token is None or os.environ.get("API_TOKEN", None) != token:
        return "Auth error", 403

    url = request.args.get("url", None)
    filename = request.args.get("filename", None)
    if url is None or filename is None:
        return "Bad params", 400

    with tempfile.NamedTemporaryFile(mode="wb") as f:
        command = ["wkhtmltopdf", url, f.name]
        subprocess.call(command)
        with open(f.name, "rb") as d:
            document = io.BytesIO(d.read())

    return send_file(document, attachment_filename=filename, mimetype="application/pdf")
