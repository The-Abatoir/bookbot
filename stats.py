def count_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def count_characters(text):
    lowered = text.lower()
    count_characters = {}
    for char in lowered:
        if char in count_characters:
            count_characters[char] += 1
        else:
            count_characters[char] = 1
    return count_characters

def dict_to_sorted_list(d):
    list = []
    for key in d:
        list.append({"letter": key, "count" : d[key]})
    list.sort(key=sort_by_count, reverse=True)
    return list

def sort_by_count(item):
    return item["count"]