# importing the profit loss csv from the project group folder to be read
from pathlib import Path
import csv
filepath = Path.cwd()/"C:/project_group/csv_reports/profit-and-loss-usd.csv"

def pl_difference ():
    '''
    This function has no parameters and will check all rows and data in the csv file to see if there are net profit deficits the following days
    and display them in a txt file
    '''
    # opening the csv file with mode "r" to access the data in the file
    with filepath.open(mode="r", encoding="UTF-8", newline="") as file:

        reader = csv.reader(file)
        # skipping the header
        next(reader)

        # assigning an empty list for day and net profit data
        pl_day = []
        
        # using a for loop to run through all rows in the file
        for row in reader:
            
            # appending the day and net profit data to the empty list
            pl_day.append([row[0], row[-1]])

            # assigning an empty list to store days where there is a deficit and its respective amount
            pl_defecit = []

            # using a for loop to run through all the data assigned to the list starting from 1
            for day in range(1 , len(pl_day)):
                
                # assigning a variable for the difference between 2 separate amounts on 2 days
                pl = int(pl_day[day-1][1]) - int(pl_day[day][1])
                
                # setting a condition if the amount on the current day is lower than the amount on the previous day,
                # it will append that day of the deficit and the calculated amount into the above empty list
                if int(pl_day[day][1]) < int(pl_day[day-1][1]):

                    number_of_days = pl_day[day][0]

                    pl_defecit.append([number_of_days,pl])
                
                # setting another condition that if for all days the net profit is higher on each day and the difference between
                # 2 amounts on any day is more than 0, a statement will be returned displaying the message
                elif int(pl_day[day][1]) > int(pl_day[day-1][1]) and pl > 0:

                    return "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"

        # assigning variables to display messages showcasing the days that deficit was present and their amounts for each day    
        write_text1 = f"[PROFIT DEFICIT] DAY: {pl_defecit[0][0]}, AMOUNT USD{pl_defecit[0][-1]}"
        write_text2 = f"[PROFIT DEFICIT] DAY: {pl_defecit[1][0]}, AMOUNT USD{pl_defecit[1][-1]}"
        
        # returning the messages back to the main program
        return f"{write_text1}\n{write_text2}"

#printing the function
print(pl_difference())


# opening a txt file named "summary_report" and appending the function to the file
with open("summary_report.txt" , "a") as file:
    file.write(pl_difference())
