# AXIS Spatial Anomaly Classifier (SAC)

The AXIS Spatial Anomaly Classifier categorizes anomalies detected by the
Spatial Anomaly Detector (SAD) into structured classes for automated
diagnostics, optimization, and AI-driven correction.

## Classification Domains

### Movement Classification
Labels:
- Jitter spikes
- Path discontinuities
- Non-normalized vectors

### Signal Classification
Labels:
- Channel overlap
- Event storms
- Timing drift

### Trace Classification
Labels:
- Over-dense checkpoints
- Missing anchors
- Temporal compression

### Memory Classification
Labels:
- Stale buffers
- Orphaned vectors
- Unreachable anchors

## Classifier Pipeline
- Ingest anomaly report
- Apply spatial classifiers
- Generate structured anomaly taxonomy

## Output
A machine-readable anomaly classification map for diagnostics and AI correction.
