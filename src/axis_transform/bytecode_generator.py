from src.axis_codegen.instruction_builder import build_instructions_from_ast

class BytecodeGenerator:
    def generate(self, ast_root):
        return build_instructions_from_ast(ast_root)
