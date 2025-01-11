from flask import Flask

app = Flask(__name__)

# Import views or routes (avoid circular imports by placing this at the end)
from app import routes
