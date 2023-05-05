"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaabuqk728r8867hq70-a.oregon-postgres.render.com",
        database="bt_7cvx",
        user="bt_7cvx_user",
        password="F91Gv43bwKoBCYZaeTVhac3AWUUdEqES")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
