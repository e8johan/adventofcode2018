import inspect
import re

class Instruction:
    def __init__(self, instruction, args):
        self.instruction = instruction
        self.args = args
        
    def op(self):
        return self.instruction
    
    def arg(self, index):
        return self.args[index]
        
class Cpu:
    def __init__(self):
        self.regs = [0] * 6
    
    def reset(self):
        self.regs = [0, 0, 0, 0, 0, 0]
    
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

program = []
ip_reg = -1
while True:
    try:
        line = raw_input()
    except EOFError:
        break

    if line.startswith("#ip"):
        m = re.match("^\#ip ([0-9]+)$", line)
        ip_reg = int(m.group(1))
    else:
        m = re.match("^([a-z]+) ([0-9]+) ([0-9]+) ([0-9]+)$", line)
        program.append(Instruction(m.group(1), [int(m.group(2)), int(m.group(3)), int(m.group(4))]))

cpu = Cpu()
ip = 0
while ip >= 0 and ip < len(program):
    if ip_reg in range(6):
        cpu.regs[ip_reg] = ip
        
    cpu.invoke(program[ip].instruction, program[ip].args[0], program[ip].args[1], program[ip].args[2])
    
    if ip_reg in range(6):
        ip = cpu.regs[ip_reg]
        
    ip += 1
    
    
print cpu.regs[0]
