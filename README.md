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
brew install portaudio
pip install -r requirements.txt
pip install "uvicorn[standard]"
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/macos_arm64
```

## Install Whisper within MLX (Machine Learning exChange)

1. Install Whisper
    ```
    pip install git+https://github.com/openai/whisper.git
    ```
2. Copy convert.py from [Link](https://github.com/ml-explore/mlx-examples/tree/main/) and git ignore it.
3. Copy whisper folder from [Link](https://github.com/ml-explore/mlx-examples/tree/main/)

## Install llama_cpp with Apple M1 GPU runnerble version
```
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python
```

# Ref
- [JARVIS-ChatGPT: A conversational assistant equipped with J.A.R.V.I.S's voice](https://github.com/BolisettySujith/J.A.R.V.I.S?tab=readme-ov-file)
- [MLX Whisper](https://github.com/ml-explore/mlx-examples/tree/main/whisper)
- [A Simple Voice Assistant Script](https://github.com/linyiLYi/voice-assistant): Lin-Yi
- [Llama build up](https://medium.com/@cch.chichieh/%E7%94%A8%E6%89%8B%E6%A9%9F%E5%B0%B1%E8%83%BD%E8%B7%91-llama-2-llama-cpp-%E6%95%99%E5%AD%B8-2451807f8ba5)

## Additional Ref
- [Code Llama Intro](https://www.unite.ai/zh-TW/%E6%8E%A2%E7%B4%A2-Code-llama-70b-%E5%85%83%E5%80%A1%E8%AD%B0%EF%BC%8C%E8%AE%93%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E8%BC%94%E5%8A%A9%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88%E6%9B%B4%E5%AE%B9%E6%98%93%E4%BD%BF%E7%94%A8/)
- [VITS tutorial](https://ithelp.ithome.com.tw/articles/10317970)
- [Power Inferenece](https://github.com/SJTU-IPADS/PowerInfer)
