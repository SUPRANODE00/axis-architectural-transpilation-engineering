# AXIS Control-Flow Graph (CFG)

The AXIS CFG models execution flow through IR blocks and bytecode segments.

## CFG Nodes
- Basic blocks
- Movement clusters
- Compute segments
- Signal emission points
- Trace checkpoints

## CFG Edges
Edges represent:
- Sequential execution
- Conditional branches (future extension)
- Spatial dependency transitions

## CFG Uses
- Optimization analysis
- Dead movement detection
- Trace compaction
- Spatial scheduling
- VM timeline visualization

## CFG Guarantees
- Deterministic traversal
- No implicit side effects
- Spatially annotated edges
