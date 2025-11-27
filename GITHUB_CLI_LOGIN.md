# GitHub CLI 登录指南

## 方法 1: 使用浏览器登录（推荐）

在 PowerShell 中运行：

```powershell
cd C:\Users\zyjst\awesome-ai-tools
gh auth login
```

然后按照提示操作：
1. 选择 `GitHub.com`
2. 选择 `HTTPS` 协议
3. 选择 `Login with a web browser`
4. 按 `Enter` 键
5. 复制显示的代码
6. 浏览器会自动打开，如果没有，手动访问显示的 URL
7. 粘贴代码并授权
8. 完成登录

## 方法 2: 使用 Personal Access Token 登录

### 步骤 1: 创建 GitHub Token

1. 访问：https://github.com/settings/tokens
2. 点击 "Generate new token" → "Generate new token (classic)"
3. 填写信息：
   - Note: `GitHub CLI - awesome-ai-tools`
   - Expiration: 选择合适的时间（建议 90 天或 No expiration）
   - 勾选权限：✅ **repo** (Full control of private repositories)
4. 点击 "Generate token"
5. **立即复制 token**（只显示一次！）

### 步骤 2: 使用 Token 登录

```powershell
cd C:\Users\zyjst\awesome-ai-tools
gh auth login --with-token
```

然后粘贴你的 token 并按 Enter。

或者直接：

```powershell
echo YOUR_TOKEN_HERE | gh auth login --with-token
```

（将 `YOUR_TOKEN_HERE` 替换为你的 token）

## 验证登录

登录后，验证是否成功：

```powershell
gh auth status
```

应该显示类似：
```
✓ Logged in to github.com as kostja94
```

## 登录后创建仓库

登录成功后，运行：

```powershell
cd C:\Users\zyjst\awesome-ai-tools
gh repo create awesome-ai-tools --public --description "A curated list of AI/SaaS products with personal insights and growth perspectives" --source=. --remote=origin --push
```

这会自动：
1. 在 GitHub 上创建仓库
2. 添加远程仓库
3. 推送代码

