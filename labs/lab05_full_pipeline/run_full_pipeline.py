import sys, os

repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(repo_root)

from src.axis_parser.parser import AxisParser
from src.axis_codegen.generator import JavaScriptCodeGenerator
from src.axis_transform.bytecode_generator import BytecodeGenerator
from src.axis_bytecode_vm.vm import AxisBytecodeVM

tokens = ["govern", "trace", "signal", "compute"]

# 1. Parse → 3D AST
parser = AxisParser()
ast = parser.parse(tokens)

# 2. Transpile → JavaScript
js_gen = JavaScriptCodeGenerator()
js_code = js_gen.visit(ast)

# 3. Generate → Bytecode
byte_gen = BytecodeGenerator()
instructions = byte_gen.generate(ast)

# 4. Execute → VM
vm = AxisBytecodeVM()
vm.execute(instructions)

print("=== AXIS 3D AST ===")
print(ast)
print("\n=== AXIS JavaScript Output ===")
print(js_code)
print("\n=== AXIS Bytecode Instructions ===")
print(instructions)
print("\n=== AXIS VM Execution State ===")
print("Stack:", vm.stack)
print("Registers:", vm.registers)
from labs.lab06_visualizer.mpl_3d_plot import plot_ast_3d
plot_ast_3d(ast)
from labs.lab06_visualizer.mpl_3d_plot import plot_ast_3d
plot_ast_3d(ast)
