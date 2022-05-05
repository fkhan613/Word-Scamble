import random
import time

def scramble():
    # a list of punctuation to look out for (optional)
    punc = (',','.',';',':','!','?',"'")

    # prompt the user
    print('\nPlease enter some text for me to scramble:\n')
    txt = input()
    print('\nThank you\n')
    time.sleep(1)

    # break up the word list up on the spaces
    word_lst = txt.split()

# optional section to handle the punctuation and not have it count in the word length.
    for p in punc:
        # create a list to work with
        working = []
        # go through each word, at this point there may be punctuation attached
        for out in word_lst:
            # break up words on from the punctuation
            for o in out.split(p):
                # if split found a match, the contents of o will have zero length
                if len(o) == 0:
                    # add the punctuation back in as its own list element
                    working.append(p)
                else:
                    # add the list to the words
                    working.append(o)
        # overwirte the word list with the new changes from the extra punctuation elements
        word_lst = working
# end of optional punctuation section
       
    # declare an empty string to build the output on
    output_txt = ''

    # go through each word in the word list
    for word in word_lst:
        # measure the word
        word_length = len(word)

        # make the scrambled word the same as the word to be able to enter the loop
        scrmbld_word = word

        # no sense scrambling words less than 4 char long
        if word_length >= 4:
            tries = 0 # prevents being stuck in an infinite loop for words like 'doom'
            # scamble the middle letters until they no longer match the original word
            # or ten attempts have happened
            while scrmbld_word == word and tries < 10:
                tries += 1 # prevents being stuck in an infinite loop for words like 'doom'
                # extract and save the middle letters
                middle_ltrs = list(word[1:word_length-1])
                # set the first letter of the scrambled word to the same as the original word
                scrmbld_word = word[0]
               
                while len( middle_ltrs ) > 0:
                    # choose a letter of the middle letters
                    ltr = random.choice(middle_ltrs)
                    # find the index of the found letter from the list
                    ltr_indx = middle_ltrs.index( ltr )
                    # remove the chosen letter from the list of middle letters
                    middle_ltrs.pop( ltr_indx )
                    # add the chosen letter to the scrambled word
                    scrmbld_word += ltr

                # set the last letter of the scrambled word to the same as the original word
                scrmbld_word += word[word_length - 1]

        # if the word happens to be a punctuation, add it without a space
        if scrmbld_word in punc:
            output_txt += scrmbld_word
        else:
            output_txt += ' ' + scrmbld_word

    # remove leading spaces
    output_txt = output_txt.strip()

    # print the output
    print( 'Here is the scrambled text:\n\n' + output_txt + '\n' )


scramble()