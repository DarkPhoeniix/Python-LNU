
def is_float(element: str) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False


def execute(file_name: str):
    variables = {}
    with open(file_name) as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].split()
        for j in range(len(line)):
            if '#' in line[j]:
                line[j] = line[j][:line[j].find('#')] + str(int(variables[line[j][line[j].find('#') + 1:]]))
        if line[0] == "ADD":
            if is_float(line[1]) and is_float(line[2]):
                variables[line[3]] = float(line[1]) + float(line[2])
            elif is_float(line[1]):
                variables[line[3]] = float(line[1]) + variables[line[2]]
            elif is_float(line[2]):
                variables[line[3]] = variables[line[1]] + float(line[2])
            else:
                variables[line[3]] = variables[line[1]] + variables[line[2]]
        elif line[0] == "SUB":
            if is_float(line[1]) and is_float(line[2]):
                variables[line[3]] = float(line[1]) - float(line[2])
            elif is_float(line[1]):
                variables[line[3]] = float(line[1]) - variables[line[2]]
            elif is_float(line[2]):
                variables[line[3]] = variables[line[1]] - float(line[2])
            else:
                variables[line[3]] = variables[line[1]] - variables[line[2]]
        elif line[0] == "MUL":
            if is_float(line[1]) and is_float(line[2]):
                variables[line[3]] = float(line[1]) * float(line[2])
            elif is_float(line[1]):
                variables[line[3]] = float(line[1]) * variables[line[2]]
            elif is_float(line[2]):
                variables[line[3]] = variables[line[1]] * float(line[2])
            else:
                variables[line[3]] = variables[line[1]] * variables[line[2]]
        elif line[0] == "DIV":
            if is_float(line[1]) and is_float(line[2]):
                variables[line[3]] = float(line[1]) / float(line[2])
            elif is_float(line[1]):
                variables[line[3]] = float(line[1]) / variables[line[2]]
            elif is_float(line[2]):
                variables[line[3]] = variables[line[1]] / float(line[2])
            else:
                variables[line[3]] = variables[line[1]] / variables[line[2]]
        elif line[0] == "COPY":
            if is_float(line[1]):
                variables[line[2]] = float(line[1])
            else:
                variables[line[2]] = variables[line[1]]
        elif line[0] == "GOTOIF":
            if variables[line[1]] > 0:
                i = int(line[2])
                continue
        elif line[0] == "GOTOIFNOT":
            if variables[line[1]] <= 0:
                i = int(line[2])
                continue
        elif line[0] == "GOTO":
            i = int(line[1])
            continue
        elif line[0] == "READ":
            var = float(input())
            variables[line[1]] = var
        elif line[0] == "WRITE":
            print(variables[line[1]])

        i += 1
