
#Exercise 1:

import urllib.request

x = dict()
frequency = int(input('which number would you like to see'))-1
with urllib.request.urlopen('http://www.py4inf.com/code/mbox.txt') as txtfile:  #urllib request from #https://towardsdatascience.com/an-efficient-way-to-read-data-from-the-web-directly-into-python-a526a0b4f4cb
    for line in [str(i) for i in txtfile]:
        if 'From:' in line:
            email = line.split(": ")[1]
            if email not in x:
                x[email] = 1
            else:
                x[email] += 1
z = dict(sorted(x.items(), key = lambda x: x[1],reverse=True))
for iteration, email in enumerate(z):
    output = (email,z[email])
    if iteration == frequency:
        break
print(f'Email: {output[0]}Value: {output[1]}')


#Exercise 2:
x = dict()
with urllib.request.urlopen('http://www.py4inf.com/code/mbox-short.txt') as txtfile:  #urllib request from #https://towardsdatascience.com/an-efficient-way-to-read-data-from-the-web-directly-into-python-a526a0b4f4cb
    for line in [str(i) for i in txtfile]:
        if 'From ' in line:
            hour = (line.split(":")[0])[-2::]
            if hour not in x:
                x[hour] = 1
            else:
                x[hour] += 1
for key in sorted(x):
    print(f'hour: {key} ammount: {x[key]}')
















