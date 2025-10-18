import torch
from prompt.prompt import create_chat_prompt as create_prompt



def get_device():
    return "cuda" if torch.cuda.is_available() else "cpu"

if __name__ == "__main__":



