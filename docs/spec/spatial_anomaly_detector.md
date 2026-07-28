# AXIS Spatial Anomaly Detector (SAD)

The AXIS Spatial Anomaly Detector identifies irregularities in movement,
signal timing, and spatial memory behavior during VM execution.

## Anomaly Classes

### 1. Movement Anomalies
Detects:
- Sudden jitter spikes
- Non-normalized vectors
- Path discontinuities

### 2. Signal Anomalies
Flags:
- Overlapping channel emissions
- Event storms
- Desynchronized visualizer hooks

### 3. Trace Anomalies
Identifies:
- Over-dense checkpoints
- Missing anchors
- Temporal drift

### 4. Memory Anomalies
Reports:
- Stale spatial buffers
- Orphaned vectors
- Unreachable trace anchors

## Detection Pipeline
- Collect spatial metrics
- Run anomaly classifiers
- Generate diagnostic overlays

## Output
A structured anomaly report for debugging and optimization.
