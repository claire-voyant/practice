import sys 
# ITEM 6 follows this line
# ITEM 9 follows this line
TAX_RATE = 0.20

timesheet = open("./timesheets.txt", 'r')

#ITEM 12 follows this line
payroll = open('payroll.txt', 'w')

while True:
    line = timesheet.readline()
    while '\n' in line or '\r' in line:
      line = line[:-1]
    if len(line) == 0:
        break
    fields = line.split(':')
    print fields
    last_name = fields[0]
    first_name = fields[1]
    try:
      hours_worked = float(fields[2])
      hourly_pay = float(fields[3])
    except ValueError:
      sys.stderr.write('Bad number in timesheet.txt. ' + line + '\n')
      hours_worked = 0
      hourly_pay = 0
   
    gross_pay = 0 
    if(hours_worked > 40) :
      gross_pay = (40 * hourly_pay) + ((hours_worked - 40) * hourly_pay *1.5)
    else:
      gross_pay = hours_worked * hourly_pay

    tax = gross_pay * TAX_RATE
    net_pay = gross_pay - tax;

    payroll.write(last_name + ':' + first_name + ':' + str(gross_pay) \
                    + ':' + str(tax) + ':' + str(net_pay) + '\n')

     

    

# ITEM 1 follows this line
    print line # ITEM 2

# ITEMS 2, 3 follow this line

# ITEMS 4, 5 follow this line

# ITEM 7 follows this line

# ITEM 8 follows this line

# ITEMS 10, 11, 12, 13 follow this line

timesheet.close()

payroll.close()
# ITEM 14 follows this line
