# Installing Ollama with Docker

## Overview

This guide explains how to install and run Ollama using Docker. Ollama is an open-source platform that allows you to run large language models locally, making it ideal for developers who need offline AI capabilities.

## Prerequisites

Before proceeding with the installation, ensure you have:

- Docker installed on your system
- At least 8GB RAM (recommended)
- Sufficient storage space (varies by model)
- Docker Compose (optional, but recommended)

## Basic Docker Installation

### 1. Pull the Official Image

```bash
docker pull ollama/ollama
```

### 2. Run Ollama Container

```bash
docker run -d \
  --name ollama \
  -p 11434:11434 \
  -v ollama:/root/.ollama \
  ollama/ollama
```

### Understanding the Docker Run Command

- `-d`: Runs the container in detached mode
- `--name ollama`: Names the container "ollama"
- `-p 11434:11434`: Maps the container's port to host port
- `-v ollama:/root/.ollama`: Creates a volume for persistent storage

## Using Docker Compose (Recommended)

### 1. Create Docker Compose File

Create a `docker-compose.yml` file:

```yaml
version: '3.8'

services:
  ollama:
    container_name: ollama
    image: ollama/ollama:latest
    ports:
      - "11434:11434"
    volumes:
      - ollama:/root/.ollama
    restart: unless-stopped

volumes:
  ollama:
```

### 2. Start Ollama with Docker Compose

```bash
docker compose up -d
```

## Verifying the Installation

### 1. Check Container Status

```bash
docker ps
```

### 2. Test Ollama API

```bash
curl http://localhost:11434/api/tags
```

## Running Your First Model

### 1. Pull a Model

```bash
docker exec -it ollama ollama pull llama2
```

### 2. Run a Basic Query

```bash
docker exec -it ollama ollama run llama2 "Hello, how are you?"
```

## Common Operations

### Stopping the Container

```bash
docker stop ollama
```

### Starting the Container

```bash
docker start ollama
```

### Viewing Logs

```bash
docker logs ollama
```

## Troubleshooting

### Common Issues and Solutions

1. **Port Conflict**
   - Error: "port 11434 already in use"
   - Solution: Change the port mapping or stop the conflicting service

2. **Insufficient Memory**
   - Error: Container exits immediately
   - Solution: Increase Docker memory allocation in Docker Desktop settings

3. **Permission Issues**
   - Error: "permission denied" for volume
   - Solution: Check Docker volume permissions and ownership

## Best Practices

1. Always use version tags for production deployments
2. Implement health checks for container monitoring
3. Use Docker volumes for persistent storage
4. Regular backup of the ollama volume
5. Monitor resource usage

## Security Considerations

1. Avoid running as root inside the container
2. Restrict network access if running in production
3. Regularly update the Ollama image
4. Use Docker secrets for sensitive configurations

## Additional Resources

- [Official Ollama Documentation](https://ollama.ai/docs)
- [Ollama GitHub Repository](https://github.com/ollama/ollama)
- [Docker Documentation](https://docs.docker.com/)
