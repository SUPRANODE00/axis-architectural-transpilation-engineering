# AXIS VM Micro-Ops

Micro-ops are the smallest atomic operations executed by the AXIS VM.

## Micro-Op Categories

### 1. Movement Micro-Ops
- MOP_X_POS
- MOP_Y_POS
- MOP_Z_POS

### 2. Stack Micro-Ops
- MOP_PUSH
- MOP_POP
- MOP_COMPUTE_ADD
- MOP_COMPUTE_SUB
- MOP_COMPUTE_MUL
- MOP_COMPUTE_DIV

### 3. Signal Micro-Ops
- MOP_SIGNAL_EMIT

### 4. Trace Micro-Ops
- MOP_TRACE_POINT

## Execution Model
Each bytecode instruction expands into 1–N micro-ops.

This enables:
- Fine-grained VM debugging
- Precise timeline visualization
- Deterministic replay
