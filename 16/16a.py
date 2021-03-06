import inspect
import re

class Scenario:
    def __init__(self, before, instruction, after):
        self.before = before
        self.instruction = instruction
        self.after = after

class Instruction:
    def __init__(self, instruction):
        self.instruction = instruction
        
class Cpu:
    def __init__(self):
        self.regs = [0] * 4
    
    def methods(self):
        return map(lambda x: x[0][6:], self.__methods())
    
    def __methods(self):
        return filter(lambda x: x[0].startswith('instr_'), inspect.getmembers(self, inspect.ismethod))
    
    def invoke(self, method, a, b, c):
        for n, f in self.__methods():
            if n == "instr_" + method:
                f(a, b, c)
    
    def instr_addr(self, a, b, c):
        self.regs[c] = self.regs[a] + self.regs[b]
        
    def instr_addi(self, a, b, c):
        self.regs[c] = self.regs[a] + b
        
    def instr_mulr(self, a, b, c):
        self.regs[c] = self.regs[a] * self.regs[b]
        
    def instr_muli(self, a, b, c):
        self.regs[c] = self.regs[a] * b
        
    def instr_banr(self, a, b, c):
        self.regs[c] = self.regs[a] & self.regs[b]
        
    def instr_barn(self, a, b, c):
        self.regs[c] = self.regs[a] & b
        
    def instr_borr(self, a, b, c):
        self.regs[c] = self.regs[a] | self.regs[b]
        
    def instr_bori(self, a, b, c):
        self.regs[c] = self.regs[a] | b
        
    def instr_setr(self, a, b, c):
        self.regs[c] = self.regs[a]
        
    def instr_seti(self, a, b, c):
        self.regs[c] = a
        
    def instr_gtir(self, a, b, c):
        if a > self.regs[b]:
            self.regs[c] = 1
        else:
            self.regs[c] = 0
            
    def instr_gtri(self, a, b, c):
        if self.regs[a] > b:
            self.regs[c] = 1
        else:
            self.regs[c] = 0
            
    def instr_gtrr(self, a, b, c):
        if self.regs[a] > self.regs[b]:
            self.regs[c] = 1
        else:
            self.regs[c] = 0
            
    def instr_eqir(self, a, b, c):
        if a == self.regs[b]:
            self.regs[c] = 1
        else:
            self.regs[c] = 0
            
    def instr_eqri(self, a, b, c):
        if self.regs[a] == b:
            self.regs[c] = 1
        else:
            self.regs[c] = 0
            
    def instr_eqrr(self, a, b, c):
        if self.regs[a] == self.regs[b]:
            self.regs[c] = 1
        else:
            self.regs[c] = 0

scenarios = []
program = []

in_scenario = False
scenario_before = []
scenario_intruction = []

while True:
    try:
        line = raw_input()
    except EOFError:
        break

    if in_scenario:
        if line.startswith("After:"):
            m = re.match("^After:  \[([0-9]+), ([0-9]+), ([0-9]+), ([0-9]+)\]$", line)
            scenario_after = [int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))]
            scenarios.append(Scenario(scenario_before, scenario_intruction, scenario_after))
            in_scenario = False
        else:
            m = re.match("^([0-9]+) ([0-9]+) ([0-9]+) ([0-9]+)$", line)
            scenario_intruction = [int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))]
            
    else:
        if not line == "":
            if line.startswith("Before:"):
                in_scenario = True
                m = re.match("^Before: \[([0-9]+), ([0-9]+), ([0-9]+), ([0-9]+)\]$", line)
                scenario_before = [int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))]
            else:
                m = re.match("^([0-9]+) ([0-9]+) ([0-9]+) ([0-9]+)$", line)
                program.append(Instruction([int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))]))

cpu = Cpu()
methods = cpu.methods()

mge3 = 0
for s in scenarios:
    matches = 0
    for m in methods:
        cpu.regs = [s.before[0], s.before[1], s.before[2], s.before[3]]
#        print "Before:", cpu.regs
        cpu.invoke(m, s.instruction[1], s.instruction[2], s.instruction[3])
#        print m, s.instruction[1], s.instruction[2], s.instruction[3]
#        print "After: ", cpu.regs
        match = True
        for i in range(4):
            if not cpu.regs[i] == s.after[i]:
                match = False
        if match:
            matches += 1
    if matches > 2:
        mge3 += 1

print mge3
