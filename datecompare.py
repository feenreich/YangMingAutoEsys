from datetime import datetime
date_format = '%Y-%m-%d'
a = datetime.strptime('2008-8-18', date_format)
b = datetime.strptime('2008-9-26', date_format)
delta = b - a
print (delta.days)