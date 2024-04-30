# jarvis

## OS
MAC OS

## Python version
Build on Python 3.11.8

## Models
- Speech to text: Whisper [Link](https://github.com/openai/whisper) with MLX convert [Link](https://github.com/ml-explore/mlx-examples/tree/main/whisper)
- LLM: llama-2-7b.Q4_K_M.gguf [link](https://huggingface.co/TheBloke/toxicqa-Llama2-7B-GGUF/tree/main)

## Basic Install
```
mkdir models
mkdir recordings
brew install portaudio
pip install -r requirements.txt
pip install "uvicorn[standard]"
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/macos_arm64
```

## Install Whisper within MLX (Machine Learning exChange)

1. Follow [MLX Whisper](https://github.com/ml-explore/mlx-examples/tree/main/whisper) instructions to convert whisper-base to MLX version
2. Put whisper model files to models/whisper-base directory

## Put llama model to models directory
1. Download .gguf model llama-2-7b.Q4_K_M.gguf from [link](https://huggingface.co/TheBloke/toxicqa-Llama2-7B-GGUF/tree/main)
2. Put llama-2-7b.Q4_K_M.gguf to models

## Install llama_cpp with Apple M1 GPU runnerble version
```
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python
```
