
from virtual_machine import execute
from analyzer import compiler


def main():
    file_name = input("Input file name: ")
    compiler(file_name, "vm.txt")
    execute("vm.txt")
    print("Success")


if __name__ == "__main__":
    main()
# def isfloat(number):
#     try:
#         float(number)
#         return True
#     except ValueError:
#         return False
#
#
# def set_priority(c):
#     if c == '*' or c == '/':
#         res = 2
#     elif c == '+' or c == '-':
#         res = 1
#     elif c == '(' or c == ')' or c == ';':
#         res = 0
#     else:
#         res = 3
#     return res
#
#
# class Token:
#     def __init__(self, value, lexeme):
#         self.value = value
#         if isfloat(self.value):
#             self.value = float(self.value)
#         self.lexeme = lexeme
#
#     def __str__(self):
#         return str(self.value) + " " + self.lexeme
#
#     def __repr__(self):
#         return str(self.value) + " " + self.lexeme
#
#
# class Command:
#     def __init__(self, name, left, right, result):
#         self.name = name
#         self.left = left
#         self.right = right
#         self.result = result
#
#     def __str__(self):
#         return self.name + " " + self.left + " " + self.right + " " + self.result
#
#     def __repr__(self):
#         return self.name + " " + self.left + " " + self.right + " " + self.result
#
#
# sign_list = ['>', ';', '=', '*', '/', '+', '-', '(', ')', '{', '}', '[', ']', '#']
# operators = ['*', '/', '+', '-']
# temp_index = 0
#
#
# def handleExpression(token_list):
#     operation = []
#     arguments = []
#     result = []
#
#     def generateCommand():
#         op = operation.pop()
#         rhs = arguments.pop()
#         lhs = arguments.pop()
#         if op.lexeme == "+":
#             name = "ADD"
#         elif op.lexeme == "-":
#             name = "SUB"
#         elif op.lexeme == "*":
#             name = "MUL"
#         elif op.lexeme == "/":
#             name = "DIV"
#         res = "t" + str(globals()["temp_index"])
#         result.append(Command(name, lhs.lexeme, rhs.lexeme, res))
#         arguments.append(Token(res, res))
#         globals()["temp_index"] += 1
#
#     while token_list != []:
#         token = token_list.pop(0)
#         if token.lexeme not in sign_list:
#             arguments.append(token)
#         elif token.lexeme in operators:
#             if operation != []:
#                 while operation[len(operation) - 1].lexeme in operators and \
#                         set_priority(operation[len(operation) - 1].lexeme) >= set_priority(token.lexeme):
#                     generateCommand()
#                     if operation == []:
#                         break
#             operation.append(token)
#         elif token.lexeme == "(":
#             operation.append(token)
#         elif token.lexeme == ")":
#             while operation[len(operation) - 1].lexeme != '(':
#                 generateCommand()
#             if operation[len(operation) - 1].lexeme != '(':
#                 print("ERROR 404")
#             operation.pop()
#     while operation != []:
#         if operation[len(operation) - 1].lexeme == "(" or operation[len(operation) - 1].lexeme == ")":
#             print("ERROR 404")
#         generateCommand()
#     return result
#
#
# def handleCommand(token_list):
#     ''' обробка команд вигляду <VARIABLE>=<EXPRESSION>; read> <VARIABLE>; write> <VARIABLE>; '''
#
#     if token_list[0].lexeme == "read":
#         return Command("READ", token_list[2].lexeme, "", "")
#     elif token_list[0].lexeme == "write":
#         return Command("WRITE", token_list[2].lexeme, "", "")
#     else:
#         if len(token_list) == 3:
#             return [Command("COPY", token_list[2].lexeme, token_list[0].lexeme, "")]
#         else:
#             temp = handleExpression(token_list[2: len(token_list)])
#             temp[len(temp) - 1].result = token_list[0].lexeme
#             globals()["temp_index"] -= 1
#             return temp
#
#
# def handleBlock(command_list, number):
#     ''' обробка набору команд чи блоків операторів; '''
#     compiled = []
#     i = 0
#     while i < len(command_list):
#         if command_list[i].lexeme == "#":
#             if isfloat(command_list[i + 1].lexeme):
#                 temp = Token(command_list[i - 1].lexeme + command_list[i + 1].lexeme,
#                              command_list[i - 1].lexeme + command_list[i + 1].lexeme)
#                 command_list.remove(command_list[i - 1])
#                 command_list.remove(command_list[i - 1])
#                 command_list.remove(command_list[i - 1])
#                 i -= 1
#                 command_list.insert(i, temp)
#             else:
#                 temp = Token(command_list[i - 1].lexeme + command_list[i].lexeme + command_list[i + 1].lexeme,
#                              command_list[i - 1].lexeme + command_list[i].lexeme + command_list[i + 1].lexeme)
#                 command_list.remove(command_list[i - 1])
#                 command_list.remove(command_list[i - 1])
#                 command_list.remove(command_list[i - 1])
#                 i -= 1
#                 command_list.insert(i, temp)
#         i += 1
#
#     i = 0
#     while i < len(command_list):
#         if command_list[i].lexeme == "read" or command_list[i].lexeme == "write":
#             compiled.append(handleCommand(command_list[i: i + 3]))
#             i += 3
#         elif command_list[i].lexeme == "=":
#             j = i
#             while command_list[j].lexeme != ";":
#                 j += 1
#             for x in handleCommand(command_list[i - 1: j]):
#                 compiled.append(x)
#             i = j
#         elif command_list[i].lexeme == "if" or command_list[i].lexeme == "ifnot" or \
#                 command_list[i].lexeme == "while" or command_list[i].lexeme == "whilenot":
#             j = i
#             while command_list[j].lexeme != "{":
#                 j += 1
#             j += 1
#             d_num = 1
#             while d_num != 0 and j < len(command_list):
#                 if command_list[j].lexeme == "{":
#                     d_num += 1
#                 if command_list[j].lexeme == "}":
#                     d_num -= 1
#                 j += 1
#             for x in handleOperatorBlock(command_list[i: j], number + len(compiled)):
#                 compiled.append(x)
#             i = j
#         else:
#             i += 1
#     return compiled
#
#
# def handleOperatorBlock(command_list, lines_number):
#     ''' обробка блоку оператора: while, whilenot, if, ifnot; '''
#     result = []
#
#     def handle_if(name):
#         last = 0
#         for i in range(2, len(command_list)):
#             if command_list[i].lexeme == "]":
#                 last = i
#                 break
#         umova = handleExpression(command_list[2:last])
#         for x in umova:
#             result.append(x)
#         block = handleBlock(command_list[last + 2:len(command_list) - 1], lines_number + len(result) + 1)
#         result.append(Command(name, umova[len(umova) - 1].result,
#                               str(lines_number + len(block) + 1 + len(result)), ""))
#         for x in block:
#             result.append(x)
#
#     def handle_while(name):
#         last = 0
#         for i in range(2, len(command_list)):
#             if command_list[i].lexeme == "]":
#                 last = i
#                 break
#         umova = handleExpression(command_list[2:last])
#         for x in umova:
#             result.append(x)
#         block = handleBlock(command_list[last + 2:len(command_list) - 1], lines_number + len(result) + 1)
#         result.append(Command(name, umova[len(umova) - 1].result,
#                               str(lines_number + len(block) + 2 + len(result)), ""))
#         for x in block:
#             result.append(x)
#
#     if command_list[0].lexeme == "if":
#         handle_if("GOTOIFNOT")
#     elif command_list[0].lexeme == "ifnot":
#         handle_if("GOTOIF")
#     elif command_list[0].lexeme == "while":
#         handle_while("GOTOIFNOT")
#         result.append(Command("GOTO", str(lines_number), "", ""))
#     else:
#         handle_while("GOTOIF")
#         result.append(Command("GOTO", str(lines_number), "", ""))
#     return result
#
#
# def compiler(path):
#     # read from file
#     program = open(path, encoding='utf-8')
#     one_line_program = ""
#     for line in program:
#         for i in line:
#             if i != "\n" and i != "\r" and i != " " and i != "\t":
#                 one_line_program += i
#     # create token
#     token_list = []
#     first = 0
#     last = -1
#     checker = True
#     for i in range(len(one_line_program)):
#         if one_line_program[i] in sign_list:
#             if not checker:
#                 temp = one_line_program[first:last + 1]
#                 token_list.append(Token(temp, temp))
#                 first += i - first
#                 last += i - last
#                 checker = True
#             token_list.append(Token(one_line_program[i], one_line_program[i]))
#             first += 1
#             last = i
#         else:
#             checker = False
#             last += 1
#     # write compiled program
#     vm = open("vm_program.txt", 'w', encoding='utf-8')
#     for i in handleBlock(token_list, 0):
#         vm.write(i.__str__() + "\n")
#
#
# def virtual_machine():
#     values = {}
#     vm_code = open("vm_program.txt", encoding='utf-8')
#     lines = []
#     for line in vm_code:
#         lines.append(line.split())
#
#     def concat(string):
#         i = 0
#         while i < len(string):
#             j = 0
#             while j < len(string[i]):
#                 if string[i][j] == "#":
#                     temp = string[i][: j] + str(int(values[string[i][j + 1:]]))
#                     string.remove(string[i])
#                     string.insert(i, temp)
#                 j += 1
#             i += 1
#         return string
#
#     i = 0
#     while i < len(lines):
#
#         temp_lines = concat(lines[i].copy())
#
#         if temp_lines[0] == "READ":
#             a = float(input())
#             if a not in values:
#                 values.update({temp_lines[1]: a})
#             else:
#                 values[temp_lines[1]] = a
#             i += 1
#         elif temp_lines[0] == "WRITE":
#             try:
#                 print(values[temp_lines[1]])
#             except Exception:
#                 print("Output error")
#             i += 1
#         elif temp_lines[0] == "ADD":
#             if isfloat(temp_lines[1]) and isfloat(temp_lines[2]):
#                 if temp_lines[3] not in values:
#                     values.update({temp_lines[3]: float(temp_lines[1]) + float(temp_lines[2])})
#                 else:
#                     values[temp_lines[3]] = float(temp_lines[1]) + float(temp_lines[2])
#             elif isfloat(temp_lines[1]):
#                 if temp_lines[3] not in values:
#                     values.update({temp_lines[3]: values[temp_lines[2]] + float(temp_lines[1])})
#                 else:
#                     values[temp_lines[3]] = values[temp_lines[2]] + float(temp_lines[1])
#             elif isfloat(temp_lines[2]):
#                 if temp_lines[3] not in values:
#                     values.update({temp_lines[3]: values[temp_lines[1]] + float(temp_lines[2])})
#                 else:
#                     values[temp_lines[3]] = values[temp_lines[1]] + float(temp_lines[2])
#             else:
#                 if temp_lines[3] not in values:
#                     values.update({temp_lines[3]: values[temp_lines[1]] + values[temp_lines[2]]})
#                 else:
#                     values[temp_lines[3]] = values[temp_lines[1]] + values[temp_lines[2]]
#             i += 1
#         elif temp_lines[0] == "SUB":
#             if isfloat(temp_lines[1]) and isfloat(temp_lines[2]):
#                 if temp_lines[3] not in values:
#                     values.update({temp_lines[3]: float(temp_lines[1]) - float(temp_lines[2])})
#                 else:
#                     values[temp_lines[3]] = float(temp_lines[1]) - float(temp_lines[2])
#             elif isfloat(temp_lines[1]):
#                 if temp_lines[3] not in values:
#                     values.update({temp_lines[3]: float(temp_lines[1]) - values[temp_lines[2]]})
#                 else:
#                     values[temp_lines[3]] = float(temp_lines[1]) - values[temp_lines[2]]
#             elif isfloat(temp_lines[2]):
#                 if temp_lines[3] not in values:
#                     values.update({temp_lines[3]: values[temp_lines[1]] - float(temp_lines[2])})
#                 else:
#                     values[temp_lines[3]] = values[temp_lines[1]] - float(temp_lines[2])
#             else:
#                 if temp_lines[3] not in values:
#                     values.update({temp_lines[3]: values[temp_lines[1]] - values[temp_lines[2]]})
#                 else:
#                     values[temp_lines[3]] = values[temp_lines[1]] - values[temp_lines[2]]
#             i += 1
#         elif temp_lines[0] == "DIV":
#             if temp_lines[2] != "0":
#                 if isfloat(temp_lines[1]) and isfloat(temp_lines[2]):
#                     if temp_lines[3] not in values:
#                         values.update({temp_lines[3]: float(temp_lines[1]) / float(temp_lines[2])})
#                     else:
#                         values[temp_lines[3]] = float(temp_lines[1]) / float(temp_lines[2])
#                 elif isfloat(temp_lines[1]):
#                     if temp_lines[3] not in values:
#                         values.update({temp_lines[3]: float(temp_lines[1]) / values[temp_lines[2]]})
#                     else:
#                         values[temp_lines[3]] = float(temp_lines[1]) / values[temp_lines[2]]
#                 elif isfloat(temp_lines[2]):
#                     if temp_lines[3] not in values:
#                         values.update({temp_lines[3]: values[temp_lines[1]] / float(temp_lines[2])})
#                     else:
#                         values[temp_lines[3]] = values[temp_lines[1]] / float(temp_lines[2])
#                 else:
#                     if temp_lines[3] not in values:
#                         values.update({temp_lines[3]: values[temp_lines[1]] / values[temp_lines[2]]})
#                     else:
#                         values[temp_lines[3]] = values[temp_lines[1]] / values[temp_lines[2]]
#             else:
#                 print("Division by 0")
#             i += 1
#         elif temp_lines[0] == "MUL":
#             if isfloat(temp_lines[1]) and isfloat(temp_lines[2]):
#                 if temp_lines[3] not in values:
#                     values.update({temp_lines[3]: float(temp_lines[1]) * float(temp_lines[2])})
#                 else:
#                     values[temp_lines[3]] = float(temp_lines[1]) * float(temp_lines[2])
#             elif isfloat(temp_lines[1]):
#                 if temp_lines[3] not in values:
#                     values.update({temp_lines[3]: values[temp_lines[2]] * float(temp_lines[1])})
#                 else:
#                     values[temp_lines[3]] = values[temp_lines[2]] * float(temp_lines[1])
#             elif isfloat(temp_lines[2]):
#                 if temp_lines[3] not in values:
#                     values.update({temp_lines[3]: float(temp_lines[2]) * values[temp_lines[1]]})
#                 else:
#                     values[temp_lines[3]] = float(temp_lines[2]) * values[temp_lines[1]]
#             else:
#                 if temp_lines[3] not in values:
#                     values.update({temp_lines[3]: values[temp_lines[1]] * values[temp_lines[2]]})
#                 else:
#                     values[temp_lines[3]] = values[temp_lines[1]] * values[temp_lines[2]]
#             i += 1
#         elif temp_lines[0] == "COPY":
#             if isfloat(temp_lines[1]):
#                 if temp_lines[2] not in values:
#                     values.update({temp_lines[2]: float(temp_lines[1])})
#                 else:
#                     values[temp_lines[2]] = float(temp_lines[1])
#             else:
#                 if temp_lines[2] not in values:
#                     values.update({temp_lines[2]: values[temp_lines[1]]})
#                 else:
#                     values[temp_lines[3]] = values[temp_lines[1]]
#             i += 1
#         elif temp_lines[0] == "GOTOIFNOT":
#             if values[temp_lines[1]] <= 0:
#                 i = int(temp_lines[2])
#             else:
#                 i += 1
#         elif temp_lines[0] == "GOTO":
#             i = int(temp_lines[1])
#         elif temp_lines[0] == "GOTOIF":
#             if values[temp_lines[1]] > 0:
#                 i = int(temp_lines[2])
#             else:
#                 i += 1
#         else:
#             print("ERROR 404")
#     print()
#
#
# def main():
#     compiler("program_1.txt")
#     virtual_machine()
#
#
# if __name__ == "__main__":
#     main()