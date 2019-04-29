# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:15:24 2019

@author: Suhas.Karanth
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 13:57:35 2019

@author: Arnab.Saha
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import flask
import pandas as pd
import numpy as np

#app=dash.Dash()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "PROMO ROI"

#server = app.server
#creating a link between two dropdowns or cascading
all_options = {
    'Instacart': {
        '1234',
        '5678',
		'68978'
    },
    'Kroger': {
        '3456',
        '8901',
		'Not Available'
    },
	'Shipt': {
        '13456',
        '28901'
    },
	'Walmart OGP': {
        '83456',
        '08901'
    },
	'Amazon': {
        '63456',
        '48901'
    }

}

app.layout = html.Div(
        html.Div([
            html.H1(children='PROMO ROI'),
			html.H2(children='A UI to calculate Returns on Investment'
		),
		
		dcc.Input(
			id="Event Field",
			placeholder='Enter Event Title',
    		type='text',
    		value=''
		),

		dcc.Dropdown(
        		id='Retailer Dropdown',
        		options=[{'label': k, 'value': k} for k in all_options.keys()],
        		placeholder="Select Retailer"
			#value='America'
    	),

    	html.Hr(),

    	dcc.RadioItems(id='UPC dropdown'),

    	html.Div(id='display-selected-values')
	]
	)
)

@app.callback(
    dash.dependencies.Output('UPC dropdown', 'options'),
    [dash.dependencies.Input('Retailer Dropdown', 'value')])
def set_UPC_options(selected_retailer):
    return [{'label': i, 'value': i} for i in all_options[selected_retailer]]


@app.callback(
    dash.dependencies.Output('UPC dropdown', 'value'),
    [dash.dependencies.Input('UPC dropdown', 'options')])
def set_UPC_value(available_options):
    return available_options[0]['value']

if __name__ == '__main__':
    app.run_server(debug=True)

