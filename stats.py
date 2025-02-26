def get_num_words(text: str) -> int:
    return len(text.split())


def count_chars(text: str) -> [{str: int}]:
    char_count = {}
    for char in text:
        char = char.lower()
        if (char in char_count.keys()):
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def print_char_count(char_count: {str: int}) -> None:
    print("--------- Character Count -------")
    sorted_dict: [{str: str | int}] = [{"char": key, "count": value}
                                       for key, value in char_count.items()]
    sorted_dict.sort(reverse=True, key=lambda x: x["count"])
    for item in sorted_dict:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")
