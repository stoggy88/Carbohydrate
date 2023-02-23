from dash import dcc, html, Input,Output, dash_table, ctx
import dash_bootstrap_components as dbc

SHORT_FORM_IDENTITIES = {
    'Ac' : 'acetyl',
    'All' : 'allyl',
    'Bn' : 'benzyl',
    'Br' : 'bromine',
    'Bu' : 'butyl',
    'Bz' : 'benzoyl',
    'Cbz' : 'benzyloxycarbonyl',
    'CDA' : 'cyclohexane-1,2-diacetal',
    'Cl' : 'chloro',
    'ClAc' : 'chloroacetyl',
    'DCA' : '?',
    'DMT' : 'dimethoxytrityl',
    'Et' : 'ethyl',
    'F' : 'fluoro',
    'Hex' : 'hexyl',
    'I' : 'iodo',
    'iBu' : 'isobutyl',
    'iPent' : 'isopentyl',
    'iPr' : 'isopropyl',
    'Lev' : 'levulinoyl',
    'Me' : 'methyl',
    'Ms' : 'mesyl',
    'N3' : 'azido',
    'opNDP' : '2,4-dinitrophenyl',
    'Pent' : 'pentyl',
    'Ph' : 'phenyl',
    'Phth' : 'phthalimidoyl',
    'Pic' : 'picolyl',
    'Piv' : 'pivaloyl',
    #'pMOPh' : ['paramethoxyphenyl', '4-methoxyphenyl', 'PMP'],
    'PMB' : 'paramethoxybenzyl',
    'PNP' : 'paranitrophenyl',
    'PPG' : 'propargyl',
    'Pr' : 'propyl',
    'sBu' : 'sec-butyl',
    'sHex' : 'sec-hexyl',
    'sPent' : 'sec-pentyl',
    'TBDPS' : 'tert-butyldiphenylsilyl',
    'TBS' : 'tert-butyldimethylsilyl',
    'TES' : 'triethylsilyl',
    'TCA' : 'trichloroacetyl',
    'TCAI' : 'trichloroacetimidoyl',
    'Tf' : 'triflyl',
    'Trt' : 'trityl',
    #'Ts' : ['tosyl', 'toluenesulfonyl'],
}

def get_filters():

    filters=dbc.Col(width=3, children=[
                dbc.Row(children=[dbc.Col(html.H5('Carb'),width=1),
                                    dbc.Col(html.H5('Ori'),width=1),
                                    dbc.Col(html.H5('Substituent'),width=9),
                                    dbc.Col(html.H5('Deo'),width=1),
                ])])  
    j=1
    for j in range(1,7):
        if j <6:
            filters.children.append(dbc.Row(children=[
                            dbc.Col('C({})'.format(j),width=1),
                            dbc.Col(dcc.Checklist([''],id='c{}oricheck'.format(j)),width=1),
                            dbc.Col(dcc.Dropdown(id='c{}subsituent'.format(j),
                                                options=[{'label': j, 'value': j} for j in SHORT_FORM_IDENTITIES.values()]),width=9),
                            dbc.Col(dcc.Checklist([''],id='c{}deocheck'.format(j)),width=1),     
                ]))
        else:
            filters.children.append(dbc.Row(children=[
                dbc.Col('C({})'.format(j),width=1),
                dbc.Col(width=1),
                dbc.Col(dcc.Dropdown(id='c{}subsituent'.format(j),
                                    options=[{'label': j, 'value': j} for j in SHORT_FORM_IDENTITIES.values()]),width=9),
                dbc.Col(dcc.Checklist([''],id='c{}deocheck'.format(j)),width=1),   
        ]))
        j+=1
    
    return filters
