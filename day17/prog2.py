def run_program(a, b, c, program): 
    program = list(map(int, program))
    def combo(i: int) -> int:
        match i:
            case 0: return 0
            case 1: return 1
            case 2: return 2
            case 3: return 3
            case 4: return a
            case 5: return b
            case 6: return c

    output = list()

    i = 0
    while i < len(program):
        opcode = program[i]
        operand = program[i+1]
        if opcode == 0:
            a = a // (2**combo(operand)) # truncated to int?
        elif opcode == 1:
            b = b ^ operand
        elif opcode == 2:
            b = combo(operand) % 8
        elif opcode == 3:
            if a != 0: i = operand
            else: i += 2
            continue
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            output.append(str(combo(operand)%8))
        elif opcode == 6:
            b = a // (2**combo(operand)) # truncated to int?
        elif opcode == 7:
            c = a // (2**combo(operand)) # truncated to int?
        i += 2

    return output

def get_best_quine_input(program, cursor, sofar):
    for candidate in range(8):
        if run_program(sofar * 8 + candidate, 0, 0, program) == program[cursor:]:
            if cursor == 0:
                return sofar * 8 + candidate
            ret = get_best_quine_input(program, cursor - 1, sofar * 8 + candidate)
            if ret is not None:
                return ret
    return None

f = open(0)

a = int(f.readline().strip()[12:])
f.readline()
f.readline()
f.readline()
program = list(f.readline().strip()[9:].split(','))

print(get_best_quine_input(program, len(program) - 1, 0))



