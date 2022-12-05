import unidecode


class CheckPalindrome:
    def is_palindrome(self,text):
        only_strings=[]
        for char in text:
            if char.isalpha():
                only_strings.append(char)
        raw_text=unidecode.unidecode(''.join(only_strings).lower())
        text_to_compare=raw_text[::-1]
        
        if raw_text==text_to_compare:
            result=text + ' IS A PALINDROME'
        else:
            result=text+ ' IT\'S NOT A PALINDROME'

        return print(result)