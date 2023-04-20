'''
Created on Oct 14, 2022
submitted: 10/13/22
@author: NSokol25
'''


def rightShift(word, moveright):
    '''
    

    
    shifts a word x characters right and replaces empties with #s to return word to original length
    Arg:
    
        word - word shifted right
        
        moveright - how many characters to move right
        
    Return:
    
        output: your word shifted right
    '''
    empties=''
    maxcounter = len(word) - moveright
    if maxcounter > 0:
        new_word = word[:maxcounter]
        counter = len(word) - len(new_word)
    else: 
        new_word = ''
        counter = len(word)
    while counter > 0:
        empties = empties + '#'
        counter -= 1
    output = empties + new_word 
    return output
word = rightShift('hio#', 1)
print(word)