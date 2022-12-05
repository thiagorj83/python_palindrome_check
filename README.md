# python_palindrome_check

Here is a palindrome checker written in python.

There are two archives: check_palindrome.py and main.py.
In check_palindrome.py, the function is_palindrome() receives a string that can be
a single word or a phrase.

It collects only the letters of the given string, remove any graphic accent like '´' or '^', for example,
and reverse the string. Then, it compares the string letters with a copy of the same string in
reversed order. If they are equal, then there is a palindrome.

The main.py archive implements the class CheckPalindrome.
