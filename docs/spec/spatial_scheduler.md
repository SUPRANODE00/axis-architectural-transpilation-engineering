# AXIS Spatial Scheduler

The AXIS Spatial Scheduler determines the optimal ordering of spatial
operations before bytecode emission.

## Goals
- Minimize unnecessary movement
- Reduce spatial jitter
- Improve VM execution efficiency
- Maintain deterministic spatial semantics

## Scheduling Stages

### 1. Movement Grouping
Clusters MOV_3D instructions into coherent spatial segments.

### 2. Dependency Resolution
Ensures SIGNAL, COMPUTE, and TRACE operations occur in correct order.

### 3. Spatial Reordering
Reorders movement instructions when safe to reduce total path length.

### 4. Conflict Avoidance
Prevents reordering that would alter:
- Stack state
- Signal timing
- Trace checkpoints

## Output
A fully scheduled IR program ready for bytecode lowering.
