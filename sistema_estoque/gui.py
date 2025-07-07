import tkinter
import customtkinter
import Application as ctrl

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("720x470")
root_tk.title("CustomTkinter Test")
root_tk.title("CADASTRO DE PRODUTOS")

main_frame_empty = customtkinter.CTkFrame(
        master=root_tk,
        width=500,
        height=320,
        corner_radius=10
    )
main_frame_empty.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)

menu_frame = customtkinter.CTkFrame(
    master=root_tk,
    width=200,
    height=320,
    )
menu_frame.place(relx=0.11, rely=0.5, anchor=tkinter.CENTER)

def button_function_cadastrar():
    main_frame = customtkinter.CTkFrame(
        master=root_tk,
        width=500,
        height=320,
        corner_radius=10
    )
    main_frame.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)

    label_codigo = customtkinter.CTkLabel(master=main_frame,
                               text="CÓDIGO:",
                               width=120,
                               height=25,
                               corner_radius=8)
    label_codigo.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)

    entry_codigo = customtkinter.CTkEntry(master=main_frame,
                               width=120,
                               height=25,
                               corner_radius=10)
    entry_codigo.place(relx=0.33, rely=0.2, anchor=tkinter.CENTER)

    label_nome = customtkinter.CTkLabel(master=main_frame,
                               text="NOME:",
                               width=120,
                               height=25,
                               corner_radius=8)
    label_nome.place(relx=0.1, rely=0.3, anchor=tkinter.CENTER)

    entry_nome = customtkinter.CTkEntry(master=main_frame,
                                width=120,
                                height=25,
                                corner_radius=10)
    entry_nome.place(relx=0.33, rely=0.3, anchor=tkinter.CENTER)

    label_preco = customtkinter.CTkLabel(master=main_frame,
                               text="PREÇO:",
                               width=120,
                               height=25,
                               corner_radius=8)
    label_preco.place(relx=0.1, rely=0.4, anchor=tkinter.CENTER)

    entry_preco = customtkinter.CTkEntry(master=main_frame,
                                width=120,
                                height=25,
                                corner_radius=10)
    entry_preco.place(relx=0.33, rely=0.4, anchor=tkinter.CENTER)

    label_qntd = customtkinter.CTkLabel(master=main_frame,
                               text="QUANTIDADE:",
                               width=120,
                               height=25,
                               corner_radius=8)
    label_qntd.place(relx=0.1, rely=0.5, anchor=tkinter.CENTER)

    entry_qntd = customtkinter.CTkEntry(master=main_frame,
                                width=120,
                                height=25,
                                corner_radius=10)
    entry_qntd.place(relx=0.33, rely=0.5, anchor=tkinter.CENTER)

    # 
    def cadastrar():
        text_codigo = entry_codigo.get()

        show_board = customtkinter.CTkFrame(
            master=main_frame,
            width=250,
            height=550,
            corner_radius=10,
            fg_color="#ffffff"
        )
        show_board.place(relx=0.73, rely=0.5, anchor=tkinter.CENTER)

        text_codigo = entry_codigo.get()
        text_nome = entry_nome.get()
        text_preco = entry_preco.get()
        text_qntd = entry_qntd.get()

        resp = ctrl.func_cadastrar_produto(text_codigo,text_nome,text_preco,text_qntd)

        if resp == None:
            label_resp_erro = customtkinter.CTkLabel(
                master=show_board,
                text="O Código é maior que 6 dígitos.",
                width=490,
                height=25,
                corner_radius=8,
                text_color= "#ff0000"
            )
            label_resp_erro.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        elif resp == False:
            label_resp_erro = customtkinter.CTkLabel(
                master=show_board,
                text="Preencha os campos\ncorretamente.",
                width=490,
                height=50,
                corner_radius=8,
                text_color= "#ff0000"
            )
            label_resp_erro.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        elif resp:
            label_resp_erro = customtkinter.CTkLabel(
                master=show_board,
                text=resp,
                width=490,
                height=300,
                corner_radius=8,
                text_color= "#00ff00"
            )
            label_resp_erro.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


        entry_codigo.delete(0, tkinter.END)
        entry_nome.delete(0, tkinter.END)
        entry_preco.delete(0, tkinter.END)
        entry_qntd.delete(0, tkinter.END)

    enviar_cadastro = customtkinter.CTkButton(
        master=main_frame,
        text="Enviar",
        fg_color="#7a8bda",
        hover_color="#ffffff",
        command=cadastrar                                      
                                              )

    enviar_cadastro.place(relx=0.2, rely=0.65, anchor=tkinter.CENTER)

