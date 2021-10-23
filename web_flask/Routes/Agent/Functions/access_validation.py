#!/usr/bin/python3


def agent_acces_val(user_rol):
    if(user_rol == 'Usuario'):
        return 'dashboard_usuario'
    elif(user_rol == 'Administrador'):
        return 'admin'
