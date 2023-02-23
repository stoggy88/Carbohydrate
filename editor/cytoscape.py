import dash_cytoscape as cyto

default_stylesheet = [
    {
        'selector': 'node',
        'style': {
            'label': 'data(label)',
            'width': "2%",
            'height': "2%"
        }
    },
                {
                'selector': '.red',
                'style': {
                    'background-color': 'red',
                    'line-color': 'red'
                }
            },
]

def get_cytoscape():
    cytoscape = cyto.Cytoscape(
            id='carbo-cytoscape',
            layout={'name': 'preset'},
            style={'width': '100%', 'height': '500px'},
            elements=[
                {'data': {'id': '1', 'label': ''}, 'position': {'x': 100, 'y': 125}},
                {'data': {'id': '2', 'label': ''}, 'position': {'x': 50, 'y': 150}},
                {'data': {'id': '3', 'label': ''}, 'position': {'x': 50, 'y': 200}},
                {'data': {'id': '4', 'label': ''}, 'position': {'x': 100, 'y': 225}},
                {'data': {'id': '5', 'label': ''}, 'position': {'x': 150, 'y': 200}},
                {'data': {'id': '6', 'label': ''}, 'position': {'x': 150, 'y': 150}},
                {'data': {'id': '22', 'label': ''}, 'position': {'x': 0, 'y': 125}},
                {'data': {'id': '23', 'label': 'HO'}, 'position': {'x':-50, 'y': 150}},
                {'data': {'id': '32', 'label': 'HO'}, 'position': {'x':0, 'y': 225}},
                {'data': {'id': '42', 'label': 'OH'}, 'position': {'x':100, 'y': 275}},
                {'data': {'id': '52', 'label': 'OH'}, 'position': {'x':200, 'y': 225}},
                {'data': {'id': '62', 'label': 'OH'}, 'position': {'x':200, 'y': 125}},
                {'data': {'source': '1', 'target': '2'}},
                {'data': {'source': '2', 'target': '3'}},
                {'data': {'source': '2', 'target': '22'}},
                {'data': {'source': '22', 'target': '23'}},
                {'data': {'source': '3', 'target': '4'}},
                {'data': {'source': '3', 'target': '32'}},
                {'data': {'source': '4', 'target': '5'}},
                {'data': {'source': '4', 'target': '42'}},
                {'data': {'source': '5', 'target': '6'}},
                {'data': {'source': '5', 'target': '52'}},
                {'data': {'source': '6', 'target': '1'}},
                {'data': {'source': '6', 'target': '62'}},
            ],
            stylesheet=default_stylesheet
        )
    return cytoscape