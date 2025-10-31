# ==================================================
# String Methods
# ==================================================



first_name = "serhat"
last_name = "kemal"



full_name = f"{first_name} {len(first_name)} {last_name} {2>1}"
print(f"f-string: {full_name}")
      # formatted string

print("Python " * 3)

# --- Slicing ---

text = "Hello World"
#       01234567890
#                -1

print(f"\n--- Slicing ---")
print(f"Orijinal: {text}")
print(f"[0:7]  -> {text[0:5]}")   
print(f"[8:]   -> {text[6:]}")    
print(f"[-5:]  -> {text[-5:]}")   # last 5 



# Strip methods
# 
dirty_text = "   \n\t s   Programming \t "
print(f"\n--- Cleaning ---")
print(f"   : '{dirty_text}'")
print(f".strip() : '{dirty_text.strip()}'")  
print(f".lstrip(): '{dirty_text.lstrip()}'") 
print(f".rstrip(): '{dirty_text.rstrip()}'") 



print(f"\n--- Chained methods ---")
test_name = "Serhat Kemal"
print(f"Orijinal: {test_name}")


print(f".upper() : {test_name.upper()}")
print(f".lower() : {test_name.lower()}")


print(f".find('a') : {test_name.find('a')}") # 3


print(f".replace('e', 'a') : {test_name.replace('e', 'a')}") # 'Sarhat Kamal'


print(f"'e' not in test_name : {'e' not in test_name}") # False
print(f"'z' in test_name     : {'z' in test_name}")     # False




sentence = "Bruh momento es uno des momentos"
words = sentence.split(' ') 
print(f"\n.split() : {words}")
print(f"First word: {words[0]}") 

# .join() -> split tersi
new_sentence = " | ".join(words)
print(f".join()  : {new_sentence}")


filename = "last_project.pdf"
print(f"\n.endswith('.pdf') : {filename.endswith('.pdf')}") # True
print(f".startswith('asd')  : {filename.startswith('asd')}")  # False


print(f"'programming'.count('g') : {'programming'.count('g')}") # 2


text = "python programming language"
print(f".capitalize() : {text.capitalize()}") 
print(f".title()      : {text.title()}")      

print(f"\n'12345'.isdigit() : {'12345'.isdigit()}") 
print(f"'Python'.isalpha(): {'Python'.isalpha()}") 
print(f"'Python123'.isalnum(): {'Python123'.isalnum()}") # isDigit or isAlpha