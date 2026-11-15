

from datetime import date, datetime

from pasture_records_data import (
    display_formatted_row,
    paddocks,
    pasture_history,
)


# ------------------------ Additional functions -------------------------



# ---------------------------- Menu functions -----------------------------

def list_paddocks():
    """Display the supplied paddock records."""
    print("\nPADDOCKS")

    if len(paddocks) == 0:
        print("No paddocks are available.")
        return

    # Display paddock details including area and irrigated status.
    format_string = "{:<5} {:<16} {:<20} {:<30} {:<16}  {:<8}  {:<15}"
    display_formatted_row(
        ["ID", "Paddock", "Contact", "Email", "Phone", "Area_ha", "Irrigated_status"],
        format_string,
    )

    for paddock in paddocks:
        irrigated_status = "Yes" if paddock["irrigated"] else "No"
        display_formatted_row(
            [
                paddock["paddock_id"],
                paddock["paddock_name"],
                paddock["contact_name"],
                paddock["contact_email"],
                paddock["contact_phone"],
                paddock["area_ha"],
                irrigated_status
            ],
            format_string,
            )

    input("\nPress Enter to return to the menu.")    


def display_pasture_history_for_paddock():
    """Display the pasture history records for paddocks."""
    print("\nPASTURE HISTORY")
    if len(pasture_history) == 0:
        print("No pasture history is available.")
        return
    
    try:
        # Ask the user to select a paddock 
        history_paddock = int(input("Please enter a paddock ID:"))
        
        record = False
        format_string_history = "{:<12} {:<20} {:<25} {:<20}"
        display_formatted_row(
            ["Paddock_id", "Measurement_date", "Pasture_cover_kg_dm_ha", "Entered_by"],
            format_string_history
            )

        # Find and display records for the selected paddock
        for i in pasture_history:
            if i[0] == history_paddock:
                display_formatted_row(
                    [i[0],i[1],i[2],i[3]],
                    format_string_history
                )
                record = True

        # Inform the user if no records were found
        if not record:
            print("No records found for this paddock ID.")

    except ValueError:
        print("Please enter a valid paddock ID.")

    input("\nPress Enter to return to the menu.")  




def display_all_pasture_measurements():
    """Display all pasture measurements grouped by paddock."""
    print("\nPASTURE HISTORY")

    if len(pasture_history) == 0:
        print("No pasture measurements history is available.")
        input("\nPress Enter to return to the menu")
        return
    
    # Sort pasture measurements by paddock ID
    sorted_history = sorted(pasture_history, key=lambda record: record[0])

    #Get all unique paddock IDs
    paddock_ids = sorted(set(record[0] for record in sorted_history))
    for paddock_id in paddock_ids:
        paddock_name = ""
        for paddock in paddocks:
            if paddock["paddock_id"] == paddock_id:
                paddock_name = paddock["paddock_name"]
                break

        # Display paddock heading
        print(f'\nPaddock ID: {paddock_id} - {paddock_name}')

        format_string_display = "{:<20} {:<25} {:<20}"

        display_formatted_row(
            [
                "Measurement_date",
                "Pasture_cover_kg_dm_ha",
                "Entered_by"
            ],
            format_string_display
        )

        # Store pasture cover valuew for calculating the average
        pasture_covers = []

        #Display measurement for this paddock
        for record in sorted_history:
            if record[0] == paddock_id:
                display_formatted_row(
                    [
                        record[1],
                        record[2],
                        record[3]
                    ],
                    format_string_display
                )
                pasture_covers.append(record[2])

        # Calculate and display average pasture cover
        average_cover = sum(pasture_covers) / len(pasture_covers)
        print(f'\nAverage pasture cover: {average_cover:.2f} kg DM/ha')
    
    input("\nPress Enter to return to the menu.")  


def record_plate_meter_readings():
    """Record plate meter readings."""
    print("\nRecord plate meter readings")

    # Ask for the person's name only once
    while True:
        record_person = input("Please enter yur name(Firstname Lastname):").strip().title()
        name_parts = record_person.split()
        if len(record_person.split()) == 2 and all(part.isalpha() for part in name_parts):
            break    
        else:
            print("Please enter yur first and last name seperated with a space using letters only")

    # Keep asking for readings until the user enters X    
    while True:
        while True:
            record_paddock_input = input("Please enter a paddock ID (or X to exit):").strip()

            # Exit if user enters X
            if record_paddock_input.upper() == "X":
                input("\nPress Enter to return to the menu.")
                return
            try:
                record_paddock = int(record_paddock_input)

                if any(paddock["paddock_id"] == record_paddock for paddock in paddocks):
                    break
                else:
                    print("Invalid paddock ID. Please try again.")
            except ValueError:
                print("Please enter a valid paddock ID or X to exit.")

        # Ask for date
        while True:
            try:
                record_date = datetime.strptime(input("Please enter a date (YYYY-MM-DD): "), "%Y-%m-%d").date()
                if record_date <= date.today():
                    break
                else:
                    print("Date cannot be in the future. Please enter today or a past date.")
            except ValueError:
                print("Invalid date, please enter a date in format YYYY-MM-DD.")

        # Ask for pasture cover
        while True:
            try:
                record_pasture_cover = round(float(input("Please enter pasture cover:")),1)
                if record_pasture_cover >0:
                    break
                else:
                    print("Pastrure cover can't be zero or nagetive.")
            except ValueError:
                print("Please enter a valid number for pasture cover.")

    # Add the new measurement to pasturement to pasture_history
        pasture_history.append([
            record_paddock,
            record_date,
            record_pasture_cover,
            record_person
        ])
        print("Pasture measurement recorded successfully.")
        print(f"Paddock ID: {record_paddock}")
        print(f"Date: {record_date}")
        print(f"Pasture cover: {record_pasture_cover:.1f} kg DM/ha")
        print(f"Recorded by: {record_person}")           


