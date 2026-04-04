#!/usr/bin/python3
"""Module for generating invitation files from a template."""


def generate_invitations(template, attendees):
    """Generate invitation files from a template and list of attendees."""
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    if not isinstance(attendees, list) or not all(
        isinstance(a, dict) for a in attendees
    ):
        print("Error: Attendees is not a list of dictionaries.")
        return
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, 1):
        output = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output = output.replace("{" + key + "}", str(value))
        with open("output_{}.txt".format(i), "w") as f:
            f.write(output)
