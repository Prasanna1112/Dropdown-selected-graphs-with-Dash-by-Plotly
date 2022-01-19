import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
import pandas as pd
from dash.dependencies import Input, Output


df = px.data.tips()

pio.templates.default = "plotly_dark"

app = dash.Dash(__name__)

server = app.server

# def blank_figure():
# 	fig = go.Figure()
# 	fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',
# 		paper_bgcolor='rgba(0,0,0,0)',
# 		yaxis=dict(showgrid=False, zeroline=False,
# 		tickfont = dict(color = 'rgba(0,0,0,0)')),
# 		xaxis = dict(showgrid=False,
# 		zeroline=False, 
# 		tickfont = dict(color = 'rgba(0,0,0,0)')))
# 	return fig

app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Pie Chart', 'value': 'PC'},
            {'label': 'Bar Chart', 'value': 'BC'},
            {'label': 'Histogram', 'value': 'HIS'},
            {'label': 'Scatter Plot', 'value': 'SCAT'},
            {'label': 'Box Plot', 'value': 'BOX'},
            {'label': 'Line Graph', 'value': 'LIN'}
        ],
        placeholder="Select type of graph to display...",
        multi=False,
        clearable=True,
        disabled=False,
        style={'margin': 5, 'fex': 1}
    ),
    html.Div(
    	dcc.Graph(
        	id='graph1',
        	className='pieplot',
        	style={'display':'none'},
        	# figure = blank_figure(),
    	),
    	style={'display':'inline-block'}
),
    html.Div(
    	dcc.Graph(
        	id='graph2',
        	className='barplot',
        	style={'display':'none'},
        	# figure = blank_figure()
    	),
    	style={'display':'inline-block'}),
    
    html.Div(
    	dcc.Graph(
        	id='graph3',
        	className='Histogram',
        	style={'display':'none'},
        	# figure = blank_figure()
    	),
    	style={'display':'inline-block'}),

    html.Div(
    	dcc.Graph(
        	id='graph4',
        	className='scatterplot',
        	style={'display':'none'},
        	# figure = blank_figure()
    	),
    	style={'display':'inline-block'}),
    
    html.Div(
    	dcc.Graph(
        	id='graph5',
        	className='boxplot',
        	style={'display':'none'},
        	# figure = blank_figure()
    	),
    	style={'display':'inline-block'}),

    
    html.Div(
    	dcc.Graph(
        	id='graph6',
        	className='linechart',
        	style={'display':'none', 'width': '800px'},
        	# figure = blank_figure(),
    	),
    	style={'display':'inline-block'}),

html.Div(id='out_container')
])

@app.callback(
    Output(component_id='out_container', component_property='children'),
    [Input(component_id='dropdown', component_property='value')]
)
def build_graph(data_chosen):
    return ('Search value was: " {} "'.format(data_chosen))

@app.callback(
	Output('graph1', 'figure'),
	Output('graph1', 'style'),
    Input('dropdown', 'value'))
def update_figure(selected_pie):
	style = {'display': 'none'} if selected_pie is None else {'display': 'block'}
	if selected_pie=='PC':
		df1 = df
		fig1 = px.pie(df1, values='tip', names='day', title='Day-wise tips')
		fig1.update_traces(textinfo='percent+label', marker=dict(colors=['gold', 'mediumturquoise', 'darkorange', 'lightgreen'], line=dict(color='#000000', width=2)))
		return fig1,style

@app.callback(
	Output('graph2', 'figure'),
	Output('graph2', 'style'),
    Input('dropdown', 'value'))
def update_figure(selected_bar):
	style = {'display': 'none'} if selected_bar is None else {'display': 'block'}
	if selected_bar=='BC':
		dff2 = px.data.medals_long()
		fig2 = px.bar(dff2, x="medal", y="count", color="nation", text_auto=True, title='Total medals won by countries')
		return fig2,style

@app.callback(
	Output('graph3', 'figure'),
	Output('graph3', 'style'),
    [Input('dropdown', 'value')])
