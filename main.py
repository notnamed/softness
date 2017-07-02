from flask import Flask, render_template, redirect, request, g
import sqlite3
import os

app = Flask(__name__)

@app.before_request
def before_request():
    g.db = sqlite3.connect("softness.db")

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route("/")
def main():
    dbresult = g.db.execute('SELECT * FROM audio WHERE id IN (SELECT id FROM audio ORDER BY RANDOM() LIMIT 1)')
    for the_dbresult in dbresult:
        title = the_dbresult[1]
        author = the_dbresult[2]
	url = the_dbresult[6]
	license = the_dbresult[3]
	mp3 = the_dbresult[4]
    return render_template("index.html", title=title, author=author, url=url, license=license, mp3=mp3)

if __name__ == "__main__":
    app.run(debug=False)
