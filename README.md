# 企业微信 CLI 插件

使用本机 `wecom-cli` CLI 完成日常办公操作。插件提供 `wecom-cli-setup`（安装/认证检查）和 `wecom-cli-use`（按实时帮助执行业务命令）两个 Skill。

## 使用

1. 将本目录作为本地插件安装到支持 Agent Plugins 的宿主。
2. 调用 `wecom-cli-setup` 检查本机 CLI 与身份；确需安装或登录时按 Skill 引导操作。
3. 调用 `wecom-cli-use`，先发现当前 CLI 的命令/schema，再执行目标任务。

安装插件包时不会自动安装 CLI；运行 setup Skill 后，若本机缺少 CLI，可在用户授权后按上游方式安装并验证。插件不打包 CLI 二进制或账号凭证，也不证明已完成真实 SaaS/云端调用。远端写操作按 Skill 要求先展示目标和变更并获得确认。

## 来源

本插件的工作流改写自 [ZCode `wecom-cli` 插件](https://github.com/zai-org/zcode-plugins/tree/0cc58d6/plugins/wecom-cli)；实际命令由[厂商 CLI](https://github.com/WecomTeam/wecom-cli)提供。具体版本、作者和许可见 [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md)。
