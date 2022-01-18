import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output


df = px.data.tips()

app = dash.Dash(__name__)

server = app.server

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
        placeholder="Select type of graph to display",
        multi=False,
    ),
    html.Div(
    	dcc.Graph(
        	id='graph1',
        	className='pieplot',
        	style={'width':'600px','height':'450px'}
    	),
    	style={'display':'inline-block'}
),
    html.Div(
    	dcc.Graph(
        	id='graph2',
        	className='barplot',
        	style={'width':'600px','height':'450px'}
    	),
    	style={'display':'inline-block'}),

    
    html.Div(
    	dcc.Graph(
        	id='graph3',
        	className='Histogram',
        	style={'width':'600px','height':'450px'}
    	),
    	style={'display':'inline-block'}),

    html.Div(
    	dcc.Graph(
        	id='graph4',
        	className='scatterplot',
        	style={'width':'600px','height':'450px'}
    	),
    	style={'display':'inline-block'}),
    
    html.Div(
    	dcc.Graph(
        	id='graph5',
        	className='boxplot',
        	style={'width':'600px','height':'450px'}
    	),
    	style={'display':'inline-block'}),

    
    html.Div(
    	dcc.Graph(
        	id='graph6',
        	className='linechart',
        	style={'width':'600px','height':'450px'}
    	),
    	style={'display':'inline-block'}),

# style={'width': '41%', 'display': 'inline-block'}
])


@app.callback(
	Output('graph1', 'figure'),
    Input('dropdown', 'value'))
def update_figure(selected):
	if selected=='PC':
		df1 = df
		fig1 = px.pie(df1, values='tip', names='day', title='Day-wise tips')
		fig1.update_traces(textinfo='percent+label', marker=dict(colors=['gold', 'mediumturquoise', 'darkorange', 'lightgreen'], line=dict(color='#000000', width=2)))
		fig1.show()
	elif selected=='BC':
		dff2 = px.data.medals_long()
		fig2 = px.bar(dff2, x="medal", y="count", color="nation", text_auto=True)
		fig2.show()
	elif selected=='HIS':
		url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
		names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'diabetic']
		dff3 = pd.read_csv(url, names=names)
		fig3 = px.histogram(dff3, x='mass', color='diabetic', title='Histogram of diabetec people by BMI')
		fig3.show()
	elif selected=='SCAT':
		dff4 = px.data.iris()
		fig4 = px.scatter(
	        dff4, x="sepal_width", y="sepal_length", 
	        color="species", size='petal_length', 
	        hover_data=['petal_width'], title='Distribution of species per sepal')
		fig4.show()
	elif selected=='BOX':
		dff5 = df

	# Exclusive algorithm uses the median to divide the ordered dataset into two halves. 
	# If the sample is odd, it does not include the median in either half. 
	# Q1 is then the median of the lower half and Q3 is the median of the upper half.

		fig5 = px.box(df, x="day", y="total_bill", color="smoker", title='Boxlplot for smokers by bill paid on respective days')
		fig5.update_traces(quartilemethod="exclusive")
		fig5.show()
	elif selected=='LIN':
		dff6 = px.data.gapminder().query("continent == 'Oceania'")
		fig6 = px.line(dff6, x='year', y='lifeExp', color='country', markers=True)
		fig6.show()

# @app.callback(
# 	Output('graph1', 'figure'),
#     Input('dropdown', 'value'))
# def update_figure(selected_pie):
# 	df1 = df
# 	fig1 = px.pie(df1, values='tip', names='day', title='Day-wise tips')
# 	fig1.update_traces(textinfo='percent+label', marker=dict(colors=['gold', 'mediumturquoise', 'darkorange', 'lightgreen'], line=dict(color='#000000', width=2)))
# 	return fig1

# @app.callback(
# 	Output('graph2', 'figure'),
#     Input('dropdown', 'value'))
# def update_figure(selected_bar):
# 	dff2 = px.data.medals_long()
# 	fig2 = px.bar(dff2, x="medal", y="count", color="nation", text_auto=True, title='Total medals won by countries')
# 	return fig2

# @app.callback(
# 	Output('graph3', 'figure'),
#     Input('dropdown', 'value'))
# def update_figure(selected_hist):
# 	url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
# 	names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'diabetic']
# 	dff3 = pd.read_csv(url, names=names)
# 	fig3 = px.histogram(dff3, x='mass', color='diabetic', title='Histogram of diabetec people by BMI')
# 	return fig3

# @app.callback(
# 	Output('graph4', 'figure'),
#     Input('dropdown', 'value'))
# def update_figure(selected_scatter):
# 	dff4 = px.data.iris()
# 	fig4 = px.scatter(
#         dff4, x="sepal_width", y="sepal_length", 
#         color="species", size='petal_length', 
#         hover_data=['petal_width'], title='Distribution of species per sepal')
# 	return fig4

# @app.callback(
# 	Output('graph5', 'figure'),
#     Input('dropdown', 'value'))
# def update_figure(selected_box):
# 	dff5 = df

# 	# Exclusive algorithm uses the median to divide the ordered dataset into two halves. 
# 	# If the sample is odd, it does not include the median in either half. 
# 	# Q1 is then the median of the lower half and Q3 is the median of the upper half.

# 	fig5 = px.box(df, x="day", y="total_bill", color="smoker", title='Boxlplot for smokers by bill paid on respective days')
# 	fig5.update_traces(quartilemethod="exclusive")
# 	return fig5

# @app.callback(
# 	Output('graph6', 'figure'),
#     Input('dropdown', 'value'))
# def update_figure(selected_line):
# 	dff6 = px.data.gapminder().query("continent == 'Oceania'")
# 	fig6 = px.line(dff6, x='year', y='lifeExp', color='country', markers=True, title='Life expectancy per year from Oceania')
# 	return fig6

if __name__ == '__main__':
    app.run_server(debug=True)