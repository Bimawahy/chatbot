import nltk
from nltk.chat.util import Chat, reflections

# Define the chat patterns
pola_chat = [
    ["(hai|halo|Hai|Halo)", ["halo", "hi", "ada yang bisa saya bantu ?."]],
    ["(baaimana kabarmu)", ["saya adalah chatbot,saya tidak punya kabar ,tapi terimakasih sudah bertanya "]],
    ["(berapa umurmu)", ["saya tidak memiliki umur, tapi system saya berjalan pertamakali pada tanggal 5 november 2024,jadi bisa disimpulkan saya lahir pada tanggal 5 november dan umur saya baru 3 hari"]],
    ["(keluar|selesai)", ["sampai jumpa semoga hari mu menyenangkan"]],
]

# Function to start the chat
def run_chat():  
    print("halo! saya adalah chatbot: silahkan bertanya")
    chatbot = Chat(pola_chat, reflections)
    chatbot.converse()

if __name__ == "__main__":
    run_chat()
