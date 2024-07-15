from simian.gui import Form, component, component_properties, utils

def gui_init(meta_data: dict) -> dict:
    """Create a form and set a logo and title."""

    # Create form.
    form = Form()

    payload = {
        "form": form,
        "navbar": {
            "title": (
                f'<a class="text-white" href="https://github.com/Rolf-MP/simian-render" target="_blank">'
                '<i class="fa fa-github"></i></a>&nbsp;Simian on Render Test '
            )
        },
        "showChanged": True,
    }

    # Add large label
    label = component.HtmlElement("header", form)
    label.tag = "h1"
    label.content = "Hatjiekidee!"

    # Create plot with some initial data
    plot_obj_pie = component.Plotly("plot_pie", waypoints_panel)
    plot_obj_pie.aspectRatio = 3
    plot_obj_pie.addCustomClass("plotly-custom", "fixed-bottom")
    update_plot_pie(plot_obj_pie)
    
    return payload

def gui_event(meta_data: dict, payload: dict) -> dict:
    """Process the events."""

    return payload


def update_plot_pie(plot_obj_pie):

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    labels1 = ["US", "China", "European Union", "Russian Federation", "Brazil", "India", "Rest of World"]
    title_font_size = 20

    # Create subplots: use 'domain' type for Pie subplot
    plot_obj_pie.figure = make_subplots(rows=1, cols=4, specs=[[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}]])
    plot_obj_pie.figure.add_trace(go.Pie(labels=labels1, values=[16, 15, 12, 6, 5, 4, 42], name="GHG Emissions", title=dict(text='CHG', font_size=title_font_size), hole=.6, hoverinfo="label+percent+name"), 1, 1)
    plot_obj_pie.figure.add_trace(go.Pie(labels=labels1, values=[27, 11, 25, 8, 1, 3, 25], name="CO2 Emissions", title=dict(text='CO2', font_size=title_font_size), hole=.6, hoverinfo="label+percent+name"), 1, 2)

    plot_obj_pie.figure.add_trace(go.Sunburst(
        labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
        values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
    ), 1, 3)

    labels2 = ["Oxygen", "Hydrogen", "Carbon_Dioxide", "Nitrogen"]
    values2 = [4500, 2500, 1053, 500]
    colors2 = ["gold", "mediumturquoise", "darkorange", "lightgreen"]

    plot_obj_pie.figure.add_trace(go.Pie(
        labels=labels2,
        values=values2,
        marker=dict(colors=colors2, pattern=dict(shape=[".", "x", "+", "-"]))
    ), 1, 4)

    plot_obj_pie.figure.update_layout(
        title_text="Global Emissions 1990-2011",
        legend=dict(
            y=0,
            orientation="h",
            yanchor="bottom",
            yref="container"
        ),
        xaxis = dict(
            automargin = True
        ),
        yaxis = dict(
            automargin = True
        ),
        margin=dict(
          l= 20,
          r= 20,
          b= 0,
          t= 30,
          pad= 5
        )
    )
