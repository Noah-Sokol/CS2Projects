'''
Created on Sep 12, 2022
desc: Works as Post office cost calculator by geting user input to what item is, sorts the item, calculates the cost and prints either the cost or UNMAILABLE
last edited: 9/29/22
Bugs: None
@author: NoahSokol
'''


def main():
    '''
    Gets user input to what item is, sorts the item, calculates the cost and prints either the cost or UNMAILABLE
    '''
    length, height, thickness, returnzipcode, zipcode = getItem()
    objecttype = compare(length, height, thickness)
    cost = costCalculator(objecttype, zipcode, returnzipcode)
    if objecttype != ("UNMAILABLE"):print("your " + objecttype + " costs $" + cost)
    else: print("your object is UNMAILABLE")
    
    
def itemSplit(item):
    '''
        splits item into seprate variables
    
    #Arg:
     
        item - item is what the user inputed
        
    #returns:
    
        the length, height, thickness, returnzipcode, zipcode all split into seprate variables

    '''
    listitem = item.split(",")
    length = listitem[0]
    height = listitem[1]
    thickness = listitem[2]
    returnzipcode = listitem[3]
    zipcode = listitem[4]
    return length, height, thickness, returnzipcode, zipcode

def getItem():
    '''
        asks the user for the input of the item and makes sure the item is in the correct format then tests that the inputs work
        
    returns:
            length, height, thickness, returnzipcode, zipcode
    
    desc: 
        make sure length, height, thickness, returnzipcode, zipcode are all in the right format

    '''
    while True:
        item = input('please input the length, height, thickness,the zipcode you are sending from, the zipcode you are sending to\nin that exact format of your package: ')
        try:
            length, height, thickness, returnzipcode, zipcode = itemSplit(item)
            length = float(length)
            height  = float(height)
            thickness = float(thickness)
            zipcode = int(zipcode)
            returnzipcode = int(returnzipcode)
            break
        
        except IndexError: print ("Length, height, thickness, returnzipcode, or zipcode not in the right format")
        except ValueError: print('Please make sure the length, height, thickness, and zipcode are all numbers')
    return length, height, thickness, returnzipcode, zipcode

def compare(length, height, thickness):
    '''
        sorts the item into the correct catagory of package
        
    Args:
        length - used to sort into the right catagory
        height - used to sort into the right catagory
        thickness - used to sort into the right catagory
    
    
    Returns - objecttype - the right catagory of item
    '''

    if length >= 3.5 and length <= 4.25 and height >= 3.5 and height <= 6 and thickness >= .007 and thickness <= .016:
        objecttype = ('regular post card')
    elif length > 4.25 and length < 6 and height > 6 and height < 11.5 and thickness >= .007 and thickness <= .015:
        objecttype = ('large post card')
    elif length >= 3.5 and length <= 6.125 and height >= 5 and height <= 11.5 and thickness > .016 and thickness < .25:
        objecttype = ('envelope')
    elif length > 6.125 and length < 24 and height >= 11 and height <= 18 and thickness >= .25 and thickness <= .5:
        objecttype = ('large envelope')
    elif length >= 24 or height > 18 or thickness > .5:
        if length + thickness + thickness + height + height <= 84:
            objecttype = ('package')
        elif length + thickness + thickness + height + height > 84 and length + thickness + thickness + height + height < 130:
            objecttype = ('large package')
        else: objecttype = ('UNMAILABLE')
    else:   objecttype = ('UNMAILABLE')
    return objecttype

def zipCodeZone(zipcode):  
    '''
          sorts the zipcode into the right zone
    Arg:
            zipcode: used to sort zipcode into the right zone
        
    returns:
     
            zone: returns the zones the zipcode was in
    '''
    zipcode = int(zipcode)
    if zipcode >= 1 and zipcode <= 6999:
        zone = 1
    elif zipcode >= 7000 and zipcode <= 19999:
        zone = 2
    elif zipcode >= 20000 and zipcode <= 35999:
        zone = 3
    elif zipcode >= 36000 and zipcode <= 62999:
        zone = 4
    elif zipcode >= 63000 and zipcode <= 84999:
        zone = 5
    elif zipcode >= 85000 and zipcode <= 99999:
        zone = 6
    return zone

def costCalculator(objecttype,zipcode,returnzipcode):
    '''
    calculates how much the total cost of the item is 

    Args:
        
        objecttype: which type of object it is, ex. (regular post card)
        zipcode: which zipcode the user is sending to
        returnzipcode: which zipcode the user is sending from
        
    Returns:
        
        cost - the total cost (str)
    '''
    zone = zipCodeZone(zipcode)
    returnzone = zipCodeZone(returnzipcode)
    
    zonedifference = abs(zone-returnzone)

    if objecttype != "UNMAILABLE":
        print("your object is a " + objecttype)

        if objecttype == 'regular post card':
            cost = .20 + zonedifference * .03 
        elif objecttype == 'large post card':
            cost = .37 + zonedifference * .03
        elif objecttype == 'envelope':
            cost = .37 + zonedifference * .04
        elif objecttype == 'large envelope':
            cost = .60 + zonedifference * .05
        elif objecttype == 'package':
            cost = 2.95 + zonedifference * .25
        elif objecttype == 'large package':
            cost = 3.95 + zonedifference * .35 
        cost = float(cost)
        currency = ('{:.2f}'.format(cost))
        currency = str(currency)
        

        
    else: currency = 0
    
    return currency



        
while True:
    main()

'''
4,4,.009,023893,08515
5,7,.013,07245,45216
5,7,.2,45216,07245
10,12,.4,15623,89175
10,12,30,21505,72400

5,8,.011,02893,05426
7,10,.18,05906,12513
8.5,11,.36,75485,02888
20,20,40,92510,18236
10,20,30,94716,06510
'''