from check_palindrome import CheckPalindrome


def main():

    check_text1=CheckPalindrome()
    check_text1.is_palindrome('arara')

    check_text2=CheckPalindrome()
    check_text2.is_palindrome('A grama é amarga.')

    check_text3=CheckPalindrome()
    check_text3.is_palindrome('Adias a data da saída.')

    check_text4=CheckPalindrome()
    check_text4.is_palindrome('A Daniela ama a lei? Nada!')

    check_text5=CheckPalindrome()
    check_text5.is_palindrome('A dama admirou o rim da amada.')

    check_text6=CheckPalindrome()
    check_text6.is_palindrome('A mãe te ama.')

    check_text7=CheckPalindrome()
    check_text7.is_palindrome('Acuda cadela da Leda caduca.')

    check_text8=CheckPalindrome()
    check_text8.is_palindrome('A gorda ama a droga.')

    check_text9=CheckPalindrome()
    check_text9.is_palindrome('A cara rajada da jararaca.')

    check_text10=CheckPalindrome()
    check_text10.is_palindrome('A base do teto desaba.')



if __name__=='__main__':

    main()