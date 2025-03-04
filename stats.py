def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(text_to_count):
    word_count = 0
    for line in text_to_count.splitlines():
        line_words = line.split()
        word_count += len(line_words)
    return word_count

def get_character_counts(text_to_count):
    character_counts = {}
    for char in text_to_count:
        lower_char = char.lower()
        if lower_char in character_counts:
            character_counts[lower_char] += 1
        else:
            character_counts[lower_char] = 1
    
    return character_counts

def get_sorted_dictionary(character_counts, reverse=True):
    sorted_counts = []
    for character in character_counts:
        sorted_counts.append({"char": character, "count": character_counts[character]})
    
    def sort_on(dict):
        return dict["count"]
    
    sorted_counts.sort(reverse=reverse, key=sort_on)

    return sorted_counts
