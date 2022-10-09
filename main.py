class WORD(object):
    def __init__(self, typenum, word):
        self.typenum = typenum
        self.word = word


str_input = ""

rwtab = ["begin", "end", "do", "if", "then", "while"]
ch = ""
p_input = 0
p_token = 0


def getchar():
    global ch, p_input
    # print("input:%d" % p_input)
    ch = str_input[p_input]
    p_input += 1
    return ch


# 去掉空格
def delete_blank():
    global ch, p_input
    while ch == " " or ch == 10:
        ch = str_input[p_input]
        p_input += 1


def concat(str1):
  global ch
  str1 += ch
  return str1


def letter():
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        return True
    else:
        return False


def digit():
    if '0' <= ch <= '9':
        return True
    else:
        return False


def reserve(str1):
   global rwtab
   for find_str in rwtab:
       if str1 == find_str:
           return rwtab.index(find_str)+1

   return 10


def retract():
  global p_input
  p_input -= 1


def dtb():
    return bin(int(ch))


def scanner():
    token =""
    myword = WORD(10, "")
    getchar()
    delete_blank()
    if letter():
        while letter() or digit():
            token += ch

            getchar()
        retract()
        myword.typenum = reserve(token)
        myword.word = token
        return myword
    elif digit():
        while digit():
            token += ch
            getchar()
        retract()
        myword.typenum = 20
        myword.word = token
        return myword
    elif ch == '=':
        getchar()
        if ch == '=':
            myword.typenum = 39
            myword.word = "=="
            return myword
        retract()
        myword.typenum = 21
        myword.word = "="
        return myword
    elif ch == '+':
        myword.typenum = 22
        myword.word = '+'
        return myword
    elif ch == '-':
        myword.typenum = 23
        myword.word = '-'
        return myword
    elif ch == '*':
        myword.typenum = 24
        myword.word = '*'
        return myword
    elif ch == '/':
        myword.typenum = 25
        myword.word = '/'
        return myword
    elif ch == '(':
        myword.typenum = 26
        myword.word = '('
        return myword
    elif ch == ')':
        myword.typenum = 27
        myword.word = ')'
        return myword
    elif ch == '[':
        myword.typenum = 28
        myword.word = '['
        return myword
    elif ch == ']':
        myword.typenum = 29
        myword.word = ']'
        return myword
    elif ch == '{':
        myword.typenum = 30
        myword.word = '{'
        return myword
    elif ch == '}':
        myword.typenum = 31
        myword.word = '}'
        return myword
    elif ch == ',':
        myword.typenum = 32
        myword.word = ','
        return myword
    elif ch == ':':
        getchar()
        if ch == "=":
            myword.typenum = 18
            myword.word = ":="
            return myword
        myword.typenum = 33
        myword.word = ':'
        return myword
    elif ch == ';':
        myword.typenum = 34
        myword.word = ';'
        return myword
    elif ch == '>':
        getchar()
        if ch == '=':
            myword.typenum = 37
            myword.word = '>='
            return myword
        retract()
        myword.typenum = 35
        myword.word = '>'
        return myword
    elif ch == '<':
        getchar()
        if ch == '=':
            myword.typenum = 38
            myword.word = '<='
            return myword
        retract()
        myword.typenum = 36
        myword.word = '<'
        return myword
    elif ch == '!':
        getchar()
        if ch == '=':
            myword.typenum = 40
            myword.word = '!='
            return myword
        retract()
        myword.typenum = -1
        myword.word = 'ERROR'
        return myword
    elif ch == '\0':
        myword.typenum = 1000
        myword.word = 'OVER'
        return myword
    else:
        myword.typenum = -1
        myword.word = 'ERROR'
        return myword


if __name__ == "__main__":
   over = 1
   # str_input = input("Enter the words:")
   # print(str_input)
   # str_input += '\0'
   f = open("text.txt", "r")
   w = open("result.txt", "w")
   str_input = f.read()+"\0"

   while over < 1000 and over != -1:
       oneword = scanner()
       print("(%d,%s)" % (oneword.typenum, oneword.word))
       w.write("(%d,%s)\n" % (oneword.typenum, oneword.word))  # 文件方式
       over = oneword.typenum
   f.close()
   w.close()
