from src.axis_transform.transpiler_visitors import TranspilerVisitor

class JavaScriptCodeGenerator(TranspilerVisitor):
    def __init__(self):
        self.code_output = []

    # NEW: universal handler for Axis3DNode
    def visit_Axis3DNode(self, node):
        kind = node.kind

        if kind == "Program":
            return self.visit_Module(node)
        elif kind == "FunctionDecl":
            return self.visit_FunctionDecl(node)
        elif kind == "SignalHook":
            return self.visit_SignalHook(node)
        elif kind == "Statement":
            # Generic statement → JS console log
            self.code_output.append(
                f"console.log('AXIS Statement: {node.name}');"
            )
            return "\n".join(self.code_output)
        else:
            raise NotImplementedError(f"No JS generator for kind: {kind}")

    def visit_Module(self, node):
        self.code_output.append(f"// Generated JS for Module: {node.name}")
        for child in node.children:
            self.visit(child)
        return "\n".join(self.code_output)

    def visit_FunctionDecl(self, node):
        self.code_output.append(f"function {node.name}() {{")
        self.code_output.append(
            f"    console.log('Executing AXIS compute node: {node.name}');"
        )
        self.code_output.append("}")

    def visit_SignalHook(self, node):
        self.code_output.append(
            f"// Signal Hook: {node.name} [Severity: {node.severity}]"
        )
        self.code_output.append(
            f"registerSignalHook('{node.name}', "
            f"{{x: {node.resource.x}, y: {node.resource.y}, z: {node.resource.z}}});"
        )
