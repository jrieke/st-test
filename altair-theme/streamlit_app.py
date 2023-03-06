import altair as alt
import pandas as pd
import streamlit as st


def snowflake_theme():
    font = "Lato"
    fillColor = "#F0F2F6"
    primary_color = "#29B5E8"
    font_color = "#11567F"
    base_size = 16
    lg_font = base_size * 1.25
    sm_font = base_size * 0.8  # st.table size

    main_palette = [
        "#29B5E8",
        "#11567F",
        "#000000",
        "#71D3DC",
        "#FF9F36",
        "#D45B90",
        "#7DD44CF",
        "#8A999E",
    ]
    main_palette_with_thirds = [
        "#29B5E8",
        "#11567F",
        "#000000",
        "#71D3DC",
        "#FF9F36",
        "#D45B90",
        "#7DD44CF",
        "#8A999E",
        "#29B5E8",
        "#11567F",
        "#29B5E8",
    ]

    sequential_palette = [
        "#29B5E8",
        "#27ACDE",
        "#25A4D5",
        "#229BCB",
        "#2092C2",
        "#1E8AB8",
        "#1C81AF",
        "#1A79A5",
        "#18709C",
        "#156792",
        "#135F89",
        "#11567F",
    ]
    theme_dict = {
        "config": {
            "view": {"fill": fillColor},
            "arc": {"fill": primary_color},
            "bar": {"fill": primary_color},
            "area": {"fill": primary_color},
            "circle": {"fill": primary_color, "stroke": font_color, "strokeWidth": 0.5},
            "line": {"stroke": primary_color},
            "path": {"stroke": primary_color},
            "point": {"filled": True},
            "rect": {"fill": primary_color},
            "shape": {"stroke": primary_color},
            "symbol": {"fill": primary_color},
            "title": {
                "font": font,
                "color": font_color,
                "fontSize": lg_font,
                "anchor": "start",
            },
        },
        "axis": {
            "titleFont": font,
            "titleColor": font_color,
            "titleFontSize": sm_font,
            "labelFont": font,
            "labelColor": font_color,
            "labelFontSize": sm_font,
            "grid": True,
            "gridColor": "#fff",
            "gridOpacity": 1,
            "domain": False,
            "tickColor": font_color,
        },
        "header": {
            "labelFont": font,
            "titleFont": font,
            "labelFontSize": base_size,
            "titleFontSize": base_size,
        },
        "legend": {
            "titleFont": font,
            "titleColor": font_color,
            "titleFontSize": sm_font,
            "labelFont": font,
            "labelColor": font_color,
            "labelFontSize": sm_font,
        },
        "range": {
            "category": main_palette,
            "diverging": sequential_palette,
            "heatmap": main_palette_with_thirds,
            "ramp": sequential_palette,
            "ordinal": sequential_palette,
        },
        "bar": {
            "size": 40,
            "binSpacing": 1,
            "continuousBandSize": 30,
            "discreteBandSize": 30,
            "fill": "#F0F0F0",
            "stroke": False,
        },
    }
    print(theme_dict)
    return theme_dict


# register the custom theme under a chosen name
alt.themes.register("snowflake", snowflake_theme)
# enable the newly registered theme
alt.themes.enable("snowflake")

source = pd.DataFrame(
    {
        "a": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
        "b": [28, 55, 43, 91, 81, 53, 19, 87, 52],
    }
)
chart = alt.Chart(source).mark_bar().encode(x="a", y="b")
st.altair_chart(chart)
