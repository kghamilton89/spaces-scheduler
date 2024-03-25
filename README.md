# 🤗 Spaces Scheduler

[Hugging Face Spaces](https://huggingface.co/spaces) offer a simple way to host ML apps directly on the Hugging Face platform.

The [MPEP initiative](https://github.com/huggingface/data-is-better-together/tree/main/prompt_translation), a part of the [DIBT project](https://huggingface.co/DIBT), identifed a use case wherein it would be desireable to have performance dashboards hosted in Spaces refresh on a schedule.

Efforts to build a `BackgroundScheduler()` function in the Gradio app proved [imperfect](https://github.com/huggingface/data-is-better-together/pull/33).

Hugging Face Spaces support [`restart_space`](https://huggingface.co/docs/huggingface_hub/main/en/package_reference/hf_api#huggingface_hub.HfApi.restart_space) but by design do not support outgoing HTTP requests so building a runtime scheduler remains elusive.

This repository is a lightweight scheduler that leverages [GitHub Actions](https://docs.github.com/en/actions) to externally trigger dashboard rebuild and by extension, data update.

It may be generalized to induce refresh of arbitrary Hugging Face Spaces.
