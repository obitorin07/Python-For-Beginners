#!/usr/bin/env python3
"""Pig Latin takes the first consonant of a word,
moves it to the end of the word and adds on an
“ay”. If a word begins with a vowel you just add
“way” to the end. For example, pig becomes igpay,
banana becomes ananabay, and aadvark becomes
aadvarkway. Create a program that will ask the
user to enter a word and change it into Pig Latin.
Make sure the new word is displayed in lower case"""

word =input("Enter Word:").lower()
first_word =word[0]
check_len =len(word)
rest =word[1:check_len]

if first_word!="a" and first_word!="e" and first_word!="i" and first_word!="o" and first_word!="u":
    new_word = rest+first_word +"ay"
else:
    new_word =first_word+"way"
print(new_word)