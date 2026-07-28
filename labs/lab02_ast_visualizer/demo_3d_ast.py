from src.axis_ast.ast_3d import Axis3DNode, attach_3d_resource


def build_demo_ast():
    root = Axis3DNode(kind="Module", name="AXIS_DSL")

    fn = Axis3DNode(kind="FunctionDecl", name="governance_rule")
    attach_3d_resource(fn, x=1.0, y=0.2, z=0.8, layer="compute", severity="info")

    sig = Axis3DNode(kind="SignalHook", name="forensics_trace")
    attach_3d_resource(sig, x=2.0, y=0.5, z=0.3, layer="signal", severity="critical")

    root.add_child(fn)
    root.add_child(sig)
    return root


if __name__ == "__main__":
    ast = build_demo_ast()
    print(ast)
