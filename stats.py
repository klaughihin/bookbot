def get_num_words(book):
    return len(book.split())


def count_characters(book):
    char_dict = {}

    for c in book:
        if not c.lower().isalpha():
            continue
        elif c.lower() in char_dict:
            char_dict[c.lower()] += 1
        else:
            char_dict[c.lower()] = 1

    return char_dict


def sort_on(items):
    return items["num"]


def sort_char_counts(char_dict):
    sorted_chars = []

    if not char_dict:
        raise Exception("empty character dictionary")
    else:
        for char in char_dict:
            sorted_chars.append({"char": char, "num": int(char_dict[char])})

    sorted_chars.sort(reverse=True, key=sort_on)

    return sorted_chars
