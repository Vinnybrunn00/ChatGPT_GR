import customtkinter as ctk
import openai

openai.api_key = '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'

def func():
    message = []
    user = input.get()
    message.append({'role':'user','content': user})
    output = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=message)
    reply = output.choices[0].message.content

    label = ctk.CTkLabel(frame, text=reply)
    label.pack()

app = ctk.CTk()
app.geometry('1000x620')
app.title('ChatGPT')
app.resizable(False, False)

tela_main = ctk.CTkLabel(app, text='ChatGPT')
tela_main.pack()

frame = ctk.CTkScrollableFrame(app, width=950, height=500)
frame.pack()

input = ctk.CTkEntry(app, placeholder_text='># ', width=950)
input.pack(pady=10)

button = ctk.CTkButton(app, text='Enviar', hover_color='#33665B', fg_color='#58B19D', command=func)
button.pack()

app.mainloop()