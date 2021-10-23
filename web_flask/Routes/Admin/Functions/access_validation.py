#!/usr/bin/python3

def admins_acces_val(user_rol):

    if(user_rol == 'Usuario'):
        return 'dashboard_usuario'
    elif(user_rol == 'Agente Helpdesk'):
        return 'HelpDesk_Dashboard'
