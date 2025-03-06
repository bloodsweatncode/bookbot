def num_words(text):
    counter = 0 
    for i in text.split():
        counter += 1
    return counter