# -*- coding: utf-8 -*-
with open("file_to_read.txt", "r") as f:
    text = f.read()

count_terrible = text.count("terrible")
print(f"The word 'terrible' appears {count_terrible} times.")

words = text.split()
new_words = []
count = 0

for word in words:
    if word == "terrible":
        count += 1
        if count % 2 == 0: 
            new_words.append("pathetic")
        else:  
            new_words.append("marvellous")
    else:
        new_words.append(word)

new_text = " ".join(new_words)
with open("result.txt", "w") as f:
    f.write(new_text)
