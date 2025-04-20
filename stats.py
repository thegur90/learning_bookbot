def count_words(book):
    count = 0
    for word in book.split():
        count +=1
    return count

def character_stats(book):
    result = {}
    word_list = book.split()
    for word in word_list:
        for char in word:
            result[char.lower()]=0
    for word in word_list:
        for char in word:
            result[char.lower()]+=1
    return result

def sort_on(dict):
    return dict["count"]

def convert_big_dict_to_dict_list(book):
    answer = []
    for key in book:
        tmp = {}
        tmp["name"] = key
        tmp["count"] = book[key]
        answer.append(tmp)
        del tmp
    answer.sort(reverse=True, key=sort_on)
    return answer
