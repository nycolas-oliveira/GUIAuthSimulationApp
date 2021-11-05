from PySimpleGUI import PySimpleGUI as sg
from comunicationServer import authentication as auth
from comunicationServer import registration as register

#Layout

def janela_login():
    sg.theme('DarkGrey6')

    layout = [
        [sg.Text('Usuário:', size = (9, 1)), sg.Input(key='usuario', size = (25, 1))],
        [sg.Text('Senha:', size = (9, 1)), sg.Input(key='senha', password_char='*', size = (25, 1))],
        #[sg.Radio('Default', "RADIO1", key = 'radio1', default=True), sg.Radio('SHA256', "RADIO1", key = 'radio2'), sg.Radio('Hash2', "RADIO1", key = 'radio3'), sg.Radio('Encrypt1', "RADIO1", key = 'radio4')],
        [sg.Button('Entrar'), sg.Button('Cadastrar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)

def janela_cadastro():
    sg.theme('DarkGrey6')
    layout = [
        [sg.Text('Usuário:', size = (18, 1)), sg.Input(key='usuario', size = (25, 1))],
        [sg.Text('Senha:', size = (18, 1)), sg.Input(key='senha1', password_char='*', size = (25, 1))],
        [sg.Text('Confirmar Senha:', size = (18, 1)), sg.Input(key='senha2', password_char='*', size = (25, 1))],
        [sg.Button('Voltar'), sg.Button('Cadastrar')]
    ]
    return sg.Window('Cadastro', layout=layout, finalize=True)


#Window
janela1, janela2 = janela_login(), None

#Events

while True: 
    
    window, event, valores = sg.read_all_windows()

    #Quando janela for fechada
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela2 and event == sg.WINDOW_CLOSED:
        break


    #Abrir janela de Cadastro
    if window == janela1 and event == 'Cadastrar':
        janela2 = janela_cadastro()
        janela1.hide()
        
        
    #Voltar para janela de Login
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()

    #Botão Entrar
    if window == janela1 and event == 'Entrar':
        method = 'SHA256'
        #AUTENTICA LOGIN UTILIZANDO HASHS/CRIPTOS DE ACORDO COM METHOD
        response = auth(valores['usuario'], valores['senha'], method)
         
        if response: 
            sg.popup_ok('Bem Vindo ao Sistema!!')
        else:   
            sg.popup_error('Usuario ou Senha incorreto(a)!!')

    #Botão Cadastrar
    if window == janela2 and event == 'Cadastrar':

        if valores['senha1'] == valores['senha2']:
            #SALVAR CADASTRO APLICANDO HASHS/CRIPTOS
            register(valores['usuario'], valores['senha1'])
            sg.popup_ok('Cadastro Efetuado!!!')
            janela2.hide()
            janela1.un_hide()

        else: 
            sg.popup_error('A senha não corresponde a confirmacao!!!')