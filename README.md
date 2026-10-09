# DevOps Copilot Demo Repo

这是一个用于测试 nanobot DevOps Copilot 的最小 GitHub Actions demo 仓库。

它包含：

- 一个简单 Python 包：`demo_pipeline`
- 一个故意失败的 pytest：`tests/test_pipeline.py`
- 一个 GitHub Actions workflow：`.github/workflows/ci.yml`

## 为什么这个 CI 会失败

`parse_build_log()` 当前会把包含 `FAILED` 的日志解析成 `failed` 状态，而测试故意期望它是 `passed`：

```text
AssertionError: assert 'failed' == 'passed'
```

这样可以稳定触发 GitHub Actions 失败，方便测试：

- `github_actions_fetch_logs`
- `github_actions_diagnose`
- `github_actions_pr_comment_draft`

## 本地复现

```bash
cd devops-copilot-demo
python -m pip install -e .
python -m pip install pytest
pytest -q
```

预期结果：测试失败。

## 推到 GitHub 测试

1. 在 GitHub 创建一个空仓库，例如 `devops-copilot-demo`。

2. 在本地执行：

```bash
git remote add origin git@github.com:YOUR_USER/devops-copilot-demo.git
git branch -M main
git push -u origin main
```

3. 打开 GitHub 仓库的 **Actions** 页面，等待 CI 失败。

4. 复制失败 workflow run 的 `run_id`。它通常在 URL 中，例如：

```text
https://github.com/YOUR_USER/devops-copilot-demo/actions/runs/123456789
```

其中 `123456789` 就是 `run_id`。

## 用 nanobot 诊断

在 nanobot WebUI 中输入：

```text
Use github_actions_diagnose on owner=YOUR_USER repo=devops-copilot-demo run_id=123456789.
```

如果是私有仓库，启动 nanobot 前设置：

```bash
export GITHUB_TOKEN=...
python -m nanobot webui
```

也可以生成 PR 评论草稿：

```text
Use github_actions_pr_comment_draft on owner=YOUR_USER repo=devops-copilot-demo run_id=123456789.
```

