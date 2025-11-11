#!/usr/bin/python3

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError("Template must be a string")
    if not isinstance(attendees, list):
        raise TypeError("Attendees must be a list of dict")

    if not template:
        raise TypeError("Template is empty, no output files generated.")

    if not attendees:
        raise TypeError("No data provided, no output files generated.")
    
    for attendee in attendees:
        if not isinstance(attendee, dict):
            raise TypeError("Each attendee must be a dictionary")
        try:
            invitation = template.format(**attendee)
        except KeyError as e:
            raise KeyError(f"Missing key in attendee data: {e}")

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
            personalized_content = personalized_content.replace(placeholder, replacement)

        output_filename = f"output_{index}.txt"
        
        try:
            with open(output_filename, 'w') as file:
                file.write(personalized_content)
            print(f"Successfully generated {output_filename}") 
        except IOError as e:
    
            print(f"Error writing to file {output_filename}: {e}")