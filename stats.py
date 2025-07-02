def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    characters = {}
    lowered_book_text = book_text.lower()
    for c in lowered_book_text:
        if c not in characters:
            characters[c] = 0
        characters[c] += 1
    return characters

def sort_on(d):
    return d["count"]

def sort(dictionary):
    dic_list = []
    for char in dictionary:
        count = dictionary[char]
        new_dict = {"char": char, "count": count}
        dic_list.append (new_dict)
    dic_list.sort(reverse=True, key=sort_on)
    return dic_list