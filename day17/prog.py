def combo(i: int) -> int:
    match i:
        case 0: return 0
        case 1: return 1
        case 2: return 2
        case 3: return 3
        case 4: return registers[A]
        case 5: return registers[B]
        case 6: return registers[C]


f = open(0)

A = 'A'
B = 'B'
C = 'C'

registers = dict()
registers[A] = int(f.readline().strip()[12:])
registers[B] = int(f.readline().strip()[12:])
registers[C] = int(f.readline().strip()[12:])
f.readline()
program = list(map(int, f.readline().strip()[9:].split(',')))

output = list()


i = 0
while i < len(program):
    opcode = program[i]
    operand = program[i+1]
    print(opcode, operand)
    if opcode == 3:
        if registers[A] != 0: i = operand
        else: i += 2
        continue
    elif opcode == 0:
        registers[A] = registers[A] // (2**combo(operand)) # truncated to int?
    elif opcode == 1:
        registers[B] = registers[B] ^ operand
    elif opcode == 2:
        registers[B] = combo(operand) % 8
    elif opcode == 4:
        registers[B] = registers[B] ^ registers[C]
    elif opcode == 5:
        output.append(str(combo(operand)%8))
    elif opcode == 6:
        registers[B] = registers[A] // (2**combo(operand)) # truncated to int?
    elif opcode == 7:
        registers[C] = registers[A] // (2**combo(operand)) # truncated to int?
    i += 2

print(','.join(output))