def button_function_mostrar():
    main_frame = customtkinter.CTkFrame(
        master=root_tk,
        width=500,
        height=320,
        corner_radius=10
    )
    main_frame.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)

    label_codigo = customtkinter.CTkLabel(master=main_frame,
                               text="CÓDIGO:",
                               width=120,
                               height=25,
                               corner_radius=8)
    label_codigo.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)

    entry_codigo = customtkinter.CTkEntry(master=main_frame,
                               width=120,
                               height=25,
                               corner_radius=10)
    entry_codigo.place(relx=0.33, rely=0.2, anchor=tkinter.CENTER)

    def mostrar():
        text_codigo = entry_codigo.get()

        show_board = customtkinter.CTkFrame(
            master=main_frame,
            width=500,
            height=150,
            corner_radius=10,
            fg_color="#ffffff"
        )
        show_board.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        resp = ctrl.func_mostrar_produto(text_codigo)
        
        if len(text_codigo) > 6:
            label_resp_erro = customtkinter.CTkLabel(
                master=show_board,
                text="O Código é maior que 6 dígitos.",
                width=490,
                height=25,
                corner_radius=8,
                text_color= "#ff0000"
            )
            label_resp_erro.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            return

        if resp != None:
            label_resp_codigo = customtkinter.CTkLabel(
                master=show_board,
                text="CÓDIGO: "+resp[0],
                width=490,
                height=25,
                corner_radius=8
            )
            label_resp_codigo.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

            label_resp_nome = customtkinter.CTkLabel(
                master=show_board,
                text="NOME: "+resp[1],
                width=490,
                height=25,
                corner_radius=8
            )
            label_resp_nome.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

            label_resp_preco = customtkinter.CTkLabel(
                master=show_board,
                text="PRECO: "+str(resp[2]),
                width=490,
                height=25,
                corner_radius=8
            )
            label_resp_preco.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

            label_resp_qntd = customtkinter.CTkLabel(
                master=show_board,
                text="QNTD: "+str(resp[3]),
                width=490,
                height=25,
                corner_radius=8
            )
            label_resp_qntd.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

            label_resp_cat = customtkinter.CTkLabel(
                master=show_board,
                text="CAT: "+str(resp[4]),
                width=490,
                height=25,
                corner_radius=8
            )
            label_resp_cat.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)
        else:
            label_resp_none = customtkinter.CTkLabel(
                master=show_board,
                text="Código Não Cadastrado.",
                width=490,
                height=25,
                corner_radius=8,
                text_color= "#ff0000"
            )
            label_resp_none.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    enviar_mostrar = customtkinter.CTkButton(master=main_frame,
        text="Enviar",
        fg_color="#7a8bda",
        hover_color="#ffffff",
        command=mostrar
        )
    enviar_mostrar.place(relx=0.2, rely=0.4, anchor=tkinter.CENTER)

