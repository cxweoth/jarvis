# jarvis
## Python version
Build on Python 3.11.8
## OS
MAC OS
## Basic Install
```
brew install portaudio
pip install -r requirements.txt
pip install "uvicorn[standard]"
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/macos_arm64
```
## Install Whisper within MLX (Machine Learning exChange)

1. Install Whisper
    ```
    pip install git+https://github.com/openai/whisper.git
    ```
2. Copy convert.py from [Link](https://github.com/ml-explore/mlx-examples/tree/main/) and git ignore it.
3. Copy whisper folder from [Link](https://github.com/ml-explore/mlx-examples/tree/main/)
## Models
- Whisper [Link](https://github.com/openai/whisper) with MLX convert [Link](https://github.com/ml-explore/mlx-examples/tree/main/whisper)

# Ref
- [JARVIS-ChatGPT: A conversational assistant equipped with J.A.R.V.I.S's voice](https://github.com/BolisettySujith/J.A.R.V.I.S?tab=readme-ov-file)
- [MLX Whisper](https://github.com/ml-explore/mlx-examples/tree/main/whisper)
- [A Simple Voice Assistant Script](https://github.com/linyiLYi/voice-assistant): Lin-Yi
- [Llama build up](https://medium.com/@cch.chichieh/%E7%94%A8%E6%89%8B%E6%A9%9F%E5%B0%B1%E8%83%BD%E8%B7%91-llama-2-llama-cpp-%E6%95%99%E5%AD%B8-2451807f8ba5)