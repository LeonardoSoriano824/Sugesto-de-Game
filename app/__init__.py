from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "chave_padrao_para_dev")

app.config["IGDB_CLIENT_ID"] = os.getenv("IGDB_CLIENT_ID", "")
app.config["IGDB_ACCESS_TOKEN"] = os.getenv("IGDB_ACCESS_TOKEN", "")

from app import routes