"""Supplied data and display helper for the pasture records program.

The paddock dictionaries represent rows returned by a PostgreSQL query that
uses dictionary-style output. The pasture tuples represent historical readings
already stored by the monitoring system.
"""

from datetime import date


paddocks = [
    {
        "paddock_id": 101,
        "paddock_name": "North 1",
        "area_ha": 8.4,
        "irrigated": True,
        "contact_name": "Aroha Ngata",
        "contact_email": "arohangata@example.nz",
        "contact_phone": "021 555 0142",
    },
    {
        "paddock_id": 205,
        "paddock_name": "South 2",
        "area_ha": 11.7,
        "irrigated": False,
        "contact_name": "Mika Jameson",
        "contact_email": "meeks1773@imail.co.nz",
        "contact_phone": "03 325 2811",
    },
    {
        "paddock_id": 317,
        "paddock_name": "Creek Flat",
        "area_ha": 6.25,
        "irrigated": True,
        "contact_name": "Mereana Ropata",
        "contact_email": "mere.ropata@notmail.com",
        "contact_phone": None,
    },
    {
        "paddock_id": 440,
        "paddock_name": "Hill Block",
        "area_ha": 14.0,
        "irrigated": False,
        "contact_name": "Jamie Taylor",
        "contact_email": "jt@taylorcontracting.co.nz",
        "contact_phone": "027 555 0198",
    },
]


# Each tuple contains:
# (paddock_id, measurement_date, pasture_cover_kg_dm_ha, entered_by)
pasture_history = [
    (101, date(2026, 7, 20), 2510.5, "Aroha Ngata"),
    (205, date(2026, 7, 20), 1940.0, "Aroha Ngata"),
    (317, date(2026, 7, 20), 1725.5, "Aroha Ngata"),
    (101, date(2026, 7, 27), 2380.75, "Mika Jameson"),
    (205, date(2026, 7, 27), 1815.25, "Mika Jameson"),
    (317, date(2026, 7, 27), 1680.0, "Mika Jameson"),
]


def display_formatted_row(row, format_string):
    """Display one list or tuple as a row of aligned columns.

    row contains the values to display, with one value for each column.
    format_string contains one set of curly braces for each column. For
    example, "{:<10}" creates a column 10 characters wide and pads unused
    positions with spaces.

    The alignment characters are:
        <  left aligned
        ^  centred
        >  right aligned

    This example creates three columns: left aligned and 5 characters wide,
    centred and 10 characters wide, and right aligned and 15 characters wide:
        format_string = "{:<5}  {:^10}  {:>15}"

    Make each column wider than its heading and its widest expected value;
    otherwise, longer text will make the columns appear out of alignment.

    A different padding character and separators can also be included. This
    example pads with full stops and separates the columns with vertical bars:
        format_string = "{:.<5} | {:.^10} | {:.>15}"

    Values are converted to strings for display. A None value is displayed as
    an empty string. 
    """
    # Build a new list of text values to build from each value in row.
    display_values = []

    # Convert each value to text, using an empty string for a missing value.
    for value in row:
        if value is None:
            display_values.append("")
        else:
            display_values.append(str(value))

    # Apply the formatting in format_string to all items in row    
    # * supplies each value to the corresponding set of braces in format_string.
    print(format_string.format(*display_values))
