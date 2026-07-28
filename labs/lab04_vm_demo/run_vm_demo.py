import sys, os

repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(repo_root)

from src.axis_parser.parser import AxisParser
from src.axis_transform.bytecode_generator import BytecodeGenerator
from src.axis_bytecode_vm.vm import AxisBytecodeVM

tokens = ["govern", "trace", "signal"]

parser = AxisParser()
ast = parser.parse(tokens)

gen = BytecodeGenerator()
instructions = gen.generate(ast)

vm = AxisBytecodeVM()
vm.execute(instructions)

print("Final Stack:", vm.stack)
print("Registers:", vm.registers)
