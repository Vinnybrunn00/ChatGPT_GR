import customtkinter as ctk
from tkinter import PhotoImage

window = ctk.CTk()
window.geometry('900x500')
window.title('ChatGPT')
window .resizable(False, False)

img = PhotoImage(file='img/logo3.png')
lb_img = ctk.CTkLabel(window, text=None, image=img)
lb_img.pack(padx=10, pady=10)

def verificar():
    if len(token.get()) != 51:
        error = ctk.CTkLabel(window, width=100, height=100, text='Erro Token', text_color='#DC143C')
        error.pack(padx=10, pady=10)

    elif not 'admin' in senha.get():
        error = ctk.CTkLabel(window,width=200, height=100, text='Incorrect Password', text_color='#DC143C')
        error.pack(padx=10, pady=10)
    
    else:
        ok = ctk.CTkLabel(window, text='Login Sucess!!!', text_color='#00FF00')
        ok.pack(padx=10, pady=10)
        import main
        main()

texto = ctk.CTkLabel(window, text='ChatGPT')
texto.pack(padx=10, pady=10)

token = ctk.CTkEntry(window, width=350, height=40, placeholder_text='Token')
token.pack(padx=10, pady=10)

senha = ctk.CTkEntry(window, width=350, height=40, placeholder_text='Password', show='*')
senha.pack(padx=10, pady=10)

botao = ctk.CTkButton(window, text='Acess', hover_color='#33665B', fg_color='#58B19D', command=verificar)
botao.pack(padx=10, pady=10)

window.mainloop()