# Pasture Records Management System
## Project Overview
The Pasture Records Management System is a Python-based application developed to manage paddock and pasture information efficiently. It allows users to maintain pasture records, monitor pasture conditions, and review historical information through a menu-driven interface. The system focuses on organising pasture data, improving record management, and providing useful summaries to support pasture monitoring.

## Features
Paddock Management: Manage paddock information and related pasture records.
Pasture Record Management: Record and maintain pasture information.
Historical Records: Keep track of previous pasture records for reference.
Data Validation: Validate user inputs to help maintain accurate records.
Exception Handling: Handle invalid inputs and unexpected errors.
Statistical Summaries: Calculate average, minimum, and maximum values to help analyse pasture information.
Menu-Driven Interface: Provide a straightforward way for users to navigate the system and access its functions.

## Technologies Used
Python
Data structures and functions
Input validation
Exception handling

## Key Learning Outcomes
Through this project, I developed practical programming skills in:
Designing and developing a menu-driven Python application.
Managing and organising structured data.
Implementing input validation and exception handling.
Performing calculations and generating statistical summaries.
Developing logical solutions to practical record-management requirements.

## How to Run
Clone or download this repository.
Open the project folder in Visual Studio Code or another Python development environment.
Run the main Python file.
Follow the menu instructions to interact with the system.

## Project Purpose
This project demonstrates the application of Python programming concepts to a practical pasture record-management scenario, with an emphasis on data organisation, validation, and basic statistical analysis.

## Test normal input
| Feature/Function Tested               | Purpose of Test       | Input/Starting Data | Expected Result                    | Actual Result                                     |
| list_poddocks()                       | Test normal selection | 1           | Display paddocks details: ID, name, contact| Paddocks details displayed: ID,name, contact      |
                                                                              | email, phone, area, irrigated status       | email, phone, area, irrigated status              |
| list_poddocks()                       | Test normal return    | Enter(any value) | Go back to the main menu              | Went back to the main menu                        |
| display_pasture_history_for_paddock() | Test normal selection | 2       | Ask for a paddock ID                            | Asked for a paddock ID                           |
| display_pasture_history_for_paddock() | Test normal ID        | 101     | Display all paddock 101 records with:           | Displayed all paddock 101 records with:          |
                                                                          | measured date, pasture cover, reocrded person   | measured date, pasture cover, reocrded person    |
| display_pasture_history_for_paddock() | Test normal return    |Enter(any value)| Go back to the main menu                 | Went back to the main menu                       |
| display_all_pasture_measurements()    | Test normal selection | 3       | Display all records with ID, name as heading,   | Displayed all records with ID, name as heading,  |
                                                                          | listed with measured date, pasture cover, person| listed with measured date, pasture cover, person |
| display_all_pasture_measurements()    | Test normal return    |Enter(any value)| Go back to the main menu                 | Went back to the main menu                       |
| record_plate_meter_readings()         | Test normal selection | 4       | Ask for a first and a last name                | Asked for a first and a last name                 |
| record_plate_meter_readings()         | Test normal name      | m p     | Accept name, ask for a paddock ID or X to exit | Accepted name, asked for a paddock ID or X to exit|
| record_plate_meter_readings()         | Test normal ID        | 317     | Accept Paddock ID, ask for a date              | Accepted Paddock ID, asked for date               |
| record_plate_meter_readings()         | Test normal date          | 2026-09-01      | Accept date, ask for a pasture cover     | Accepted date, asked for a pasture cover    |
| record_plate_meter_readings()         | Test normal pasture cover | 1235.5          | Accept cover, display record details,    | Accepted cover, displayed record details,   |
                                                                                      | and ask for a paddock ID or X to exit    | and asked for a paddock ID or X to exit     |
| record_plate_meter_readings()         | Test normal exit      | x        | Exit, ask for Enter to return to menu     | Exited, asked for Enter to return to menu             |
| record_plate_meter_readings()         | Test normal return    |Enter(any value)| Go back to the main menu            | Went back to the main menu                            |
| display_paddock_summary_report()      | Test normal selection | 5       | Display paddocks summary report with ID, name,  | Display paddocks summary report with ID, name,   |
                                                                          | number of measurements, average, minimum and    | number of measurements, average, minimum and     |
                                                                          | maximum pasture covers, and cover status.       | maximum pasture covers, and cover status.        |
| display_paddock_summary_report()      | Test normal return    |Enter(any value)| Go back to the main menu                 | Go back to the main menu                         |
| exit Pasture Records System           | Test normal quit      | q                | Exit Pasture Records System             | Exited Pasture Records System                   |

