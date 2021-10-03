from flask import Flask, flash, redirect, render_template, \
     request, url_for
import geonamescache

app = Flask(__name__)
gc = geonamescache.GeonamesCache()

@app.route('/')
def index():
    return render_template('template.html',
        data=[value['name'] for key, value in gc.get_cities().items()])

@app.route('/test' , methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    return(str(select)) # just to see what select is

if __name__=='__main__':
    app.run(debug=True)
