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
    label = component.HtmlElement("truck_label", truck_details_panel)
    label.tag = "h1"
    label.content = "Hatjiekidee!"
  
    return payload

def gui_event(meta_data: dict, payload: dict) -> dict:
    """Process the events."""

    return payload
