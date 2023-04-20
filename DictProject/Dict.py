'''
Created on Sep 12, 2022
desc: creates output csv file from txt file then graphs csv file using dicts 
last edited: 3/8/23
Bonus: used matplotlib instead of exel
Bugs: None
@author: NoahSokol
'''


import matplotlib.pyplot as plt
import string


def create_dict():
    '''
        Creates main dictionary(counts) by iterating through txt file
    
    returns:
        counts - dict - dictionary with all words and sorted by quantity
    '''
    counts = dict()
    with open("DictProject\A_Midsummer_Night's_Dream.txt") as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.translate(str.maketrans('','',string.punctuation)).translate(str.maketrans('','','1234567890')).lower()#https://stackoverflow.com/questions/23175809/str-translate-gives-typeerror-translate-takes-one-argument-2-given-worked-i deletes punctuation and numbers
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] += 1
    return dict(sorted(counts.items(), key = lambda x: x[1],reverse=True))

def write_to_output(counts):
    '''
        writes to the output file and doesn't write bad words

    Args:
        counts - dict - dictionary with all words and sorted by quantity
    '''
    common_words = ['my','how','go','let','there','an','never','may','these','our','oberon','one','thisbe','would','see','titania','did','hath','some','we','bottom','here','now','o','am','come','pyramus','puck','quince','must','enter','demetrius','lysander','hermia','theseus','shall','helena','all','than','can','should','make','which','when','by','your','do','no','what','if','will','more','their','nor','yet','or','then','not','but','me','thee','so','thy','thou','the','of','and','a','to','in','is','you','that','it','he','was','for','on','are','as','with','his','they','at','be','this','have','from','i']
    with open("DictProject\DictGraph.csv",'a',newline='') as outputFile:
        for word in counts:
            if counts[word] > 20 and word not in common_words:
                outputFile.write((str(((word),(counts[word])))+'\n').replace(')','').replace('(','').replace("'",'').replace('"',''))

def get_data(counts):
    '''
        Sorts the data into names, values for graphing

    Args:
        counts - dict - dictionary with all words and sorted by quantity
    
    Returns:
        amount_of_words - int - how many words the user wants to graph
        names - list - list of all words
        values - list - list of all the quantities
    '''
    names =list()
    values = list()
    amount_of_words = int(input('please input how many words you would like to graph '))
    with open("DictProject\DictGraph.csv",'r',newline='') as readfile:
        for count,line in enumerate(readfile):
            names.append(str(line.split(',')[0]))
            values.append(counts[names[count]])
            if count == amount_of_words:
                break
    return amount_of_words, names, values

def create_graph(amount_of_words, names, values):
    '''
        Creates and shows the graph using matplotlib

    Arg:
    amount_of_words - int - how many words the user wants to graph
    names - list - list of all words
    values - list - list of all the quantities
    '''
    plt.bar(range(len(names)), values, tick_label=names)
    plt.title(label = str(amount_of_words) + " common words in A Midsummer Night's Dream", fontdict=None, loc='center', pad=None)
    plt.show()

def main():
    counts = create_dict()
    write_to_output(counts)
    amount_of_words, names, values = get_data(counts)
    create_graph(amount_of_words, names, values)
    open("DictProject\DictGraph.csv",'w',newline='')


main()
