import string

def get_num_words(text):
    counter = 0 
    for i in text.split():
        counter += 1
    return counter

"""
def analyze_characters(text):
    character_set = {'$', 'q', 'z', 'f', 'o', '_', 'p', '9', '™', 'r', 'h', '1', '”', 'g', 'x', '[', 't', ':', 'ê', 'b', 'm', ')', 'l', 'c', 'k', '0', '!', 'ë', '‘', '\n', '8', 'j', ']', 's', 'w', '3', '4', '.', 'v', '(', '%', '2', '&', '’', 'n', ',', '7', 'ô', '\ufeff', 'd', '-', 'i', '?', '—', 'u', '•', '5', '*', 'y', 'æ', ' ', ';', '/', '6', '“', 'a', 'e', '#', 'â'}
    dictionary = dict.fromkeys(character_set, 0)
    for character in text.lower():
        dictionary[character] +=1
    return dictionary
"""


def get_chars_dict(text):
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] +=1
        else:
            chars[c] =1
    return chars


def sort_on(d):
    return d["count"]

def chars_dict_to_sorted_list(dictionary):
    sorted_list = []
    for character in dictionary:
        sorted_list.append({"character": character, "count": dictionary[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list