'''
Created on Nov 3, 2022

@author: NSokol25
'''

def get_square_root(e,p,n):
    thing = ((2*e)-n)
    if  thing < p:
        return e
    else: return get_square_root(n,p,(e+n)/e)/2
    
def main():
    e = float(input('e'))
    p = float(input('p'))
    n = float(input('n'))
    output = get_square_root(e,p,n)
    print(output)

main()