def update_figure(selected_hist):
	style = {'display': 'none'} if selected_hist is None else {'display': 'block'}
	url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
	names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'diabetic']
	dff3 = pd.read_csv(url, names=names)
	if selected_hist=='HIS':
		fig3 = px.histogram(dff3, x='mass', color='diabetic', title='Histogram of diabetec people by BMI')
		return fig3,style

@app.callback(
	Output('graph4', 'figure'),
	Output('graph4', 'style'),
    Input('dropdown', 'value'))
def update_figure(selected_scatter):
	style = {'display': 'none'} if selected_scatter is None else {'display': 'block'}
	if selected_scatter=='SCAT':
		dff4 = px.data.iris()
		fig4 = px.scatter(
		dff4, x="sepal_width", y="sepal_length",
		color="species", size='petal_length',
		hover_data=['petal_width'], title='Distribution of species per sepal')
		return fig4,style

@app.callback(
	Output('graph5', 'figure'),
	Output('graph5', 'style'),
    Input('dropdown', 'value'))
def update_figure(selected_box):
	style = {'display': 'none'} if selected_box is None else {'display': 'block'}
	if selected_box=='BOX':
		dff5 = df
		# Exclusive algorithm uses the median to divide the ordered dataset into two halves. 
		# If the sample is odd, it does not include the median in either half. 
		# Q1 is then the median of the lower half and Q3 is the median of the upper half.
		fig5 = px.box(df, x="day", y="total_bill", color="smoker", title='Boxlplot for smokers by bill paid on respective days')
		fig5.update_traces(quartilemethod="exclusive")
		return fig5,style

@app.callback(
	Output('graph6', 'figure'),
	Output('graph6', 'style'),
    Input('dropdown', 'value'))
def update_figure(selected_line):
	style = {'display': 'none'} if selected_line is None else {'display': 'block'}
	if selected_line=='LIN':
		dff6 = px.data.gapminder().query("continent == 'Oceania'")
		fig6 = px.line(dff6, x='year', y='lifeExp', color='country', markers=True, title='Life expectancy per year from Oceania')
		return fig6,style


# @app.callback(
# 	Output('graph1', 'figure'),
#     [Input('dropdown', 'value')])
# def update_figure(selected):
	# if selected=='PC':
	# 	df1 = df
	# 	fig1 = px.pie(df1, values='tip', names='day', title='Day-wise tips')
	# 	fig1.update_traces(textinfo='percent+label', marker=dict(colors=['gold', 'mediumturquoise', 'darkorange', 'lightgreen'], line=dict(color='#000000', width=2)))
	# 	fig1.show()
	# elif selected=='BC':
	# 	dff2 = px.data.medals_long()
	# 	fig2 = px.bar(dff2, x="medal", y="count", color="nation", text_auto=True)
	# 	fig2.show()
	# elif selected=='HIS':
	# 	url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
	# 	names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'diabetic']
	# 	dff3 = pd.read_csv(url, names=names)
	# 	fig3 = px.histogram(dff3, x='mass', color='diabetic', title='Histogram of diabetec people by BMI')
	# 	fig3.show()
	# elif selected=='SCAT':
	# 	dff4 = px.data.iris()
	# 	fig4 = px.scatter(
	#         dff4, x="sepal_width", y="sepal_length", 
	#         color="species", size='petal_length', 
	#         hover_data=['petal_width'], title='Distribution of species per sepal')
	# 	fig4.show()
	# elif selected=='BOX':
	# 	dff5 = df

	# # Exclusive algorithm uses the median to divide the ordered dataset into two halves. 
	# # If the sample is odd, it does not include the median in either half. 
	# # Q1 is then the median of the lower half and Q3 is the median of the upper half.

	# 	fig5 = px.box(df, x="day", y="total_bill", color="smoker", title='Boxlplot for smokers by bill paid on respective days')
	# 	fig5.update_traces(quartilemethod="exclusive")
	# 	fig5.show()
	# elif selected=='LIN':
	# 	dff6 = px.data.gapminder().query("continent == 'Oceania'")
	# 	fig6 = px.line(dff6, x='year', y='lifeExp', color='country', markers=True)
	# 	fig6.show()

if __name__ == '__main__':
    app.run_server(debug=True)