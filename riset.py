import re

txt = '# uwuwu'
x = re.search('#.*', txt) 

if (x):
  print("Yes, there is at least one match!", x.group())
else:
  print("No match")