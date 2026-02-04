def get_book_text(filepath):
    content = ""
    with open(filepath, 'r') as f:
        content = f.read()
    return content

def word_count(text):
    word_list = text.split()
    return len(word_list)

# producing unexpected results
# def character_count(text):
#     char_dict = dict()
#     for i in text:
#         i = i.lower()
#         if i in char_dict:
#             continue
#         char_dict[i] = text.count(i)
#     return len(text), char_dict

def character_count_v2(text):
    char_dict = dict()
    for i in text:
        i = i.lower()
        if i in char_dict:
            char_dict[i] += 1
            continue
        char_dict[i] = 1
    return len(text), char_dict

def report(a_dict):
    sorted_list = list()
    new_dict = dict()
    for key in a_dict:
        if key.isalpha():
            new_dict["char"] = key
            new_dict["num"] = a_dict[key]
            sorted_list.append(new_dict)
        new_dict = {}
    return sorted(sorted_list, \
    key=lambda item: item["num"], reverse=True)

def display_report(a_dict, filepath, total_char_count,num_words):
    my_report = report(a_dict)
    print(f"""\
============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for item in my_report:
        print(f"{item['char']}: {item['num']}")
    print(f"Total characters (including spaces and punctuation): {total_char_count}")
    print("============= END ===============")
