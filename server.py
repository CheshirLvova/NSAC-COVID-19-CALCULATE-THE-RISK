from flask import Flask, flash, redirect, render_template, \
     request, url_for
import geonamescache

app = Flask(__name__)
gc = geonamescache.GeonamesCache()

@app.route('/')
def index():
    return render_template('index.html',
        data={'cities': [value['name'] for key, value in gc.get_cities().items()],
              'city': None,
              'total_cases': 360.524,
              'active_cases': 244.375,
              'recovered': 100.658,
              'total_death': 15.491})

@app.route('/calculate' , methods=['GET', 'POST'])
def calculate():
    selected_city = str(request.form.get('comp_select'))
    return render_template('index.html',
        data={'cities': [value['name'] for key, value in gc.get_cities().items()],
              'city': selected_city,
              'total_cases': 360.524,
              'active_cases': 244.375,
              'recovered': 100.658,
              'total_death': 15.491})

if __name__=='__main__':
    app.run(debug=True)
