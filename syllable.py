def main(word):
    temp = ''
    temp2 = ''
    i = 0

    while i < len(word):
        temp += word[i]
        temp2 += word[i]
        if word[i] not in ('a', 'e', 'i', 'o', 'u'):
            #consonant
            #print("{0} is Consonant".format(word[i]))
            pass
        else:
            #vowel
            #print("{0} is Vowel".format(word[i]))
            print(temp)
            temp = ''
        i += 1
    if temp is not '':
        print(temp)

main("sindhuli")
