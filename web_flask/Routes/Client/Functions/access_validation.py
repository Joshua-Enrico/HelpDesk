#!/usr/bin/python3


def client_acces_val(user_rol):
    if(user_rol == 'Agente Helpdesk'):
        return 'HelpDesk_Dashboard'
    elif(user_rol == 'Administrador'):
        return 'admin'
