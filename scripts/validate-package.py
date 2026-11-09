#!/usr/bin/env python3
"""发布前验证本仓插件清单、Skill 和来源声明。"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
core = json.loads((ROOT / 'plugin.json').read_text(encoding='utf-8'))
name = core['name']
version = core['version']
assert re.fullmatch(r'0|[1-9]\d*', version.split('.')[0]) and re.fullmatch(r'\d+\.\d+\.\d+', version), version
assert core['$schema'] == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
for rel in ('kimi.plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json', '.zcode-plugin/plugin.json'):
    item = json.loads((ROOT / rel).read_text(encoding='utf-8'))
    assert item['name'] == name and item['version'] == version and item['description'] == core['description'], rel
market = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text(encoding='utf-8'))
assert len(market['plugins']) == 1
entry = market['plugins'][0]
assert entry['name'] == name and entry['version'] == version and entry['description'] == core['description']
assert entry['source'] == {'source': 'url', 'url': f'https://github.com/full-work-plugins/{name}-plugin.git', 'ref': f'v{version}'}
assert (ROOT / 'assets/logo.png').is_file()
assert entry['icon'].endswith(f'@v{version}/assets/logo.png')
for suffix in ('setup', 'use'):
    skill = f'{name}-{suffix}'
    text = (ROOT / 'skills' / skill / 'SKILL.md').read_text(encoding='utf-8')
    assert re.search(rf'^name: {re.escape(skill)}$', text, re.M), skill
    assert len(text.splitlines()) < 500
notice = (ROOT / 'THIRD-PARTY-NOTICES.md').read_text(encoding='utf-8')
assert 'zai-org/zcode-plugins' in notice and '0cc58d6' in notice
print(f'{name} v{version}: package validated')
