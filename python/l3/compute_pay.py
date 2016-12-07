import sys

TAX_RATE = 0.20

def safe_open(filename, mode):
    '''Tries to open the given file.
    If successful, returns the file handle.
    If not, complains and exits'''
    
    try:
        handle = open(filename, mode)
    except Exception as e:
        sys.stderr.write('Can\'t open ' + filename + ':' + str(e) + '\n')
        sys.exit(1)
    return handle

# ITEM 3: read the employee file and get the hourly rates,
# indexed by employee ID

def get_hourly_rates(filename):
    hourly_rates = dict()
    rates = open(filename, 'r')
    line = rates.readline()
    while len(line) != 0:
      fields = line.split(':')

      employee_id = fields[0]
      rate = fields[3]
    
      hourly_rates[employee_id] = rate
      
      line = rates.readline()
  
    # ...
    return hourly_rates


def compute_pay(timesheet_filename, payroll_filename, employees):
    timesheet = safe_open(timesheet_filename, 'r')
    payroll = safe_open(payroll_filename, 'w')

    while True:
        hourly_rates = get_hourly_rates(employees)
        line = timesheet.readline()
        while '\n' in line or '\r' in line:
          line = line[:-1]
        if len(line) == 0:
            break
        fields = line.split(':')
        print fields

        # ITEM 4: only fields 0 and 1 have data in the new file format
       
        employee_id = fields[0] 
        hours_worked = 0
        try:
            hours_worked = float(fields[1])
        except ValueError:
            sys.stderr.write('bad number in timesheet file: ' + line)
      
        hourly_rate = float(hourly_rates[employee_id])
        if hours_worked <= 40:
            regular_hours = hours_worked
            overtime_hours = 0
        else:
            regular_hours = 40
            overtime_hours = hours_worked - 40

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        gross_pay = regular_pay + overtime_pay
        tax = gross_pay * TAX_RATE
        net_pay = gross_pay - tax

        # ITEM 5: The format for the payroll file has changed too!
        
        payroll.write(employee_id  + ':' +
                      str(gross_pay) + ':' + str(tax) + ':' + str(net_pay) + '\n')

    timesheet.close()
    payroll.close()

def main():
    # ITEM 2: Check sys.argv for THREE filenames,
    # or get them from the user
    if len(sys.argv) == 4:
      myTimeSheet = sys.argv[2]
      myPayroll = sys.argv[3]
      
      employees = sys.argv[1]
    
      compute_pay(myTimeSheet, myPayroll, employees)

if __name__ == '__main__':
    main()
