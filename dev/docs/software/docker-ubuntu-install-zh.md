# Docker 安裝指南 - Ubuntu

本文檔將指導您如何在 Ubuntu 系統上安裝 Docker Engine 和 Docker Compose。

## 系統需求

- Ubuntu 版本：20.04 LTS 或更新版本
- 具有 sudo 權限的用戶帳戶
- 終端機訪問權限

## 安裝 Docker Engine

### 1. 更新系統套件
```bash
sudo apt update
sudo apt upgrade -y
```

### 2. 安裝必要的依賴套件
```bash
sudo apt install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

### 3. 添加 Docker 官方 GPG 密鑰
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

### 4. 設置 Docker 倉庫
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### 5. 安裝 Docker Engine
```bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
```

### 6. 驗證安裝
```bash
sudo docker run hello-world
```

### 7. 將當前用戶添加到 docker 群組（可選但推薦）
```bash
sudo usermod -aG docker $USER
```
> 注意：添加用戶到 docker 群組後需要重新登入才能生效

## 安裝 Docker Compose

### 1. 下載最新版本的 Docker Compose
```bash
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

### 2. 設置執行權限
```bash
sudo chmod +x /usr/local/bin/docker-compose
```

### 3. 驗證安裝
```bash
docker-compose --version
```

## 常見問題排解

### Docker 服務無法啟動
如果 Docker 服務無法啟動，可以嘗試以下命令：
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

### 查看 Docker 服務狀態
```bash
sudo systemctl status docker
```

### 移除舊版本 Docker
如果需要移除舊版本的 Docker：
```bash
sudo apt remove docker docker-engine docker.io containerd runc
```

## 基本使用範例

### 1. 檢查 Docker 版本
```bash
docker --version
docker-compose --version
```

### 2. 檢查 Docker 系統信息
```bash
docker info
```

### 3. 列出所有運行中的容器
```bash
docker ps
```

### 4. 列出所有容器（包括已停止的）
```bash
docker ps -a
```

## 參考資料

- [Docker 官方文檔](https://docs.docker.com/)
- [Docker Compose 官方文檔](https://docs.docker.com/compose/)
- [Ubuntu 官方文檔](https://ubuntu.com/server/docs)