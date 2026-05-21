# audio-compare-testbed
A specialized Python testing tool to analyze, visualize, and compare audio signals. Evaluates acoustic differences using waveform alignment, Fast Fourier Transforms (FFT), and Mean Squared Error metrics.
# Audio Comparison & Fidelity Testing Suite

A modular Python framework designed to programmatically test, compare, and analyze differences between audio signals. Whether you are benchmarking audio compression algorithms, verifying noise-reduction filters, or checking audio alignment, this tool provides both mathematical metrics and visual graphs to map acoustic variance.

---

## 📐 Mathematical & Signal Metrics

The codebase evaluates the disparity between a **Reference Audio File** and a **Test Audio File** across multiple domains:

1. **Time-Domain Waveform Differences:** Directly subtracts synchronized signal amplitudes to calculate absolute error over time.
2. **Mean Squared Error (MSE) & Signal-to-Noise Ratio (SNR):** Quantifies overall signal degradation and fidelity drops mathematically.
3. **Frequency-Domain Analysis (FFT):** Uses Fast Fourier Transforms to convert raw time signals into spectral frequencies, exposing exactly which pitches or frequencies were lost or altered.

---

## 🚀 Core Features

- **Dual-Waveform Visualization:** Overlays the reference and test waveforms side-by-side or on a unified plot for visual inspection.
- **Spectral Difference Mapping:** Generates spectrogram differentials to pinpoint where compression artifacts or noise distortions occur.
- **Automated Gain & Phase Alignment:** Simple normalization hooks to match audio volumes before performing data subtraction tests.
- **Batch Testing Support:** Easily expandable to script-test entire directories of audio files against a single baseline standard.

---

## 📁 Repository Directory Structure

```text
├── audio_samples/         # Storage for audio files (.wav, .mp3)
│   ├── reference.wav      # The clean, baseline original audio track
│   └── test_compressed.wav# The modified, degraded, or processed test track
├── src/                   # Source code scripts
│   ├── audio_loader.py    # Standardized audio reading and normalization utilities
│   ├── compare_engine.py  # Core mathematical analysis (FFT, MSE, SNR calculations)
│   └── main.py            # Execution file generating analytics dashboards and plots
├── requirements.txt       # Software package dependencies
└── README.md              # Project documentation
