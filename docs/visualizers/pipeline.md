# AXIS Pipeline Visualization

The AXIS Pipeline Visualizer provides a unified view of the entire
transpilation process from DSL input to VM execution.

## Visualization Stages

### 1. DSL Parsing
Displays:
- Token stream
- Grammar rule matches
- Parse tree structure

### 2. IR Construction
Shows:
- IR blocks
- Instruction flow
- Spatial annotations

### 3. Optimization Passes
Highlights:
- Constant folding
- Dead movement elimination
- Trace compaction
- Vector normalization

### 4. Bytecode Generation
Renders:
- MOV_3D sequences
- SIGNAL and COMPUTE operations
- TRACE checkpoints

### 5. VM Execution
Provides:
- Micro-op timeline
- Register state transitions
- Spatial path rendering

## Output
A full pipeline diagram for debugging, teaching, and architectural analysis.
