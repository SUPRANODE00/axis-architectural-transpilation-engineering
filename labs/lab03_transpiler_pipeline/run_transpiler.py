from labs.lab02_ast_visualizer.demo_3d_ast import build_demo_ast
from src.axis_codegen.generator import JavaScriptCodeGenerator

if __name__ == "__main__":
    ast_root = build_demo_ast()
    generator = JavaScriptCodeGenerator()
    js_code = generator.visit(ast_root)
    print("--- Transpiled JavaScript Output ---")
    print(js_code)
