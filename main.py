def main(relative_path_to_book):
  file_content = get_file_content(relative_path_to_book)
  words_count = words_counter(file_content)
  characters_dict = characters_counter(file_content)
  list_char_dicts = convert_dict_to_list(characters_dict)
  list_char_dicts.sort(reverse=True, key=sort_on)
  book_name = get_book_name_from_path(relative_path_to_book)
  generate_report(book_name, words_count, list_char_dicts)

def get_file_content(path_to_file):
  with open(path_to_file) as f:
    file_content = f.read()
    return file_content
  
def words_counter(file_content):
  words_count = file_content.split()
  return len(words_count)

def characters_counter(file_content):
  characters_dict = {}
  for char in file_content:
    lowered_char = char.lower()
    if lowered_char in characters_dict:
      characters_dict[lowered_char] += 1
    else:
      characters_dict[lowered_char] = 1
  return characters_dict

def convert_dict_to_list(dict):
  dict_list = []
  for key in dict:
    if key.isalpha():
      new_dict = {}
      new_dict["char"] = key
      new_dict["count"] = dict[key]
      dict_list.append(new_dict)
  return dict_list

def generate_report(book_name, words_count, list_char_dicts):
  print(f"--- Begin report of {book_name} ---")
  print(f"{words_count} words found in the document")
  print()
  for dict in list_char_dicts:
    print(f"The {dict['char']} character was found {dict['count']} times")
  print("--- End report ---")


def sort_on(dict):
  return dict["count"]

def get_book_name_from_path(relative_path):
  path_parts = relative_path.split('/')
  book_name = path_parts[1].split('.')[0]
  return book_name

main("books/frankenstein.txt")