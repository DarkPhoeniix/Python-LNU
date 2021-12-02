
import re
from Token import Token

lexemes = ['>', ';', '=', '*', '/', '+', '-', '(', ')', '{', '}', '[', ']']


def parse(file_name: str) -> []:
    with open(file_name) as file:
        lines = file.readlines()

    raw_code = ""
    for line in lines:
        raw_code += re.sub(r"\s", "", line)

    token_list = []
    temp = ""
    for i in range(len(raw_code)):
        if raw_code[i] not in lexemes:
            temp += raw_code[i]
        else:
            if temp:
                token_list.append(Token(temp))
            token_list.append(Token(raw_code[i]))
            temp = ""

    return token_list
