# AXIS Spatial Type System

The AXIS Spatial Type System defines the rules governing spatial values,
vectors, and movement semantics.

## Core Types

### 1. Scalar
A single numeric value used for:
- PUSH operations
- COMPUTE operands

### 2. Vector3
A 3D spatial vector:
- MOV_3D(x, y, z)
- IRMove3D nodes
- Spatial normalization

### 3. SignalType
Represents:
- SIGNAL channels
- Event markers
- Visualizer hooks

### 4. TraceType
Represents:
- Spatial checkpoints
- VM timeline anchors

## Type Rules

### Movement Rules
- Vector3 must be normalized before scheduling
- MOV_3D cannot accept scalar operands
- Spatial operations must preserve dimensionality

### Compute Rules
- COMPUTE operations require scalar operands
- Mixed-type arithmetic is disallowed

### Signal Rules
- SIGNAL channels must be declared before use
- Duplicate signals in the same cycle are optimized away

## Guarantees
- Deterministic spatial semantics
- Safe lowering from IR to bytecode
- Consistent behavior across all visualizers
