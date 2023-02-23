from dash import dcc, html, Input,Output, dash_table, ctx
import dash_bootstrap_components as dbc
from datetime import date

from django_plotly_dash import DjangoDash

from.components import get_filters
from .cytoscape import get_cytoscape

app = DjangoDash('SimpleExample',external_stylesheets=[dbc.themes.BOOTSTRAP])   # replaces dash.Dash

app.layout = html.Div(children=[dbc.Row(children=[dbc.Col(get_cytoscape(),width=9),
                                        get_filters()]),
                                dbc.Row(dbc.Col(html.H3(id='carb-name'),style={'textAlign':'center'},width=9))])

@app.callback(Output('carb-name', 'children'),
                Input('c1subsituent','value'),
                Input('c2subsituent','value'),
                Input('c3subsituent','value'),
                Input('c4subsituent','value'),
                Input('c5subsituent','value'),
                Input('c6subsituent','value'),
                Input('c1oricheck','value'),
                Input('c2oricheck','value'),
                Input('c3oricheck','value'),
                Input('c4oricheck','value'),
                Input('c5oricheck','value'),          
              )
def update_output(c1,c2,c3,c4,c5,c6,o1,o2,o3,o4,o5):

    name = ''

    if c1 is not None:
        name = '1-O-'+c1
    if c2 is not None:
        name = name +'-2-O-'+c2
    if c3 is not None:
        name = name+'-3-O-'+c3
    if c4 is not None:  
        name = name+'-4-O-'+c4
    if c5 is not None:
        name = name+'-5-O-'+c5
    if c6 is not None:
        name = name+'-6-O-'+c6

    if name != '':
        name=name+'-'

    if o1 is None or "" not in o1:
        name=name+'α-'
    else: name=name+'β-'

    if o5 is None or "" not in o5:
        name=name+'D-'
    else: name=name+'L-'

    name = name+'allopyranoside'

    return name

@app.callback(Output('carbo-cytoscape', 'elements'),
              Input('c1deocheck','value'),
              Input('c2deocheck','value'),)
def update_cytoscape(d1,d2):

    elements = [
                {'data': {'id': '3', 'label': ''}, 'position': {'x': 50, 'y': 200}},
                {'data': {'id': '4', 'label': ''}, 'position': {'x': 100, 'y': 225}},
                {'data': {'id': '5', 'label': ''}, 'position': {'x': 150, 'y': 200}},
                {'data': {'id': '6', 'label': ''}, 'position': {'x': 150, 'y': 150}},
                {'data': {'id': '32', 'label': 'HO'}, 'position': {'x':0, 'y': 225}},
                {'data': {'id': '42', 'label': 'OH'}, 'position': {'x':100, 'y': 275}},
                {'data': {'id': '52', 'label': 'OH'}, 'position': {'x':200, 'y': 225}},
                {'data': {'id': '62', 'label': 'OH'}, 'position': {'x':200, 'y': 125}},
                {'data': {'source': '3', 'target': '4'}},
                {'data': {'source': '3', 'target': '32'}},
                {'data': {'source': '4', 'target': '5'}},
                {'data': {'source': '4', 'target': '42'}},
                {'data': {'source': '5', 'target': '6'}},
                {'data': {'source': '5', 'target': '52'}},
                {'data': {'source': '6', 'target': '1'}},
                {'data': {'source': '6', 'target': '62'}},
            ]

    if d1 is None or "" not in d1:
        d1_elements = [
            {'data': {'id': '1', 'label': ''}, 'position': {'x': 100, 'y': 125}},
            {'data': {'source': '1', 'target': '2'}},] 
    else:
        d1_elements = [{'data': {'id': '1', 'label': ''}, 'position': {'x': 100, 'y': 125}},
                       {'data': {'source': '1', 'target': '2'},'classes':'red'},]
    
    if d2 is None or "" not in d2:
        d2_elements = [
            {'data': {'id': '2', 'label': ''}, 'position': {'x': 50, 'y': 150}},
            {'data': {'id': '22', 'label': ''}, 'position': {'x': 0, 'y': 125}},
            {'data': {'id': '23', 'label': 'HO'}, 'position': {'x':-50, 'y': 150}},
            {'data': {'source': '2', 'target': '3'}},
            {'data': {'source': '2', 'target': '22'}},
            {'data': {'source': '22', 'target': '23'}},
            ]
    else:
        d2_elements = [
            {'data': {'id': '2', 'label': ''}, 'position': {'x': 50, 'y': 150}},
            {'data': {'id': '22', 'label': ''}, 'position': {'x': 0, 'y': 175}},
            {'data': {'id': '23', 'label': 'OH'}, 'position': {'x':-50, 'y': 150}},
            {'data': {'source': '2', 'target': '3'},'classes':'red'},
            {'data': {'source': '2', 'target': '22'},'classes':'red'},
            {'data': {'source': '22', 'target': '23'},'classes':'red'},
            ]
        
    
    
        
    elements = elements + d1_elements + d2_elements

    return elements