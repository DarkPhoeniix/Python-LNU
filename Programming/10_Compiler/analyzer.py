
from command import Command
from parser import parse, Token, lexemes


ops = ['+', '-', '*', '/']
temp_variable_index = 0


def priority(op):
    res_priority = 3
    if op == '*' or op == '/':
        res_priority = 2
    elif op == '+' or op == '-':
        res_priority = 1
    elif op == '(' or op == ')' or op == ';':
        res_priority = 0

    return res_priority


def handle_expression(token_list):
    operations = []
    arguments = []
    result = []

    def generate_command():
        op = operations.pop()
        rhs = arguments.pop()
        lhs = arguments.pop()
        name = ""
        if op.value == "+":
            name = "ADD"
        elif op.value == "-":
            name = "SUB"
        elif op.value == "*":
            name = "MUL"
        elif op.value == "/":
            name = "DIV"
        res = "t" + str(globals()["temp_variable_index"])
        result.append(Command(name, lhs.value, rhs.value, res))
        arguments.append(Token(res))
        globals()["temp_variable_index"] += 1

    while token_list != []:
        token = token_list.pop(0)
        if token.value not in lexemes:
            arguments.append(token)
        elif token.value in ops:
            if operations != []:
                while operations[-1].value in ops and \
                        priority(operations[-1].value) >= priority(token.value):
                    generate_command()
                    if operations == []:
                        break
            operations.append(token)
        elif token.value == "(":
            operations.append(token)
        elif token.value == ")":
            while operations[-1].value != '(':
                generate_command()
            if operations[-1].value != '(':
                print("ERROR 404")
            operations.pop()
    while operations != []:
        if operations[-1].value == "(" or operations[-1].value == ")":
            print("ERROR 404")
        generate_command()
    return result


def handle_command(token_list):
    if token_list[0].value == "read":
        return Command("READ", token_list[2].value, "", "")
    elif token_list[0].value == "write":
        return Command("WRITE", token_list[2].value, "", "")
    else:
        if len(token_list) == 3:
            return [Command("COPY", token_list[2].value, token_list[0].value, "")]
        else:
            temp = handle_expression(token_list[2: len(token_list)])
            temp[-1].result = token_list[0].value
            globals()["temp_variable_index"] -= 1
            return temp


def handle_block(command_list, number):
    compiled = []
    i = 0
    while i < len(command_list):
        if command_list[i].value == "read" or command_list[i].value == "write":
            compiled.append(handle_command(command_list[i: i + 3]))
            i += 3
        elif command_list[i].value == '=':
            j = i
            while command_list[j].value != ';':
                j += 1
            for x in handle_command(command_list[i - 1: j]):
                compiled.append(x)
            i = j
        elif command_list[i].value == "if" or command_list[i].value == "ifnot" or \
                command_list[i].value == "while" or command_list[i].value == "whilenot":
            j = i
            while command_list[j].value != "{":
                j += 1
            j += 1
            d_num = 1
            while d_num != 0 and j < len(command_list):
                if command_list[j].value == "{":
                    d_num += 1
                if command_list[j].value == "}":
                    d_num -= 1
                j += 1
            for x in handle_operator_block(command_list[i: j], number + len(compiled)):
                compiled.append(x)
            i = j
        else:
            i += 1
    return compiled


def handle_operator_block(command_list, lines_number):
    result = []

    def handle_if(name):
        last = 0
        for i in range(2, len(command_list)):
            if command_list[i].value == "]":
                last = i
                break
        condition = handle_expression(command_list[2:last])
        for x in condition:
            result.append(x)
        block = handle_block(command_list[last + 2:len(command_list) - 1], lines_number + len(result) + 1)
        result.append(Command(name, condition[-1].result,
                              str(lines_number + len(block) + 1 + len(result)), ""))
        for x in block:
            result.append(x)

    def handle_while(name):
        last = 0
        for i in range(2, len(command_list)):
            if command_list[i].value == "]":
                last = i
                break
        condition = handle_expression(command_list[2:last])
        for x in condition:
            result.append(x)
        block = handle_block(command_list[last + 2:len(command_list) - 1], lines_number + len(result) + 1)
        result.append(Command(name, condition[-1].result,
                              str(lines_number + len(block) + 2 + len(result)), ""))
        for x in block:
            result.append(x)

    if command_list[0].value == "if":
        handle_if("GOTOIFNOT")
    elif command_list[0].value == "ifnot":
        handle_if("GOTOIF")
    elif command_list[0].value == "while":
        handle_while("GOTOIFNOT")
        result.append(Command("GOTO", str(lines_number), "", ""))
    else:
        handle_while("GOTOIF")
        result.append(Command("GOTO", str(lines_number), "", ""))
    return result


def compiler(input_file_name: str, output_file_name):
    token_list = parse(input_file_name)
    vm = open(output_file_name, 'w')
    for i in handle_block(token_list, 0):
        vm.write(str(i.name) + ' ' + str(i.lhs))
        if i.rhs:
            vm.write(' ' + str(i.rhs))
        if i.result:
            vm.write(' ' + str(i.result))
        vm.write(' \n')
