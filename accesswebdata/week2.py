import re

data=open("regex_sum_879485.txt")

sum1=0
for line in data:
    y=re.findall('[0-9]+', line)
    if len(y)!=0:
        for i in y:
            sum1+=int(i)

print(sum1)

