# AXIS VM Register Specification

The AXIS VM uses a minimal deterministic register set.

## Core Registers

### R_POS
Current 3D position of the VM cursor.

### R_STACK
Primary stack for PUSH and COMPUTE operations.

### R_SIGNAL
Holds the last emitted SIGNAL channel.

### R_TRACE
Stores the most recent TRACE checkpoint.

## Execution Guarantees
- Registers are updated deterministically.
- No external side effects.
- Spatial consistency across all visualizers.

