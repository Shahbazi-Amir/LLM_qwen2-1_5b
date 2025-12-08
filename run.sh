#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"

"$DIR/llama.cpp/build/bin/llama-server" \
  --model "$DIR/models/qwen2-1_5b-instruct-q4_k_m.gguf" \
  --n-gpu-layers 0
