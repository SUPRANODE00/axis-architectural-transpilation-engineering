from src.axis_ast.ast_3d import Axis3DNode, attach_3d_resource

class AxisParser:
    def __init__(self):
        self.tokens = []
        self.position = 0

    def parse(self, tokens):
        self.tokens = tokens
        self.position = 0

        root = Axis3DNode(kind="Program", name="AXIS_DSL")
        attach_3d_resource(root, x=0.0, y=0.0, z=0.0, layer="compute", severity="info")

        while not self._at_end():
            stmt = self._parse_statement()
            if stmt:
                root.add_child(stmt)

        return root

    def _parse_statement(self):
        token = self._advance()
        node = Axis3DNode(kind="Statement", name=str(token))

        attach_3d_resource(
            node,
            x=1.0,
            y=self.position / max(1, len(self.tokens)),
            z=0.5,
            layer="signal",
            severity="info"
        )

        return node

    def _advance(self):
        tok = self.tokens[self.position]
        self.position += 1
        return tok

    def _at_end(self):
        return self.position >= len(self.tokens)
