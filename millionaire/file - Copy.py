import os
import webbrowser
import urllib

def form():
    filename = 'file:///'+os.getcwd()+'/' + 'login.html'
    webbrowser.open_new_tab(filename)

def call():

    webbrowser.open('https://ievaphone.com/')
