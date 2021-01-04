import sys
sys.path.append('')

from flask import Flask, render_template, request

from backend.metodos import marketplaces, categories, new_marketplaces


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    mkt_list = marketplaces()
    return render_template('marketplaces.html', list = mkt_list)

@app.route('/add_mkt')
def create_marketplace():
    mkt = request.args.get('marketplace')
    new_marketplaces(mkt)
    mkt_list = marketplaces()
    return render_template(
        'marketplaces.html', success = True, 
        list = mkt_list,
        mkt = mkt
        )

@app.route('/categories/<string:mkt>', methods=['GET'])
def mkt_meli(mkt):
    title = mkt
    cat_list = categories()
    return render_template('categories.html', list = cat_list, title = title)


app.run(debug=True)
