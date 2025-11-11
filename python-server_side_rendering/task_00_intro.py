#!/usr/bin/python3

def generate_invitations(template, attendees):
    if not template:
        raise TypeError("Empty template.")
    if not attendees:
        raise TypeError("Empty list.")
    if not isinstance(template, str):
        raise TypeError("Template must be a string")
    if not isinstance(attendees, list):
        raise TypeError("Attendees must be a list of dict")

    for attendee in attendees:
        if not isinstance(attendee, dict):
            raise TypeError("attendees must be a list of dict")
        try:
            invitation = template.format(**attendee)
        except KeyError as e:
            raise KeyError(f"key error: {e}")

        filename = f"invitation_{attendee.get('name', 'unknown')}.txt"
        with open(filename, 'w') as file:
            file.write(invitation)

        for index, attendee_data in enumerate(attendees, 1):
            required_keys = ["name", "event", "date", "location"]
            personalized_content = template

        for key in required_keys:
            value = attendee_data.get(key)
            if value is None:
                replacement = "N/A"
            else:
                replacement = str(value)

            placeholder = "{" + key + "}"
            personalized_content = personalized_content.replace
            (placeholder, replacement)

        output_filename = f"output_{index}.txt"

        try:
            with open(output_filename, 'w') as file:
                file.write(personalized_content)
            print(f"200 {output_filename}")
        except IOError as e:

            print(f"400 {output_filename}: {e}")
