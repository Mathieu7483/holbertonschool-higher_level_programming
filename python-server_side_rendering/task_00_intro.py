#!/usr/bin/python3
def generate_invitations(template, attendees):
    """Generates personalized invitation files from a given
    template and a list of attendee dictionaries."""
    if not isinstance(template, str):
        print("Invalid Input Types: Template must be a string.")
        return
    if not isinstance(attendees, list):
        print("Invalid Input Types: Attendees must be a list of dictionaries.")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index in enumerate(attendees, start=1):
        required_keys = ["name", "event_title", "event_date", "event_location"]

        invitation_text = template

        for placeholder in required_keys:
            value = index[1].get(placeholder, "N/A")
            if value is None or value == "":
                value = "N/A"

            invitation_text = invitation_text.replace(
                "{" + placeholder + "}", str(value))

        filename = f"output_{index}.txt"

        try:
            with open(filename, "w") as f:
                f.write(invitation_text)
        except Exception as e:
            print(f"Error writing {filename}: {e}")
