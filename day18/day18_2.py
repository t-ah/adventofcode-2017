from collections import defaultdict
from multiprocessing import Queue

def get_val(reg, addr):
    try:
        a = int(addr)
        return a
    except ValueError:
        return reg[addr]

def run(num, prog, queue):
    reg = defaultdict(int)
    reg["p"] = num
    pc = 0

    while pc >= 0 and pc < len(prog):
        instr = prog[pc]
        if instr[0] == "snd":
            yield get_val(reg, instr[1])
        elif instr[0] == "set":
            reg[instr[1]] = get_val(reg, instr[2])
        elif instr[0] == "add":
            reg[instr[1]] += get_val(reg, instr[2])
        elif instr[0] == "mul":
            reg[instr[1]] *= get_val(reg, instr[2])
        elif instr[0] == "mod":
            reg[instr[1]] %= get_val(reg, instr[2])
        elif instr[0] == "rcv":
            if queue.empty():
                yield "r"
            reg[instr[1]] = queue.get()
        elif instr[0] == "jgz":
            if get_val(reg, instr[1]) > 0:
                pc += get_val(reg, instr[2]) - 1
        pc += 1

prog = []
with open("input.txt", "r") as f:
    for line in f:
        prog.append(line.strip().split(" "))

queues = [Queue(), Queue()]
progs = [run(0, prog, queues[0]), run(1, prog, queues[1])]
current, other = 0, 1
snd_count = 0
while True:
    res = next(progs[current])
    if res == "r":
        current, other = other, current
    else:
        queues[other].put(res)
        if current == 1:
            snd_count += 1
            print(snd_count) # TODO: detect termination