def button_function_entradas_saidas():
    main_frame = customtkinter.CTkFrame(
        master=root_tk,
        width=500,
        height=320,
        corner_radius=10
    )
    main_frame.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)

    label_codigo = customtkinter.CTkLabel(
        master=main_frame,
        text="CÓDIGO:",
        width=120,
        height=25,
        corner_radius=8
    )
    label_codigo.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)

    entry_codigo = customtkinter.CTkEntry(
        master=main_frame,
        width=120,
        height=25,
        corner_radius=10
    )
    entry_codigo.place(relx=0.33, rely=0.2, anchor=tkinter.CENTER)

    label_qntd = customtkinter.CTkLabel(
        master=main_frame,
        text="QNTD:",
        width=120,
        height=25,
        corner_radius=8
    )
    label_qntd.place(relx=0.6, rely=0.2, anchor=tkinter.CENTER)

    entry_qntd = customtkinter.CTkEntry(
        master=main_frame,
        width=120,
        height=25,
        corner_radius=10
    )
    entry_qntd.place(relx=0.8, rely=0.2, anchor=tkinter.CENTER)

    # Variável de controle para radio buttons
    selected_option = customtkinter.StringVar(value="opcao1")

    def entradas_saidas():
        text_codigo = entry_codigo.get()
        text_qntd = entry_qntd.get()
        opcao = int(selected_option.get())

        show_board = customtkinter.CTkFrame(
            master=main_frame,
            width=500,
            height=150,
            corner_radius=10,
            fg_color="#ffffff"
        )
        show_board.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        # Exemplo: chamada ao controller (ajuste para seu código real)
        resp = None
        try:
            resp = ctrl.func_entradas_saidas(text_codigo, opcao, quantidade=text_qntd)
        except Exception as e:
            print(f"Erro ao chamar controller: {e}")

        if len(text_codigo) > 6:
            label_resp_erro = customtkinter.CTkLabel(
                master=show_board,
                text="O Código é maior que 6 dígitos.",
                width=490,
                height=25,
                corner_radius=8,
                text_color="#ff0000"
            )
            label_resp_erro.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            return

        if resp is not None:
            label_resp_codigo = customtkinter.CTkLabel(
                master=show_board,
                text=resp,
                width=490,
                height=400,
                corner_radius=8
            )
            label_resp_codigo.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        else:
            label_resp_none = customtkinter.CTkLabel(
                master=show_board,
                text="Código Não Cadastrado.",
                width=490,
                height=25,
                corner_radius=8,
                text_color="#ff0000"
            )
            label_resp_none.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    radio1 = customtkinter.CTkRadioButton(
        master=main_frame,
        text="Entrada",
        variable=selected_option,
        value=0
    )
    radio1.place(relx=0.2, rely=0.35, anchor=tkinter.CENTER)

    radio2 = customtkinter.CTkRadioButton(
        master=main_frame,
        text="Saída",
        variable=selected_option,
        value=1
    )
    radio2.place(relx=0.4, rely=0.35, anchor=tkinter.CENTER)

    enviar_entradas_saidas = customtkinter.CTkButton(
        master=main_frame,
        text="Enviar",
        fg_color="#7a8bda",
        hover_color="#ffffff",
        command=entradas_saidas
    )
    enviar_entradas_saidas.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)

