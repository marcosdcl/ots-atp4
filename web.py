from flask import Flask, render_template

from metodos import (
    marketplaces,
    categories,
    sub_categories
)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/marketplaces')
def marketplace():
    mkt_list = marketplaces()
    return render_template('lists.html', list = mkt_list)

@app.route('/categories')
def category():
    cat_list = categories()
    return render_template('lists.html', list = cat_list)

@app.route('/subcategories')
def sub_category():
    sub_list = sub_categories()
    return render_template('lists.html', list = sub_list)


app.run(debug=True)
