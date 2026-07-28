from labs.lab06_visualizer.mpl_3d_plot import plot_ast_3d

class MockResource:
    def __init__(self, x, y, z, layer):
        self.x = x
        self.y = y
        self.z = z
        self.layer = layer

class MockNode:
    def __init__(self, name, x, y, z):
        self.name = name
        self.kind = "Statement"
        self.resource = MockResource(x, y, z, "signal")

class MockAST:
    def __init__(self):
        self.children = [
            MockNode("govern", 1.0, 0.25, 0.5),
            MockNode("trace", 1.0, 0.5, 0.5),
            MockNode("signal", 1.0, 0.75, 0.5),
            MockNode("compute", 1.0, 1.0, 0.5),
        ]

class MockVM:
    def __init__(self):
        self.path = [(0.0, 0.0, 0.0), (1.0, 0.5, 0.5), (1.0, 1.0, 0.5)]

if __name__ == "__main__":
    ast = MockAST()
    vm = MockVM()
    
    print("=== Executing Full Pipeline with Visualizer ===")
    plot_ast_3d(ast, vm)