def button_function_editar():
    main_frame = customtkinter.CTkFrame(
        master=root_tk,
        width=500,
        height=320,
        corner_radius=10
    )
    main_frame.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)

    # EDIT 
    label_codigo = customtkinter.CTkLabel(master=main_frame,
                               text="CÓDIGO:",
                               width=120,
                               height=25,
                               corner_radius=8)
    label_codigo.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)

    entry_codigo = customtkinter.CTkEntry(master=main_frame,
                               width=120,
                               height=25,
                               corner_radius=10)
    entry_codigo.place(relx=0.33, rely=0.2, anchor=tkinter.CENTER)

    # EDIT - CHANGE

    # CODIGO
    label_codigo_edit = customtkinter.CTkLabel(master=main_frame,
                               text="CÓDIGO:",
                               width=120,
                               height=25,
                               corner_radius=8)
    label_codigo_edit.place(relx=0.6, rely=0.2, anchor=tkinter.CENTER)

    entry_codigo_edit = customtkinter.CTkEntry(master=main_frame,
                               width=120,
                               height=25,
                               corner_radius=10)
    entry_codigo_edit.place(relx=0.83, rely=0.2, anchor=tkinter.CENTER)

    # NOME

    label_nome_edit = customtkinter.CTkLabel(master=main_frame,
                               text="NOME:",
                               width=120,
                               height=25,
                               corner_radius=8)
    label_nome_edit.place(relx=0.6, rely=0.3, anchor=tkinter.CENTER)

    entry_nome_edit = customtkinter.CTkEntry(master=main_frame,
                                width=120,
                                height=25,
                                corner_radius=10)
    entry_nome_edit.place(relx=0.83, rely=0.3, anchor=tkinter.CENTER)

    # PRECO

    label_preco_edit = customtkinter.CTkLabel(master=main_frame,
                               text="PREÇO:",
                               width=120,
                               height=25,
                               corner_radius=8)
    label_preco_edit.place(relx=0.6, rely=0.4, anchor=tkinter.CENTER)

    entry_preco_edit = customtkinter.CTkEntry(master=main_frame,
                                width=120,
                                height=25,
                                corner_radius=10)
    entry_preco_edit.place(relx=0.83, rely=0.4, anchor=tkinter.CENTER)

    # QNTD

    """label_qntd_edit = customtkinter.CTkLabel(master=main_frame,
                               text="QUANTIDADE:",
                               width=120,
                               height=25,
                               corner_radius=8)
    label_qntd_edit.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)

    entry_qntd_edit = customtkinter.CTkEntry(master=main_frame,
                                width=120,
                                height=25,
                                corner_radius=10)
    entry_qntd_edit.place(relx=0.83, rely=0.5, anchor=tkinter.CENTER)"""

    
    def editar():
        text_codigo = entry_codigo.get()
        
        show_board = customtkinter.CTkFrame(
            master=main_frame,
            width=350,
            height=120,
            corner_radius=10,
            fg_color="#ffffff"
        )
        show_board.place(relx=0.7, rely=0.8, anchor=tkinter.CENTER)

        text_codigo = entry_codigo.get()

        text_codigo_edit = entry_codigo_edit.get()
        text_nome_edit = entry_nome_edit.get()
        text_preco_edit = entry_preco_edit.get()
        #text_qntd_edit = entry_qntd_edit.get()

        resp = ctrl.func_alterar_produto(text_codigo,text_codigo_edit,text_nome_edit,text_preco_edit)

        if resp == None:
            label_resp_erro = customtkinter.CTkLabel(
                master=show_board,
                text="O Código é maior que 6 dígitos.",
                width=490,
                height=25,
                corner_radius=8,
                text_color= "#ff0000"
            )
            label_resp_erro.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        elif resp == False:
            label_resp_erro = customtkinter.CTkLabel(
                master=show_board,
                text="Preencha os campos\ncorretamente.",
                width=490,
                height=50,
                corner_radius=8,
                text_color= "#ff0000"
            )
            label_resp_erro.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        elif resp:
            label_resp_erro = customtkinter.CTkLabel(
                master=show_board,
                text=resp,
                width=490,
                height=300,
                corner_radius=8,
                text_color= "#000000"
            )
            label_resp_erro.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


        entry_codigo.delete(0, tkinter.END)
        entry_codigo_edit.delete(0, tkinter.END)
        entry_nome_edit.delete(0, tkinter.END)
        entry_preco_edit.delete(0, tkinter.END)
        #entry_qntd_edit.delete(0, tkinter.END)

    enviar_cadastro = customtkinter.CTkButton(
        master=main_frame,
        text="Enviar",
        fg_color="#7a8bda",
        hover_color="#ffffff",
        command=editar                                      
                                              )

    enviar_cadastro.place(relx=0.2, rely=0.65, anchor=tkinter.CENTER)

