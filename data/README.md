# Data Directory

Raw measurement data is not included in this public repository due to confidentiality and operational security considerations.

The code expects input files with the same structure as described in the thesis and notebooks:
- **Sender-end measurements** (voltage, current, phase angles per phase)
- **Receiver-end measurements** (voltage, current, phase angles per phase)
- **Synchronized timestamps** for two-end phasor measurement
- **Sufficient resolution** for 50 Hz power system analysis

## Data Availability

If you have access to the raw measurement data, place it in this directory structure:

```
data/
├── raw/
│   ├── sender/
│   └── receiver/
└── processed/
```

The Python functions in `src/data_loader.py` will handle loading and synchronization.
