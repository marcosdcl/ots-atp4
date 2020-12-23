from flask import Flask, render_template

from metodos import marketplaces, categories


app = Flask(__name__)


@app.route('/')
def index():
    mkt_list = marketplaces()
    return render_template('marketplaces.html', list = mkt_list)

@app.route('/meli')
def mkt_meli():
    cat_list = categories()
    return render_template('categories.html', list = cat_list)

@app.route('/b2w')
def mkt_b2w():
    cat_list = categories()
    return render_template('categories.html', list = cat_list)

@app.route('/magalu')
def mkt_magalu():
    cat_list = categories()
    return render_template('categories.html', list = cat_list)


app.run(debug=True)
