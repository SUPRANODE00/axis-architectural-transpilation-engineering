# AXIS Spatial Bytecode Reference

AXIS bytecode is designed for spatial computation and 3D architectural mapping.

## Core Instructions

### MOV_3D x y z
Moves the VM cursor in 3D space.

### PUSH value
Pushes a scalar onto the VM stack.

### SIGNAL channel
Emits a spatial signal for visualizers.

### COMPUTE op
Performs arithmetic or logical operations.

### TRACE
Records the current VM position for visualization.

## Execution Guarantees
- Deterministic movement
- Stack-safe operations
- Spatial trace consistency

