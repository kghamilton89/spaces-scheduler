# 🤗 Spaces Scheduler

> Please note, this mechanism has been optimized by way of the following three commits: [1](https://huggingface.co/spaces/DIBT-Russian/MPEP_Dashboard/commit/7be166dc69cb857f28c9e78b2c81e741803ea740), [2](https://huggingface.co/spaces/DIBT-Russian/MPEP_Dashboard/commit/a39f9d0c8fe61ba5f2072542debfb790bd6e27f5), [3](https://huggingface.co/spaces/DIBT-Russian/MPEP_Dashboard/commit/ab83c6062d50883cd9b9321ea835739bbe5f1fb9). Whilst the core methodology remains viable, there is a more elegant way to implement this feature according to [this template](https://huggingface.co/spaces/davanstrien/restart/blob/main/app.py).

[Hugging Face Spaces](https://huggingface.co/spaces) offer a simple way to host ML apps directly on the Hugging Face platform.

The [MPEP initiative](https://github.com/huggingface/data-is-better-together/tree/main/prompt_translation), a part of the [DIBT project](https://huggingface.co/DIBT), identifed a use case wherein it would be desireable to have performance dashboards hosted in Spaces refresh on a schedule.

Efforts to build a `BackgroundScheduler()` function in the Gradio app proved [imperfect](https://github.com/huggingface/data-is-better-together/pull/33).

This repository is a lightweight scheduler that leverages [GitHub Actions](https://docs.github.com/en/actions) to externally trigger dashboard rebuild and by extension, data update.

It may be generalized to induce refresh of arbitrary Hugging Face Spaces.

# Usage

Follow these instructions to schedule automated rebuilds of your Hugging Face Space. You need to update the repository to point to the target Space and provide a Hugging Face `write` token.

1. To get started, fork or clone this repository to your own GitHub account.
2. Navigate to `/restart_space.py`.
3. Refer to `restart_space()` function:

```python
def restart_space():
    token = os.environ['HF_TOKEN'] # Please navigate to Settings > Secrets and variables > Actions and define "HF_TOKEN".
    repo_id = "DIBT-Russian/MPEP_Dashboard" #  Please replace this value with the name of your own Hugging Face Space.
```

4. Modify `DIBT-Russian/MPEP_Dashbaord` to point to your Hugging Face Space using the syntax `{{USER OR ORGANIZATION}}/{{SPACE}}`.
5. In the Repository Menu, follow the path `Settings > Secrets and keys > Actions`.
6. On the Secrets tab, click New repository secret.
7. Create a new repository secret called `HF_KEY`.
8. Provide a [Hugging Face token](https://huggingface.co/settings/tokens) with `write` access from the account which owns the target Space.
9. Navigate to `/.github/workflows/restart_hf_space.yaml`.
10. Refer to `cron` schedule: `*/30 * * * *` and update it to your desired value. Please note, inducing rebuild too frequently can result in errored builds caused by compute throttling from Hugging Face. On a free-tier Gradio Space, schedule `*/10 * * * *` proved to be too frequent and hanging builds were observed.
11. Commit your changes and that's it! Your rebuild scheduler is ready to go!