### Test invalid input
| Feature/Function Tested         | Purpose of Test        | Input/Starting Data | Expected Result                           | Actual Result                               |
| Main menu                       | Test invalid selection | 6 (invalid numbers) | Remind to select from 1 to 5 or Q to quit | Reminded to select from 1 to 5 or Q to quit |
| Main menu                       | Test invalid selection | a (invalid letters) | Remind to select from 1 to 5 or Q to quit | Reminded to select from 1 to 5 or Q to quit |
| Main menu                       | Test invalid selection | + (invalid symbols) | Remind to select from 1 to 5 or Q to quit | Reminded to select from 1 to 5 or Q to quit |
| display_pasture_history_for_paddock()| Test invalid ID | 769 (invalid ID) | Display no records for this ID           | Displayed no records for this ID                  |
| display_pasture_history_for_paddock()| Test invalid ID | -10 (invalid ID) | Display no records for this ID           | Displayed no records for this ID                  |
| display_pasture_history_for_paddock()| Test invalid ID | gyh (value error)| Ask for a valid paddock ID               | Asked for a valid paddock ID                      |
| display_pasture_history_for_paddock()| Test invalid ID | +_- (value error)| Ask for a valid paddock ID               | Asked for a valid paddock ID                      |
| record_plate_meter_readings()        | Test invalid name | meg     | Ask for a full name with a space in between     | Asked for a full name with a space in between     |  
| record_plate_meter_readings()        | Test invalid name | meg p y | Ask for a full name with a space in between     | Asked for a full name with a space in between     |  
| record_plate_meter_readings()        | Test invalid name | 125     | Ask for a full name with a space in between     | Asked for a full name with a space in between     | 
| record_plate_meter_readings()        | Test invalid name | meg p y | Ask for a full name with a space in between     | Asked for a full name with a space in between     | 
| record_plate_meter_readings()        | Test invalid name | 12 5    | Ask for a formated full name                    | Asked for a formated full name                    | 
| record_plate_meter_readings()        | Test invalid ID   | ghu (type error) | Ask for a valid ID or X to exit        | Asked for a valid ID or X to exit                 | 
| record_plate_meter_readings()        | Test invalid ID   | -10 (value error)| Display invalid ID and try again       | Displayed invalid ID and try again                |
| record_plate_meter_readings()        | Test invalid ID   | _(* (type error) | Display invalid ID and try again       | Displayed invalid ID and try again                |  
| record_plate_meter_readings()        | Test invalid date | 2028-03-01       | Display date can't be in furture       | Display date can't be in furture                  |
| record_plate_meter_readings()        | Test invalid date | 2026-02-31       | Display invalid date and remind format | Displayed invalid date and reminded format        |
| record_plate_meter_readings()        | Test invalid date | 2026             | Display invalid date and remind format | Displayed invalid date and reminded format        |
| record_plate_meter_readings()        | Test invalid date | 2026/03/01       | Display invalid date and remind format | Displayed invalid date and reminded format        |
| record_plate_meter_readings()        | Test invalid date | 2026-26-01       | Display invalid date and remind format | Displayed invalid date and reminded format        |
| record_plate_meter_readings()        | Test invalid date | 01-09-2026       | Display invalid date and remind format | Displayed invalid date and reminded format        |
| record_plate_meter_readings()        | Test invalid pasture cover | dbs(type error)| Ask for a valid number for pastrue cover| Asked for a valid number for pastrue cover|
| record_plate_meter_readings()        | Test invalid pasture cover | =-(type error) | Ask for a valid number for pastrue cover| Asked for a valid number for pastrue cover|


### Test boundary input
| Feature/Function Tested         | Purpose of Test     | Input/Starting Data    | Expected Result                         | Actual Result                                  |
| record_plate_meter_readings()   | Test boundary ID    | 0 (value error)        | Display invalid ID and try again        | Displayed invalid ID and try again             | 
| record_plate_meter_readings()   | Test boundary pasrure cover | 0 (value error)| Display input can't be zero or negative | Display input can't be zero or negative format |
| display_pasture_history_for_paddock()| Test boundary ID | 0 (invalid ID)       | Display no records for this ID          | Displayed no records for this ID               |


### Test empty/no-data input
| Feature/Function Tested         | Purpose of Test          | Input/Starting Data | Expected Result                    | Actual Result                                    |
| record_plate_meter_readings()   | Test empty ID            | empty/no-data       | Display invalid ID and try again   | Displayed invalid ID and try again               | 
| record_plate_meter_readings()   | Test empty pasture cover | empty/no-data       | Ask for a valid number for pastrue cover | Asked for a valid number for pastrue cover | 
| display_pasture_history_for_paddock()| Test empty ID       | empty/no-data       | Ask for a valid paddock ID         | Asked for a valid paddock ID                     |

