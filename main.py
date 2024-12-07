file_path = 'books/frankenstein.txt'

def main():
        with open(file_path) as f:
            file_contents = f.read()
        return file_contents

print(main())
all_text = main()

def count(text):
      words = text.split()
      return print(len(words))
    
word_count = count(all_text)

def count_letters(text):
      lower_case = text.lower()
      letters_dict = {char: lower_case.count(char) for char in set(lower_case) if char.isalpha()}
      return letters_dict

print(count_letters(all_text))

letters_dict = count_letters(all_text)

[print(f'The ')]

def report(dict):
      print(f"--- Begin report of {file_path} ---")
      print(f"{word_count} words found in the document\n")

      for letter, count in dict.items():
            print(f"The {letter} character was found {count} times")
      
      print("\n--- End report ---")

report(letters_dict)