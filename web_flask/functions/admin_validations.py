#!/usr/bin/python3
from flask import Flask, render_template, redirect, url_for
from ..models.Class import *
from ..app import *
from flask_wtf import FlaskForm

def Admin_validations():
    ticket = TicketForm()
    if ticket.validate_on_submit():
        New_Ticket = Tickets(User_ID=current_user.id, Subject=ticket.subject.data, Problem_Type=ticket.problemType.data, Company_Area=ticket.company_area.data, Description=ticket.description.data)
        db.session.add(New_Ticket)
        db.session.commit()
        summary = User_Tickets_Summary.query.filter_by(User_id=current_user.id).first()
        all_summary = Tickets_Summary.query.first()
        if (all_summary == None):
            obj = Tickets_Summary(All_tickets=0, Pendings=0, Solved=0, Assigned=0)
            db.session.add(obj)
            db.session.commit()


        if (summary == None):
            User_Summary =  User_Tickets_Summary(All_tickets=1, Pendings=1, Assigned=0, Solved=0, User_id=current_user.id)
            db.session.add(User_Summary)

            """ updating all summary """
            all_summary.All_tickets += 1
            all_summary.Pendings += 1
            all_summary.UpdateTime = datetime.now()

            db.session.commit()
        else:
            """ updating user summary table """
            summary.All_tickets +=  1
            summary.Pendings +=  1
            summary.UpdateTime = datetime.now()
            """ updating all summary table """
            all_summary.All_tickets += 1
            all_summary.Pendings += 1
            all_summary.UpdateTime = datetime.now()
            db.session.commit()

    return render_template('dashboard.html', ticket=ticket, name=current_user.Nombre, id=current_user.id)
