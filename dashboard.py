from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

def Dash_board(data):

    df = pd.DataFrame(data)

    app = Dash(__name__)

    # Dashboard layout
    app.layout = html.Div([
        html.H1("Job Statistics Dashboard", style={'textAlign': 'center', 'color': '#003366'}),
        html.Label("Select Job Title", style={'fontSize': 18, 'marginTop': 20}),

        dcc.Dropdown(
            id="job_dropdown",
            options=[{"label": job, "value": job} for job in sorted(df["Job_Title"].dropna().unique())],
            value=df["Job_Title"].dropna().unique()[0],
            clearable=False,
            style={'width': '50%', 'margin': '10px auto', 'fontSize': 16}
        ),

        dcc.Graph(
            id="job_stats_graph",
            style={"width": "75%", "height": "55vh", "margin": "auto"}
        )
    ], style={'backgroundColor': '#f0f8ff', 'padding': '20px'})

    @app.callback(
        Output("job_stats_graph", "figure"),
        Input("job_dropdown", "value")
    )
    def update_graph(selected_job):
        filtered_df = df[df["Job_Title"] == selected_job]

        metrics = ["Average_Salary", "Years_Experience", "AI_Exposure_Index",
                   "Tech_Growth_Factor", "Automation_Probability_2030"]
        values = [filtered_df[m].values[0] for m in metrics]

        # Assign distinct colors for each metric
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

        fig = px.bar(
            x=metrics,
            y=values,
            text=values,  # show values on bars
            color=metrics,  # each bar has a distinct color
            color_discrete_sequence=colors,
            labels={"x": "Metrics", "y": "Values"},
            title=f"Key Stats for {selected_job}"
        )

        # Update layout for visibility
        fig.update_traces(textposition='outside', textfont_size=14)
        fig.update_layout(
            plot_bgcolor='#e6f2ff',
            paper_bgcolor='#f0f8ff',
            font=dict(color='#003366', size=14),
            title_font_size=20,
            xaxis_tickangle=-30
        )

        return fig

    app.run(debug=False)
