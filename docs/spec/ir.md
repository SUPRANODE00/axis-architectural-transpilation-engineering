# AXIS Intermediate Representation (IR)

The AXIS IR is a structured, architecture-neutral layer between
the DSL parser and the spatial bytecode generator.

## IR Goals
- Provide a stable transformation target for optimizations
- Decouple DSL syntax from VM bytecode
- Enable analysis of spatial and logical structure
- Support deterministic lowering into spatial bytecode

## IR Node Types
- IRProgram
- IRBlock
- IRMove3D(x, y, z)
- IRPush(value)
- IRSignal(channel)
- IRCompute(op)
- IRTrace()

## IR Structure
An AXIS IR program consists of:

- A sequence of IRBlock nodes
- Each IRBlock contains ordered IR instructions
- Instructions are side-effect aware and spatially annotated

## IR Optimization Layer
Optimization passes operate primarily on IR:

- Constant folding
- Dead movement elimination
- Trace compaction
- Vector stream normalization
- Signal deduplication
- Spatial path smoothing

## IR → Bytecode Lowering
The IR is lowered to spatial bytecode via:

- IRMove3D → MOV_3D
- IRPush → PUSH
- IRSignal → SIGNAL
- IRCompute → COMPUTE
- IRTrace → TRACE
- IR structural markers → control flow metadata

