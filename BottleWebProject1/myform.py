from genericpath import exists
from tkinter import CURRENT
from turtle import pd
from bottle import datetime, post, request, run, route, template, static_file
import re
import pdb
import os
import json 
import pandas as pd

# Создаем пустой словарь для хранения данных
data_dict = {}

@post('/home', method='post')
def my_from():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
    
    emailpattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z0-9-.]+$"
    namepattern = r"^[a-zA-Z]$"
     
  
    mail = request.forms.get('ADRESS')
    name = request.forms.get('USERNAME')
    quest = request.forms.get('QUESTS')
    
    
    if mail and name and quest:
        if not len(quest) < 10 and re.search(r'[a-zA-Z0-9]', quest):
            if not re.match(namepattern, name) and len(name) < 2:
                return "Name field has an incorrect value or an invalid length "
            else:
                if re.match(emailpattern, mail):
                 data_dict[mail] = [name, quest]
                 print("Final data_dict contents:")
                 for email, info in data_dict.items():
                     print(f"Email: {email}, Username: {info[0]}, Question: {info[1]}")
                 return f"Thank you for contacting us {name} <br> Access date: {current_date}"
                else:
                    return "You have entered an invalid email address"
        else:
             return "The length of the request is too short(<10 symb) or the request was made incorrectly"
    else:
        return "One or more fields are not filled in"
    

@route('/home', method='POST')
def save_form_data():
    company_name = request.forms.get('Company_Name')
    description = request.forms.get('Description')
    contacts = request.forms.get('Contacts')
    start_date = request.forms.get('Date_Start')
    ceo_name = request.forms.get('CEO_Name')

    file_path = r'D:\lab5-6-e13dce5b571056c041103ab023a0b9f347d98bb7\BottleWebProject1\views\partners_data.txt'

    with open(file_path, 'a') as file:
        file.write(f"Company Name: {company_name}\n")
        file.write(f"Description: {description}\n")
        file.write(f"Contacts: {contacts}\n")
        file.write(f"Start Date: {start_date}\n")
        file.write(f"CEO Name: {ceo_name}\n\n")
    return 'Data saved'

 
from bottle import route, template


    
  


    
    


    


    
