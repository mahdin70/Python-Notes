
# Pythin has a module called "datetime" to work with dates 
# It's not a data type 

import datetime

z = datetime.datetime.now()
print(z)

# Output : -> 2022-05-12 19:31:40.341024
# Output contains Year-Month-Date Hour:Minute:Second.Milisecond


# Date Time methods to use in print(x.strftime(""))


#  %a	Weekday, short version	               Wed	
#  %A	Weekday, full version	               Wednesday	
#  %w	Weekday as a number 0-6, 0 is Sunday   3	
#  %d	Day of month 01-31	                   31	
#  %b	Month name, short version	           Dec	
#  %B	Month name, full version	           December	
#  %m	Month as a number 01-12                12	
#  %y	Year, short version, without century   18