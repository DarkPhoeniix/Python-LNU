
def print_help():
    print('''Available commands:
    help  - show this help
    exit  - exit this program
    print - print memory blocks map
    allocate <num> - allocate <num> cells. Returns block first cell number
    free <num> - free block with first cell number <num>
    ''')


def print_memory_state(memory, width):
    print_width = 2

    for i in range(len(memory)):
        if (i * print_width) % (width * print_width) == 0:
            print('|', end='')

        if memory[i] != ' ' and memory[i] != 'x':
            print(memory[i], end='')
            print('x' * (print_width - len(str(memory[i]))), end='')
            printed = (i * 3) % print_width
        elif ((i + 1) * print_width) % (width * print_width) == 0:
            print(memory[i], end='')
        elif i + 1 < len(memory) and memory[i] != memory[i+1]:
            print(memory[i] * (print_width - 1), end='')
        else:
            print(memory[i] * print_width, end='')

        if i + 1 < len(memory) and memory[i] != memory[i+1] and memory[i+1] != 'x':
            print('|', end='')

        if ((i + 1) * print_width) % (width * print_width) == 0:
            print('|\n', end='')


def allocate_memory(memory, allocate_num):
    sublist = [' ' for i in range(allocate_num)]
    allocate_index = []
    for i in range(len(memory)):
        if memory[i] == sublist[0] and memory[i:i + len(sublist)] == sublist:
            allocate_index.append(i)
    if len(allocate_index) != 0 and allocate_index[0] + allocate_num - 1 < len(memory):
        print(allocate_index[0])
        memory[allocate_index[0]] = allocate_index[0]
        for i in range(allocate_index[0] + 1, allocate_index[0] + allocate_num):
            memory[i] = 'x'
    else:
        print("Can't allocate " + str(allocate_num) + " cells")
        return


def free_memory(memory, free_index):
    for i in range(len(memory)):
        if memory[i] == free_index:
            memory[i] = ' '
            i += 1
            while memory[i] == 'x':
                memory[i] = ' '
                i += 1


print("Please set memory size and max output width: ")
memory_size, memory_width = map(int, input().split())
memory_list = [' ' for i in range(memory_size)]

print("Type 'help' for additional info.")
while True:
    command_list = input().split(' ')
    if command_list[0] == "help":
        print_help()
    elif command_list[0] == "print":
        print_memory_state(memory_list, memory_width)
    elif command_list[0] == "allocate":
        allocate_memory(memory_list, int(command_list[1]))
    elif command_list[0] == "free":
        free_memory(memory_list, int(command_list[1]))
    elif command_list[0] == "exit":
        quit()

