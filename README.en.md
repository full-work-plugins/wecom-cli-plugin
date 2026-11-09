# WeCom CLI plugin

This package supplies `wecom-cli-setup` and `wecom-cli-use` Skills for the locally installed vendor CLI. Install this directory as a local Agent Plugin, run setup to verify CLI and identity, then use cli with live command discovery. Installing this plugin package does not automatically install the CLI. The setup Skill can install it using the upstream method after user authorization, then verify the result. The package does not bundle the CLI binary or credentials. Remote writes require an explicit target and user confirmation.

Workflow adapted from the [ZCode `wecom-cli` plugin](https://github.com/zai-org/zcode-plugins/tree/0cc58d6/plugins/wecom-cli); commands come from the [vendor CLI](https://github.com/WecomTeam/wecom-cli). See [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).
