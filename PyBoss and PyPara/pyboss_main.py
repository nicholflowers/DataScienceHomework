# import libraries
import os
import csv

 
# store path
csvpath1 = 'employee_data1.csv'

csvpath2 = 'employee_data2.csv'

 
# declare variables
emp_id = []

first_name = []

last_name = []

dob = []

ssn = []

state = []

 
# create dictionary of states 
us_state_abbrev = {

    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',

    'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',

    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',

    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN',

    'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',

    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',

    'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',

    'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX',

    'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',

    'Wisconsin': 'WI', 'Wyoming': 'WY',

}


# Read file
with open(csvpath1,'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)

 
    # loop through the read file
    for row in csvreader:

        # append employee id to a new list

        emp_id.append(row[0])

 
        # append first & last name to two separate lists

        name = row[1].split(" ") # splitting name by space

        first_name.append(name[0]) # append first name

        last_name.append(name[1]) # append last name

 
        # format & append dob

        bdate = row[2].split("-") # split dob by '-'

        new_db = bdate[1] + "/" + bdate[2] + "/" + bdate[0] # format dob

        dob.append(new_db) # appending formatted dob

 
        #format and append ssn

        ssn_split = row[3].split("-") # splitting ssn by '-'

        new_ssn = "***-**-" +ssn_split[2] # formatting ssn

        ssn.append(new_ssn) # appending formatted ssn

 
        # loop through states dict

        state.append(us_state_abbrev[row[4]])

 

# verify

# print(first_name[0])

# print(last_name[0])

# print(dob[0])

# print(ssn[0])

# print(state[0])

 
# zip data
employees = zip(emp_id, first_name, last_name, dob, ssn, state)

 

# create new csv file
output_file = 'employee_data_clean.csv'

 
# open + write the file
with open(output_file, 'w', newline = '') as csvfile:

    writer = csv.writer(csvfile, delimiter = ',')

 
    # write in headers
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # write data
    for employee in employees:

        writer.writerow(employee)