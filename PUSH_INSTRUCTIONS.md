# 推送代码到 GitHub 的说明

由于网络连接问题，可能需要手动推送。以下是几种方法：

## 方法 1: 使用 HTTPS（需要认证）

如果推送时提示需要认证，Git 会弹出窗口要求输入：
- **Username**: `kostja94`
- **Password**: 使用你的 **Personal Access Token**（不是 GitHub 密码）

### 创建 Personal Access Token（如果还没有）

1. 访问：https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 勾选 `repo` 权限
4. 生成并复制 token

### 推送命令

```powershell
cd C:\Users\zyjst\awesome-ai-tools
git push -u origin main
```

当提示输入密码时，粘贴你的 Personal Access Token。

## 方法 2: 使用 SSH（推荐，避免每次输入密码）

### 步骤 1: 检查是否有 SSH 密钥

```powershell
ls ~/.ssh
```

### 步骤 2: 如果没有 SSH 密钥，生成一个

```powershell
ssh-keygen -t ed25519 -C "your_email@example.com"
```

按 Enter 使用默认位置，设置密码（可选）。

### 步骤 3: 添加 SSH 密钥到 GitHub

1. 复制公钥内容：
   ```powershell
   cat ~/.ssh/id_ed25519.pub
   ```
   或
   ```powershell
   type C:\Users\zyjst\.ssh\id_ed25519.pub
   ```

2. 访问：https://github.com/settings/keys
3. 点击 "New SSH key"
4. 粘贴公钥内容并保存

### 步骤 4: 更改远程 URL 为 SSH

```powershell
cd C:\Users\zyjst\awesome-ai-tools
git remote set-url origin git@github.com:kostja94/awesome-ai-tools.git
git push -u origin main
```

## 方法 3: 使用 GitHub Desktop

1. 下载并安装 GitHub Desktop：https://desktop.github.com/
2. 打开 GitHub Desktop
3. File → Add Local Repository
4. 选择 `C:\Users\zyjst\awesome-ai-tools`
5. 点击 "Publish repository"

## 方法 4: 使用 GitHub CLI（如果已登录）

```powershell
cd C:\Users\zyjst\awesome-ai-tools
gh repo sync
```

或者：

```powershell
git push -u origin main
```

## 验证推送成功

推送成功后，访问 https://github.com/kostja94/awesome-ai-tools 应该能看到所有文件。

## 如果仍然遇到问题

- 检查网络连接
- 尝试使用 VPN
- 检查防火墙设置
- 使用 GitHub Desktop 图形界面工具


