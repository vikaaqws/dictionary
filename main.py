text: str = input("Введіть текст :  ")
mode = input("Введіть режим редагування(A/B/C) : ")

def ShowSorted(text, mode=None):
    text = text.replace(".", " ")
    text = text.replace(",", " ")
    edited_text = text.split()
    for i in edited_text:
         if mode == "A" and len(i) > 3:
             edited_text.append(i)
             edited_text.sort()
         elif mode == "B" and len(i) > 3:
             edited_text.append(i)
         elif mode == "C" and len(i) > 3:
             edited_text.append(i)

    if edited_text and mode == "A"
        edited_text = set(edited_text)
        edited_text = list(edited_text)
        edited_text.sort()
    output = " "
    for i in edited_text:
        output += i + "\n"
        print(output)
    elif edited_text and mode ==  "B" :
        output = {}
    for word in edited_text:
        edited_text.update({word: allWords.count(word)})
    keysSorted = []
    for key in edited_text:
        keysSorted.append(key)
    keysSorted.sort()
    for key in keysSorted:
        print(key)
def ShowWordCount(text):
    text = text.replace(".", " ")
    text = text.replace(",", " ")
    allWords = text.split()
    edited_text = {}
    for word in allWords:
        edited_text.update({word: allWords.count(word)})
    keysSorted = []
    for key in edited_text:
        keysSorted.append(key)
    keysSorted.sort()
    for key in keysSorted:
        print(f"{key} - {edited_text[key]}")

def ShowTextLenght(text):
    text = text.split()
    print(text[-1;-6;-1])

while True:
     action = input("Select an action: \n1 - Show words sorted \n2 - Show words count \n3 Show )
       if action == "1":
           ShowSorted(text)
       elif action == "2":
            ShowWordCount(text)
       elif action == "3":
           ShowTextLenght(text)
       else:
           print("Invalid action!")

