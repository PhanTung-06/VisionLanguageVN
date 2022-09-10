import encodings
import os
import glob

char_list_1 = '0123456789abcdefghijklmnopqrstuvwxyzáàảãạâấầẩẫậăắằẳẵặóòỏõọôốồổỗộơớờởỡợéèẻẽẹêếềểễệúùủũụưứừửữựíìỉĩịýỳỷỹỵđ'
token = [*char_list_1]

f = open('charset_62.txt', 'a+', encoding='utf-8')
for i in range(len(token)):
    character = token[i].upper()
    f.write(str(i) + " " + character + '\n')


char_list_2 = 'abcdefghijklmnopqrstuvwxyzáàảãạâấầẩẫậăắằẳẵặóòỏõọôốồổỗộơớờởỡợéèẻẽẹêếềểễệúùủũụưứừửữựíìỉĩịýỳỷỹỵđ'
token = [*char_list_2]
for i in range(len(token)):
    character = token[i]
    f.write(str(i + len(char_list_1)) + " " + character + '\n')
f.close()