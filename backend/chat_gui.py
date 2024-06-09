import tkinter as tk
from tkinter import scrolledtext, font
from gpt4 import ler_documento, obter_resposta

class ChatGUI:
    def __init__(self, master):
        self.master = master
        master.title("ChatBot")
        
        # Criar uma fonte em negrito
        bold_font = font.Font(weight="bold")

        small_font = font.Font(size=8)


        self.title_label = tk.Label(master, text="Bem-vindo ao ChatBot", font=bold_font)
        self.title_label.grid(row=0, column=0, columnspan=2)

        self.description_label = tk.Label(master, text="Digite SAIR para iniciar nova conversa")
        self.description_label.grid(row=1, column=0, columnspan=2) 

        self.description_label = tk.Label(master, text="https://linkedin.com/in/guilhermecavazzana\n@CavData", font=small_font)
        self.description_label.grid(row=2, column=0, columnspan=2)        

        self.chat_history = scrolledtext.ScrolledText(master, width=50, height=20, wrap=tk.WORD)
        self.chat_history.grid(row=3, column=0, columnspan=2)

        self.entry_label = tk.Label(master, text="Digite sua pergunta:")
        self.entry_label.grid(row=4, column=0)

        self.entry = tk.Entry(master, width=40)
        self.entry.grid(row=4, column=1)

        self.ask_button = tk.Button(master, text="Enviar", command=self.send_question)
        self.ask_button.grid(row=5, columnspan=2)

        self.context = ler_documento(None)  # Carregar o contexto inicial

    def send_question(self):
        question = self.entry.get()
        if question.strip() == "":
            return
        response = obter_resposta(question, self.context)
        self.update_chat_history(question, response)
        self.entry.delete(0, 'end')  # Limpar a entrada

    def update_chat_history(self, question, response):
        self.chat_history.insert(tk.END, "Você: " + question + "\n")
        self.chat_history.insert(tk.END, "ChatBot: " + response + "\n")
        self.chat_history.see(tk.END)  # Role a caixa de texto para mostrar a última mensagem

if __name__ == "__main__":
    root = tk.Tk()
    chat_gui = ChatGUI(root)
    root.mainloop()
