# importing the overheads csv from the project group folder to be read
from pathlib import Path
import csv
filepath = Path.cwd()/"C:/project_group/csv_reports/overheads-day-90.csv"

def overheads_highest():
    '''
    This function has no parameters and will check all rows and data in the csv file to see if there are cash deficits the following days
    and display them in a txt file
    '''
    # opening the csv file with mode "r" to access the data in the file
    with filepath.open(mode="r", encoding="UTF-8", newline="") as file:

        reader = csv.reader(file)
        # skipping the header
        next(reader)

        # assigning variables for the category with the highest overhead and starting them from 0
        highest_cat = ""
        overhead = 0
        
        # using a for loop to run through all the data in the file
        for row in reader:
            
            # setting a condition to find the highest value amongst all the overheads, and assigning the value and respective category
            # to variables to be printed
            if float(row[1]) > overhead:
                
                highest_cat = row[0]
                overhead = float(row[1])
        
        # assigning a variable to the statement showcasing the highest overhead and its category
        write_text = (f"[HIGHEST OVERHEADS] {highest_cat.upper()}: {overhead}%")
        
        # returning the statement
        return write_text

# printing the function
print(overheads_highest())

# opening a txt file named "summary_report" and appending the function to the file
with open("summary_report.txt" , "a") as file:
    file.write(overheads_highest())
    cheryl
