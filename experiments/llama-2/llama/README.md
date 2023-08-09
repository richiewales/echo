# Llama 2 on CPU, and Mac M1/M2 GPU

This is a fork of https://github.com/facebookresearch/llama that runs on CPU and Mac M1/M2 GPU (mps) if available.

Please refer to the official installation and usage instructions as they are exactly the same.

<img width="978" alt="image" src="https://github.com/krychu/llama/assets/947457/8a7bd5c8-1d45-4835-8463-64e12486d0e9">

MacBook Pro M1 with 7B model:
- MPS (default): ~4.3 words per second
- CPU: ~0.67 words per second

There is also an extra message shown during text generation that reports the number and speed at which tokens are being generated.
