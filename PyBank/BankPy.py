import os
import csv

bd_1 = os.path.join( "budget_data_1.csv")
bd_2 = os.path.join( "budget_data_1.csv")

total_number_months = 0
ttl_revenue = 0
previous_row = 0
changes_monthly = 0
total_changes = 0

mon_chan_dr = {}

with open(bd_1, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)

        for row in csvreader:
            FD = row[0]
            FR = row[1]

            total_number_months = total_number_months + 1
            ttl_revenue = ttl_revenue + int(FR)
            changes_monthly = int(FR) - previous_row
            previous_row = int(FR)

            if (total_number_months > 1):
                MMC[FD] = changes_monthly

        monthly_changes = (sum(MMC.values()))
        monthly_averages = int(monthly_changes)/int(total_number_months)
