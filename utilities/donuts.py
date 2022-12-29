import plotly.graph_objects as go 
from utilities import utilities

# Stack value based on purchase price
buy = go.Figure(
    layout=go.Layout(
        template='plotly_dark',
        margin={'t': 25, 'b': 35, 'l': 25, 'r': 25},
        showlegend=False, 
        annotations=[
            dict(
                text=utilities.purchase_price,
                x=0.5,
                y=0.55,
                font=dict(
                    size=32,
                    color='white'
                ),
                showarrow=False),
            dict(
                text='PURCHASE PRICE',
                x=0.5,
                y=0.435,
                font_size=14,
                showarrow=False
            )
        ]
    )
)
buy.add_trace(
    go.Pie(
        labels=utilities.df['Type'],
        values=utilities.df['Purchase Price'],
        textinfo='none'
    )
)
buy.update_traces(
    hole=.8,
    # TODO: Hover template here
    hoverinfo='percent+value+label',
    marker=dict(
        colors=('gold', 'silver')
    )
)
buy.update_xaxes(automargin=True)
buy.update_yaxes(automargin=True)

# Stack value based on current spot price
spot = go.Figure(
    layout=go.Layout(
        template='plotly_dark',
        margin={'t': 25, 'b': 35, 'l': 25, 'r': 25},
        showlegend=False, 
        annotations=[
            dict(
                text=utilities.spot_price,
                x=0.5,
                y=0.55,
                font=dict(
                    size=32,
                    color='white'
                ),
                showarrow=False),
            dict(
                text='SPOT PRICE',
                x=0.5,
                y=0.435,
                font=dict(
                    size=14,
                    color='white'
                ),
                showarrow=False
            ),
            dict(
                text=utilities.gain_loss_text(utilities.gain_loss),
                x=0.5,
                y=0.365,
                font=dict(
                    size=14,
                    color=utilities.gain_loss_color(utilities.gain_loss)
                ),
                showarrow=False
            )
        ]
    )
)
spot.add_trace(
    go.Pie(
        labels=utilities.df['Type'],
        values=utilities.df['Spot Price'],
        textinfo='none'
    )
)
spot.update_traces(
    hole=.8,
    # TODO: Hover template here
    hoverinfo='percent+value+label',
    marker=dict(
        colors=('gold', 'silver')
    )
)
spot.update_xaxes(automargin=True)
spot.update_yaxes(automargin=True)