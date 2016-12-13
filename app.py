from flask import Flask, render_template, request, redirect
import requests
from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
    plot = figure(tools="pan,wheel_zoom,box_zoom,reset",
              title='Data from Quandle WIKI set',
              x_axis_label='date',
              x_axis_type='datetime')

    script, div = components(plot)
    return render_template('index.html', script=script, div=div)

if __name__ == '__main__':
    app.run(port=33507,debug=True)
