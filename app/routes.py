from app import app
from flask import render_template
from app.services.igdb_service import get_random_games, get_best_rated_games


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/random")
def random_games():
    quant_games = get_random_games(10)
    return render_template("random_games.html", games=quant_games)


@app.route("/best_rated")
def best_rated_games():
    quant_games = get_best_rated_games(100)
    return render_template("best_rated_games.html", games=quant_games)