def button_function_deletar():
    main_frame = customtkinter.CTkFrame(
        master=root_tk,
        width=500,
        height=320,
        corner_radius=10
    )
    main_frame.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)

    label_codigo = customtkinter.CTkLabel(master=main_frame,
                               text="CÓDIGO:",
                               width=120,
                               height=25,
                               corner_radius=8)
    label_codigo.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)

    entry_codigo = customtkinter.CTkEntry(master=main_frame,
                               width=120,
                               height=25,
                               corner_radius=10)
    entry_codigo.place(relx=0.33, rely=0.2, anchor=tkinter.CENTER)

    selected_option = customtkinter.StringVar(value="option1")

    def deletar():
        text_codigo = entry_codigo.get()
        confirmacao = int(selected_option.get())

        show_board = customtkinter.CTkFrame(
            master=main_frame,
            width=500,
            height=150,
            corner_radius=10,
            fg_color="#ffffff"
        )
        show_board.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        resp = ctrl.func_deletar_produto(text_codigo, confirmacao)
        
        if len(text_codigo) > 6:
            label_resp_erro = customtkinter.CTkLabel(
                master=show_board,
                text="O Código é maior que 6 dígitos.",
                width=490,
                height=25,
                corner_radius=8,
                text_color= "#ff0000"
            )
            label_resp_erro.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            return

        if resp != None:
            label_resp_codigo = customtkinter.CTkLabel(
                master=show_board,
                text=resp,
                width=490,
                height=25,
                corner_radius=8
            )
            label_resp_codigo.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        else:
            label_resp_none = customtkinter.CTkLabel(
                master=show_board,
                text="Código Não Cadastrado.",
                width=490,
                height=25,
                corner_radius=8,
                text_color= "#ff0000"
            )
            label_resp_none.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    radio_buttom = customtkinter.CTkRadioButton(
        master=main_frame,
        text="Confirme para deletar o produto.",
        variable=selected_option,
        value=1
    )
    
    radio_buttom.place(relx=0.25, rely=0.3, anchor=tkinter.CENTER)

    deletar = customtkinter.CTkButton(
        master=main_frame,
        text="Enviar",
        fg_color="#7a8bda",
        hover_color="#ffffff",
        command=deletar
        )
    deletar.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)

def button_function_importar():
    main_frame = customtkinter.CTkFrame(
        master=root_tk,
        width=500,
        height=320,
        corner_radius=10
    )
    main_frame.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)

    def importar():
        resp = ctrl.func_importar_arquivo()

        show_board = customtkinter.CTkFrame(
            master=main_frame,
            width=500,
            height=150,
            corner_radius=10,
            fg_color="#ffffff"
        )
        show_board.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        label_resp_codigo = customtkinter.CTkLabel(
                master=show_board,
                text=resp,
                width=490,
                height=400,
                corner_radius=8
            )
        label_resp_codigo.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    enviar_entradas_saidas = customtkinter.CTkButton(
        master=main_frame,
        text="Importar",
        fg_color="#7a8bda",
        hover_color="#ffffff",
        command=importar
    )
    enviar_entradas_saidas.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
# Layout menu_frame
button_cadastro = customtkinter.CTkButton(
    master=menu_frame,
    corner_radius=10,
    command=button_function_cadastrar,
    text="Cadastrar Produto",
    width=200,
    border_color="#000000",
    fg_color="#7a8bda",
    hover_color="#ffffff"
    )

button_mostrar = customtkinter.CTkButton(
    master=menu_frame,
    corner_radius=10,
    command=button_function_mostrar,
    text="Mostrar Produto",
    width=200,
    border_color="#000000",
    fg_color="#7a8bda",
    hover_color="#ffffff"
    )

button_entradas_saidas = customtkinter.CTkButton(
    master=menu_frame,
    corner_radius=10,
    command=button_function_entradas_saidas,
    text="Entradas e Saídas",
    width=200,
    border_color="#000000",
    fg_color="#7a8bda",
    hover_color="#ffffff"
    )

button_editar = customtkinter.CTkButton(
    master=menu_frame,
    corner_radius=10,
    command=button_function_editar,
    text="Editar Produto",
    width=200,
    border_color="#000000",
    fg_color="#7a8bda",
    hover_color="#ffffff"
    )

button_deletar = customtkinter.CTkButton(
    master=menu_frame,
    corner_radius=10,
    command=button_function_deletar,
    text="Deletar Produto",
    width=200,
    border_color="#000000",
    fg_color="#7a8bda",
    hover_color="#ffffff"
    )

button_importar = customtkinter.CTkButton(
    master=menu_frame,
    corner_radius=10,
    command=button_function_importar,
    text="Importar Arquivo",
    width=200,
    border_color="#000000",
    fg_color="#7a8bda",
    hover_color="#ffffff"
    )

# Layout main_menu



# ----------------

button_cadastro.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
button_mostrar.place(relx=0.5, rely=0.23, anchor=tkinter.CENTER)
button_entradas_saidas.place(relx=0.5, rely=0.37, anchor=tkinter.CENTER)
button_editar.place(relx=0.5, rely=0.51, anchor=tkinter.CENTER)
button_deletar.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)
button_importar.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

if __name__ == '__main__':
    root_tk.mainloop()