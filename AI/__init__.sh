#!/bin/bash

echo "Installing Ollama..."

# Detect OS
OS="$(uname -s)"

if [ "$OS" = "Darwin" ]; then
    echo "Detected macOS. Installing via Homebrew..."
    brew install ollama
elif [ "$OS" = "Linux" ]; then
    echo "Detected Linux. Installing via curl..."
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "Unsupported OS: $OS"
    exit 1
fi

echo "Starting Ollama service..."
ollama serve &

echo "Ollama installation completed!"
ollama list

echo "Install chat model"
ollama pull deepseek-r1:1.5b
