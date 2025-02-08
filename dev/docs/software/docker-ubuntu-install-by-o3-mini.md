
# Docker and Docker Compose Installation Guide

## Prerequisites

- Ubuntu 20.04 LTS or Ubuntu 22.04 LTS (recommended)
- `sudo` access on the system
- Stable internet connection

---

## 1. Update System Packages

Ensure your system packages are up-to-date:

```bash
sudo apt update && sudo apt upgrade -y
```

---

## 2. Install Required Dependencies

Install packages to allow `apt` to use HTTPS repositories:

```bash
sudo apt install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

---

## 3. Add Docker’s Official GPG Key

Import Docker's GPG key for secure package verification:

```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

---

## 4. Set Up Docker Repository

Add the Docker repository to APT sources:

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

---

## 5. Install Docker Engine

1. Update the package index:
   ```bash
   sudo apt update
   ```

2. Install Docker components:
   ```bash
   sudo apt install -y \
       docker-ce \
       docker-ce-cli \
       containerd.io \
       docker-buildx-plugin
   ```

---

## 6. Install Docker Compose

1. Download the Docker Compose binary (replace `v2.27.0` with the [latest release](https://github.com/docker/compose/releases) if needed):
   ```bash
   sudo curl -SL https://github.com/docker/compose/releases/download/v2.27.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
   ```

2. Apply executable permissions:
   ```bash
   sudo chmod +x /usr/local/bin/docker-compose
   ```

---

## 7. Post-Installation Steps

### A. Manage Docker as a Non-Root User
Add your user to the `docker` group to run Docker without `sudo`:
```bash
sudo usermod -aG docker $USER
```
**Reboot or log out/in** for changes to take effect.

### B. Enable Docker Service at Boot
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

---

## 8. Verify Installation

1. Check Docker version:
   ```bash
   docker --version
   ```

2. Check Docker Compose version:
   ```bash
   docker-compose --version
   ```

3. Test Docker functionality:
   ```bash
   docker run hello-world
   ```

---

## 9. Uninstallation (Optional)

### Remove Docker
```bash
sudo apt purge -y docker-ce docker-ce-cli containerd.io
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd
```

### Remove Docker Compose
```bash
sudo rm /usr/local/bin/docker-compose
```

---

## Conclusion

- Docker and Docker Compose are now ready for containerized workflows.
- Use `docker-compose up` to start multi-container applications.
