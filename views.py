from flask import Flask,render_template,url_for
from request import get_music

app = Flask(__name__)


@app.route('/')
def index():
    title = "Search Data compiled by Itunes "
    table= get_music('track')
    return render_template('itunes.html', table=table, title=title)


if  __name__ == '__main__':
    app.run(debug=True)