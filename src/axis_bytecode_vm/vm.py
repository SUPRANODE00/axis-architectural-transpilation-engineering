class AxisBytecodeVM:
    def __init__(self):
        self.stack = []
        self.registers = {"x": 0.0, "y": 0.0, "z": 0.0}
        self.pc = 0
        self.path = []  # optional: for 3D visualization

    def execute(self, instructions):
        while self.pc < len(instructions):
            instr = instructions[self.pc]
            self._dispatch(instr)
            self.pc += 1

    def _dispatch(self, instr):
        op = instr.get("op")
        if op == "PUSH":
            self.stack.append(instr.get("value"))
        elif op == "MOV_3D":
            self.registers["x"] = instr.get("x", 0.0)
            self.registers["y"] = instr.get("y", 0.0)
            self.registers["z"] = instr.get("z", 0.0)
            self.path.append((self.registers["x"], self.registers["y"], self.registers["z"]))
        else:
            raise ValueError(f"Unknown opcode: {op}")
