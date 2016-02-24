import sys
converter = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
             "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
             "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
             "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
             "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
             "z": "--..", "0": "-----", "1": ".----", "2": "..---",
             "3": "...--", "4": "....-", "5": ".....", "6": "-....",
             "7": "--...", "8": "---..", "9": "----."}
reverse_converter = {val:key for key, val in converter.iteritems()}

def convert_to_morse(word):
    return "".join([converter[char] for char in word if char in converter])

def find_duplicated_morse_code_for_word(words):
    morse_to_char = {}
    hashed_code_map = {}
    duplicates = set()
    # step 1: create data structure to store potential duplicates
    for word in words:
        code = convert_to_morse(word)
        if code in hashed_code_map:
            duplicates.add(code)
        # hash reduces the size of the string in memory
        hashed_code_map.setdefault(code, []).append(word)

    res = {}
    #layer 2: filter and remove false positives
    for code in duplicates:
        for word in hashed_code_map[code]:
            res.setdefault(code, []).append(word)
    for key in res:
        if len(res[key]) == 1:
            del res[key]
    
    return res

print find_duplicated_morse_code_for_word(["hi", "ih"])
# prints {'......': ['hi', 'ih']}
print find_duplicated_morse_code_for_word(["hi", "ih", "a"])
# prints {'......': ['hi', 'ih']}
print find_duplicated_morse_code_for_word(["hi", "ih", "a", "a"])
# prints {'......': ['hi', 'ih'], '.-': ['a', 'a']}
print find_duplicated_morse_code_for_word(["hi", "ih", "a", "a", "c"])
# prints {'......': ['hi', 'ih'], '.-': ['a', 'a']}
print find_duplicated_morse_code_for_word(["hi", "ih", "a", "b", "c"])
# prints {'......': ['hi', 'ih']}
