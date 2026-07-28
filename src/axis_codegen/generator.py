from src.axis_transform.transpiler_visitors import TranspilerVisitor

class JavaScriptCodeGenerator(TranspilerVisitor):
    def __init__(self):
        self.code_output = []

    def visit_Module(self, node):
        self.code_output.append(f"// Generated JS for Module: {node.name}")
        for child in node.children:
            self.visit(child)
        return "\n".join(self.code_output)

    def visit_FunctionDecl(self, node):
        self.code_output.append(f"function {node.name}() {{")
        self.code_output.append(f"    console.log('Executing AXIS compute node: {node.name}');")
        self.code_output.append("}")

    def visit_SignalHook(self, node):
        self.code_output.append(f"// Signal Hook: {node.name} [Severity: {node.severity}]")
        self.code_output.append(f"registerSignalHook('{node.name}', {{x: {node.resource.x}, y: {node.resource.y}, z: {node.resource.z}}});")