def display_paddock_summary_report():
    """Display paddock summary report."""
    print("\nDISPLAY PADDOCK SUMMARY REPORT")

    if len(paddocks) == 0 and len(pasture_history) == 0:
        print("No paddock summary report availiable.") 
        return
    format_string_report = "{:<15} {:<20} {:<15} {:<15} {:<15} {:<15} {:<110}"
    display_formatted_row(
        [
            "Paddock ID", 
            "Paddock Name", 
            "Measurement",
            "Average",
            "Minimum", 
            "Max",
            "Status"
            ],
        format_string_report
    )

    # Keep track of paddocks that need follow_up
    follow_up_paddocks = []
    for paddock in paddocks:
        paddock_records = []

        # Find all measurements for this paddock
        for record in pasture_history:
            if record[0] == paddock["paddock_id"]:
                paddock_records.append(record)

        # Paddock has measurements       
        if len(paddock_records) > 0:

            # Get pasture cover values
            pasture_covers = [
                record[2] for record in paddock_records
            ]
            measurement_count = len(pasture_covers)
            average_cover = sum(pasture_covers) / measurement_count
            minimum_cover = min(pasture_covers)
            maximum_cover = max(pasture_covers)

            # Check whether average is below 1800
            if average_cover < 1800:
                status = "LOW"
                follow_up_paddocks.append(paddock)
            else:
                status = ""

            display_formatted_row(
                [
                    paddock["paddock_id"],
                    paddock["paddock_name"],
                    measurement_count,
                    f"{average_cover:.1f}",
                    f"{minimum_cover:.1f}",
                    f"{maximum_cover:.1f}",
                    status
                ],
                format_string_report
            )

        # Paddock has no measurements
        else:
            measurement_count = 0
            average_cover = "No Records"
            minimum_cover = "No Records"
            maximum_cover = "No Records"
            status = "No Records"

            follow_up_paddocks.append(paddock)

            display_formatted_row(
                [
                    paddock["paddock_id"],
                    paddock["paddock_name"],
                    measurement_count,
                    average_cover,
                    minimum_cover,
                    maximum_cover,
                    status  
                ],
                format_string_report
            )

    # Follow-up report
    print("\nFOLLOW-UP REPORT")

    if len(follow_up_paddocks) == 0:
        print("No paddocks require follow-up.")
    else:
        follow_up_format = "{:<12} {:<20} {:<25} {:<30} {:<20}"
        display_formatted_row(
            [
                "Paddock ID",
                "Paddock Name",
                "Contact Name",
                "Contact Email",
                "Conatct Phone"
            ],
            follow_up_format
        )

        for paddock in follow_up_paddocks:
            display_formatted_row(
                [
                    paddock["paddock_id"],
                    paddock["paddock_name"],
                    paddock["contact_name"],
                    paddock["contact_email"],
                    paddock["contact_phone"] if paddock["contact_phone"] else "None"
                ],
                follow_up_format
            )

    input("\nPress Enter to return to the menu.")
        


# ------------------------------ Main menu ------------------------------

# -------------- DO NOT MAKE CHANGES BELOW THIS POINT -------------- 

def display_menu():
    """Display the program menu."""
    print("\nLINCOLN UNIVERSITY PASTURE RECORDS")
    print("1 - List paddocks")
    print("2 - Display pasture history for a paddock")
    print("3 - Display all pasture measurements")
    print("4 - Record plate-meter readings")
    print("5 - Display paddock summary and follow-up report")
    print("Q - Quit")

# -------------- DO NOT MAKE CHANGES TO THE MENU -------------- 

def run_program():
    """Run the menu until the user chooses to quit."""
    menu_choice = ""

    while menu_choice.upper() != "Q":
        display_menu()
        menu_choice = input("Select an option: ").strip()

        if menu_choice == "1":
            list_paddocks()
        elif menu_choice == "2":
            display_pasture_history_for_paddock()
        elif menu_choice == "3":
            display_all_pasture_measurements()
        elif menu_choice == "4":
            record_plate_meter_readings()
        elif menu_choice == "5":
            display_paddock_summary_report()
        elif menu_choice != "Q":
            print("Select an option from 1 to 5, or Q to quit.")

    print("\nThank you for using Lincoln University Pasture Records.")


run_program()
