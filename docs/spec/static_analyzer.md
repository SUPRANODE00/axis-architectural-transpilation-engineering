# AXIS Static Analyzer

The AXIS Static Analyzer inspects DSL and IR programs without executing them.

## Analysis Capabilities

### 1. Structural Analysis
- Detects unreachable IR blocks
- Identifies redundant movement clusters
- Flags unused SIGNAL channels

### 2. Type & Value Analysis
- Ensures numeric consistency
- Validates vector dimensions
- Checks COMPUTE operand compatibility

### 3. Spatial Safety Analysis
- Detects extreme movement spikes
- Flags jitter-prone path segments
- Ensures TRACE density is within limits

### 4. Optimization Hints
Provides suggestions for:
- Movement smoothing
- Constant folding
- Dead movement elimination

## Output
A static report describing structural, spatial, and semantic properties.
