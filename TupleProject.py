
#Exercise 1:

import urllib.request
def excersize_1():
    x = dict()
    frequency = int(input('which number would you like to see'))-1
    with urllib.request.urlopen('http://www.py4inf.com/code/mbox.txt') as txtfile:  #urllib request from #https://towardsdatascience.com/an-efficient-way-to-read-data-from-the-web-directly-into-python-a526a0b4f4cb
        for line in [str(i) for i in txtfile]:                      #iterates through file and converts line to str
            if 'From:' in line:                                     #finds right lines for assignment
                email = line.split(": ")[1]
                if email not in x:                                  #adds to dict if not in dict already
                    x[email] = 1
                else:                                               #if email in dict add one to frequency
                    x[email] += 1
    z = dict(sorted(x.items(), key = lambda x: x[1],reverse=True))  #sorts dict by frequency
    for iteration, email in enumerate(z):
        output = (email,z[email])                                   #iterates through dict and creates tuple(output)
        if iteration == frequency:
            break
    print(f'Email: {output[0]}Value: {output[1]}')


#Exercise 2:
def excersize_2():
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


#Exercise 3:
def excersize_3():
    x = dict()
    maxcount = 0
    acceptable_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    with urllib.request.urlopen('http://www.py4inf.com/code/mbox-short.txt') as txtfile:  #urllib request from #https://towardsdatascience.com/an-efficient-way-to-read-data-from-the-web-directly-into-python-a526a0b4f4cb
        for line in [str(i).replace("b'",'') for i in txtfile]:
            for letter in [letter.lower() for letter in line]:
                if letter in acceptable_letters:
                    if letter not in x:
                        x[letter] = 1
                    else:
                        x[letter] += 1
    for i in x.values():
        maxcount += i
    for key in sorted(x):
        print(f"letter: {key} ammount: {x[key]} percent: {x[key]/maxcount*100:.2f}%")


def main():
    excersize_1()
    excersize_2()
    excersize_3()



main()