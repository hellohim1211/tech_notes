# Open WebUI: Introduction and Installation Guide

## What is Open WebUI?

Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform designed to operate entirely offline. It provides a modern web interface for interacting with various Large Language Models (LLMs) and comes with built-in support for Ollama integration. [4]

### Key Features

- **User-friendly Interface**: Clean and intuitive chat interface with conversation history
- **Model Management**: Easy model installation and switching
- **Multi-Modal Support**: Handle text, images, and code interactions
- **OpenAI API Integration**: Support for OpenAI-compatible APIs alongside Ollama models
- **Offline Operation**: Run completely offline for privacy and security
- **Cross-Platform**: Works on Windows, macOS, and Linux [2]

## System Requirements

- Docker installed on your system
- Minimum 8GB RAM recommended
- 10GB free disk space
- Internet connection (for initial setup and model downloads) [1]

## Installation Methods

### Method 1: Docker Compose (Recommended)

1. Create a new directory and navigate to it:
```bash
mkdir open-webui && cd open-webui
```

2. Create a `docker-compose.yml` file with the following content:
```yaml
version: '3.8'
services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    volumes:
      - ./ollama:/root/.ollama
    ports:
      - "11434:11434"

  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    volumes:
      - ./open-webui:/data
    ports:
      - "3000:8080"
    environment:
      - OLLAMA_API_BASE_URL=http://ollama:11434/api
    depends_on:
      - ollama
```

3. Start the containers:
```bash
docker-compose up -d
```

4. Access the interface at `http://localhost:3000` [1]

### Method 2: All-in-One Docker Image

For a simpler setup, you can use the bundled image that includes both Open WebUI and Ollama:

```bash
docker run -d \
  --name open-webui \
  -v open-webui:/data \
  -p 3000:8080 \
  --restart always \
  ghcr.io/open-webui/open-webui-standalone:main
```

Access the interface at `http://localhost:3000` [2]

## Post-Installation Steps

1. **First Launch**:
   - Open your browser and navigate to `http://localhost:3000`
   - Create your admin account on first launch
   - Select and download your preferred LLM model [4]

2. **Model Installation**:
   - Click on the 'Models' tab in the interface
   - Choose from available models
   - Wait for the download to complete [2]

3. **API Configuration** (Optional):
   - Navigate to Settings
   - Configure OpenAI-compatible API endpoints if needed
   - Set up any additional parameters for model interaction [3]

## Troubleshooting

Common issues and solutions:

1. **Connection Issues**:
   - Verify Docker containers are running: `docker ps`
   - Check logs: `docker logs open-webui`
   - Ensure ports 3000 and 11434 are not in use [1]

2. **Model Download Failures**:
   - Check available disk space
   - Verify internet connection
   - Review Ollama logs: `docker logs ollama` [2]

## Security Considerations

- The default setup exposes the UI on localhost only
- For remote access, configure proper authentication
- Consider setting up HTTPS if exposing to the internet
- Regularly update both Open WebUI and Ollama containers [1], [4]

## Additional Resources

- [Official Documentation](https://docs.openwebui.com/)
- [GitHub Repository](https://github.com/open-webui/open-webui)
- [Feature Requests and Bug Reports](https://github.com/open-webui/open-webui/issues)
