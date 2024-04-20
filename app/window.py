import PySimpleGUI as sg

import main

sg.theme('DarkBlue6')

layout = [[sg.InputText(key='Texto', do_not_clear=False, expand_x=True)],

          [sg.Push(), sg.Button('Solicitar', expand_x=True), sg.Push(),
           sg.Checkbox('Criar arquivo?'), sg.Push()],

          [sg.Text(f'Arquivo atual: {main.nome_arquivo()}', key='arquivo')],

          [sg.Text('', key='arq')],

          [sg.Button('Mostrar dados atuais no arquivo', key='mostrar')],

          [sg.Push(), sg.Text('', key='analise'), sg.Push()],

          [sg.Text('Digite o índicie a ser removido:'),
           sg.Input('', key='indicie', do_not_clear=False, size=20, expand_x=True),
           sg.Button('Remover', key='remove', size=10),
           sg.Button('Reescrever', key='reescrever', size=10)],

          [sg.Text('', key='apagado', expand_x=True)]
          ]

window = sg.Window('Salvando informações', layout, margins=(50, 50), resizable=True, font=('Miriam Libre', 12),
                   titlebar_font=('Miriam Libre', 10), element_justification='Center',
                   use_ttk_buttons=True, auto_size_buttons=True, auto_size_text=True,
                   )

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Solicitar':
        if values[0]:
            main.criar_arq(values['Texto'])
            main.guardar_arquivo(values['Texto'])
            window['arquivo'].update(f'Arquivo atual:{main.nome_arquivo()}')
            window['arq'].update(f'Arquivo {values['Texto']} foi criado com êxito!!!')
        else:
            try:
                main.escrever(values['Texto'])
                window['arq'].update(f'As palavras {values['Texto']} foram escritas com êxito.')
            except:
                window['arq'].update('Arquivo não encontrado ou não criado. Por favor crie um arquivo novo.')
    if event == 'mostrar':
        window['analise'].update(main.mostrar_arq())
    if event == 'remove':
        try:
            indice = int(values['indicie'])
            apagado = main.apagar(indice)
            window['apagado'].update(f'Palavra(as) apagadas: {apagado}')
        except:
            window['analise'].update(main.mostrar_arq())
            num_indicie = values['indicie']
            num_indicie = ''.join(num_indicie)
            if len(num_indicie) > 0:
                window['apagado'].update('O índicie descrito não existe.')
        window['analise'].update(main.mostrar_arq())
    if event == 'reescrever':
        retornada = main.guardar_apagado(reescrever=True)
        window['analise'].update(main.mostrar_arq())
        window['apagado'].update(f'A(s) palavra(s) "{retornada}" foi reescrito no arquivo atual.')

window.close()
