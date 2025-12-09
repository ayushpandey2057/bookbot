def get_num_of_words(text):
    return len(text.split())
    
def get_character_count(text):
    count_dict = {}
    for char in text:
        char = char.lower()
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

def char_dict_to_list(char_dict):
    char_dict_list = []
    for k,v in char_dict.items():
        char_dict_list.append({"char": k, "num": v})
    return char_dict_list

def sort_on(char_dict):
    return char_dict["num"]
