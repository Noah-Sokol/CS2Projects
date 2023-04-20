'''
Created on Oct 10, 2022

@author: NSokol25
'''
def main():
    word = input('what word would you like to use ')
    moveleft = int(input('how much move left'))
    leftshift = leftShift(word,moveleft)
    print(leftshift)
def leftShift(word, moveleft):
    '''
        Shifts a word x characters to the left
    
    Args:
    
        word - the word you would like to shift left - str
    
        moveleft - how many characters to move left - int
    
    Returns:
    
        output: your word shifted to the left - str
    
    '''
    output = word[moveleft:]
    maxcounter = len(word) - len(output) 
    while maxcounter > 0:
        output = output + '#'
        maxcounter -= 1
    return output


main()
