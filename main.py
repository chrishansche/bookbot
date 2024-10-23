def main():
     book = read()
     num_words = count(book)
     book_character_count = character_count(book)
     letter_list = split_dict(book_character_count)

     print(f"--- Begin report of books/frankenstein.txt ---")
     print(f"{num_words} words found in the document")
     
     for item in letter_list:
          if not item["char"].isalpha():
               continue
          print(f"The '{item['char']}' character was found {item['num']} times")

     print("--- End report ---")



def read():
    with open("books/frankenstein.txt") as f:
            file_contents = f.read()
    #print(file_contents)
    return file_contents




def count(file_contents):
    words = file_contents.split()
    count_words = len(words)
    return count_words

def character_count(file_contents):
     char_dictionary = {}
     lowered_file_contents = file_contents.lower()
     for char in lowered_file_contents:
          char_dictionary[char] = char_dictionary.get(char, 0) + 1
     return(char_dictionary)

def sort_on(d):
    return d["num"]

def split_dict(character_count):
     letter_list = []
     for pair in character_count:
          letter_list.append({"char":pair,"num": character_count[pair]})
     letter_list.sort(reverse=True, key=sort_on)
     return letter_list
          
          
     


main()

