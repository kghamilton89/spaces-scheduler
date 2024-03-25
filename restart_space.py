from huggingface_hub import HfApi

def restart_space():
    token = "HF_TOKEN"
    repo_id = "SPACE_ID"  # Example: "username/space-name"

    try:
        HfApi().restart_space(repo_id=repo_id, token=token)
        print(f"Successfully restarted Space: {repo_id}")
    except Exception as e:
        print(f"Failed to restart Space {repo_id}: {e}")

if __name__ == "__main__":
    restart_space()
