import altair as alt
import bokeh.plotting
import graphviz
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import pydeck as pdk
import requests
import streamlit as st
from vega_datasets import data


@st.experimental_memo
def create_pyplot():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    return fig


@st.experimental_memo
def create_plotly():
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length")
    return fig


@st.experimental_memo
def create_altair():
    source = data.cars()

    chart = (
        alt.Chart(source)
        .mark_circle()
        .encode(
            x="Horsepower",
            y="Miles_per_Gallon",
            color="Origin",
            tooltip=["Name", "Origin", "Horsepower", "Miles_per_Gallon"],
        )
        .interactive()
    )

    return chart


@st.experimental_memo
def create_vega_lite():
    chart_spec = {
        "mark": {"type": "circle", "tooltip": True},
        "encoding": {
            "x": {"field": "a", "type": "quantitative"},
            "y": {"field": "b", "type": "quantitative"},
            "size": {"field": "c", "type": "quantitative"},
            "color": {"field": "c", "type": "quantitative"},
        },
    }
    return chart_spec


@st.experimental_memo
def create_bokeh():
    df = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])

    p = bokeh.plotting.figure(
        title="simple line example", x_axis_label="x", y_axis_label="y"
    )

    p.line(df["a"], df["b"], legend_label="Temp.", line_width=2)
    return p


@st.experimental_memo
def create_pydeck():
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
    )
    chart = pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=df,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,
            ),
        ],
    )
    return chart


@st.experimental_memo
def create_graphviz():
    graph = graphviz.Digraph()
    graph.edge("run", "intr")
    graph.edge("intr", "runbl")
    graph.edge("runbl", "run")
    graph.edge("run", "kernel")
    graph.edge("kernel", "zombie")
    graph.edge("kernel", "sleep")
    graph.edge("kernel", "runmem")
    graph.edge("sleep", "swap")
    graph.edge("swap", "runswap")
    graph.edge("runswap", "new")
    graph.edge("runswap", "runmem")
    graph.edge("new", "runmem")
    graph.edge("sleep", "runmem")
    return graph


st.pyplot(create_pyplot())
st.plotly_chart(create_plotly())
st.altair_chart(create_altair())
df = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
st.vega_lite_chart(df, create_vega_lite())
# st.bokeh_chart(create_bokeh())
st.pydeck_chart(create_pydeck())
st.graphviz_chart(create_graphviz())
