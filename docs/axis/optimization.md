# AXIS Optimization Passes

AXIS includes a series of optimization passes that refine DSL programs,
improve spatial bytecode efficiency, and reduce VM execution overhead.

## 1. Constant Folding
Simplifies expressions at compile time.

Example:
PUSH 2
PUSH 3
COMPUTE ADD

Becomes:
PUSH 5

## 2. Dead Movement Elimination
Removes spatial MOV_3D instructions that do not affect final VM state.

## 3. Trace Compaction
Merges redundant TRACE operations to reduce visualizer load.

## 4. Vector Stream Normalization
Ensures consistent scaling of spatial vectors for:
- AST rendering
- WebGL playback
- Sovereign telemetry analysis

## 5. Signal Deduplication
Eliminates repeated SIGNAL events emitted within the same VM cycle.

## 6. Spatial Path Smoothing
Applies geometric smoothing to VM movement paths for cleaner visualization.

