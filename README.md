# Pozdnyakov-Vlad-AI
AI trained on a [Pozdnyakov channel](https://t.me/+k_Z9AGYLs7g5ZGUy)

![Поздняков](https://static10.tgstat.ru/channels/_0/5f/5fbf3b1303c96932a625815726535754.jpg)

# User guide
Install latest PyTorch with CUDA
```bash
pip3 install --upgrade torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```
Download from PyPi:
```bash
pip install pozdnyakov
```
Downloading repo via git clone:
```bash
git clone https://github.com/sodeeplearning/Pozdnyakov-Vlad-AI
cd Pozdnyakov-Vlad-AI
pip install -r requirements.txt
```
Starting chatbot:
```python
from pozdnyakov.chatbot import PozdnyakovChatBot

model = PozdnyakovChatBot() # Wait for model's weights downloading
print(model("Привет!")) # Output: "Привет!"
```

## For contributors 💘
1) Create fork from ```main``` branch
2) Make your changes
3) Create pull request from your fork to ```dev``` branch with description of implemented changes
4) Wait for approving
5) **You're officially part of the project!**

# Team info
[Vitally Petreev](https://github.com/sodeeplearning) - Head of the project

⚠⚠⚠
The project team is not responsible for the model's responses. The model was trained on the open-source texts.