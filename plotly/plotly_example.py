# Get this figure: fig = py.get_figure("https://plot.ly/~MattSundquist/1056/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~MattSundquist/1056/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="Number of University Graduates", fileopt="extend"))
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~MattSundquist/1056/").get_data()[0]["y"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
# py.sign_in('username', 'api_key')
trace1 = Bar(
    x=['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012'],
    y=['1.1', '1.5', '2.1', '2.8', '3.4', '4.1', '5.0', '5.6', '6.1', '6.3', '6.6', '6.8'],
    marker=Marker(
        color='rgb(222, 113, 88)'
    ),
    name='China',
    uid='368324'
)
trace2 = Bar(
    x=['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012'],
    y=['1.3', '1.2', '1.3', '1.4', '1.5', '1.5', '1.5', '1.6', '1.6', '1.7', '1.7', '1.8'],
    marker=Marker(
        color='rgb(84, 172, 234)'
    ),
    name='U.S.',
    uid='25a4e9'
)
data = Data([trace1, trace2])
layout = Layout(
    annotations=Annotations([
        Annotation(
            x=0.1000000000000038,
            y=0.5709595420143821,
            align='center',
            arrowcolor='rgba(0, 0, 0, 0)',
            arrowhead=1,
            arrowsize=1,
            arrowwidth=0,
            ax=436,
            ay=155.98332977294922,
            bgcolor='rgba(0,0,0,0)',
            bordercolor='',
            borderpad=1,
            borderwidth=1,
            font=Font(
                color='',
                family='',
                size=0
            ),
            opacity=1,
            showarrow=True,
            text='Source: <a href="http://qz.com/187350/six-charts-that-show-why-china-is-competing-with-the-multinationals-it-used-to-work-for/">Quartz</a>',
            xanchor='auto',
            xref='paper',
            yanchor='auto',
            yref='paper'
        )
    ]),
    autosize=False,
    bargap=0.1,
    bargroupgap=0.15,
    barmode='group',
    boxgap=0.3,
    boxgroupgap=0.3,
    boxmode='overlay',
    dragmode='zoom',
    font=Font(
        color='rgb(33, 33, 33)',
        family="'Open sans', verdana, arial, sans-serif",
        size=12
    ),
    height=400,
    hidesources=False,
    hovermode='x',
    legend=Legend(
        x=0.001851851851851852,
        y=0.9863636363636363,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(0, 0, 0, 0)',
        borderwidth=1,
        font=Font(
            color='',
            family='',
            size=0
        ),
        traceorder='normal',
        xanchor='auto',
        yanchor='auto'
    ),
    margin=Margin(
        r=80,
        t=100,
        autoexpand=True,
        b=80,
        l=80,
        pad=0
    ),
    paper_bgcolor='#fff',
    plot_bgcolor='#fff',
    separators='.,',
    showlegend=True,
    smith=False,
    title='<br> # OF UNIVERSITY GRADUATES IN CHINA VS. U.S. (MILLIONS)',
    titlefont=dict(
        color='',
        family='',
        size=0
    ),
    width=700,
    xaxis=XAxis(
        anchor='y',
        autorange=True,
        autotick=True,
        domain=[0, 1],
        dtick=1,
        exponentformat='e',
        gridcolor='#ddd',
        gridwidth=1,
        linecolor='#000',
        linewidth=1,
        mirror=False,
        nticks=17,
        overlaying=False,
        position=0,
        range=[2000.5, 2012.5],
        rangemode='normal',
        showexponent='all',
        showgrid=False,
        showline=True,
        showticklabels=True,
        tick0=2001,
        tickangle='auto',
        tickcolor='#000',
        tickfont=dict(
            color='',
            family='',
            size=0
        ),
        ticklen=5,
        ticks='',
        tickwidth=1,
        title="<i>Data: Solidiance's Analysis</i>",
        titlefont=dict(
            color='',
            family='',
            size=0
        ),
        type='linear',
        zeroline=False,
        zerolinecolor='#000',
        zerolinewidth=1
    ),
    yaxis=YAxis(
        anchor='x',
        autorange=True,
        autotick=True,
        domain=[0, 1],
        dtick=2,
        exponentformat='e',
        gridcolor='#ddd',
        gridwidth=1,
        linecolor='#000',
        linewidth=1,
        mirror=False,
        nticks=0,
        overlaying=False,
        position=0,
        range=[0, 7.157894736842105],
        rangemode='normal',
        showexponent='all',
        showgrid=True,
        showline=True,
        showticklabels=True,
        tick0=0,
        tickangle='auto',
        tickcolor='#000',
        tickfont=dict(
            color='',
            family='',
            size=0
        ),
        ticklen=5,
        ticks='',
        tickwidth=1,
        title='',
        titlefont=dict(
            color='',
            family='',
            size=0
        ),
        type='linear',
        zeroline=False,
        zerolinecolor='#000',
        zerolinewidth=1
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)

print('URL: {}'.format(plot_url))

