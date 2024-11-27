from pozdnyakov.chatbot import PozdnyakovChatBot

model = PozdnyakovChatBot(
    checkpoint=3695,
    max_seq=128,
    save_history=True
)

while True:
    prompt = input("User prompt:\n")
    print(model(prompt))
