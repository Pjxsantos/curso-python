#!/usr/bin/env python

# config.py
name_dict = {}  # Variável global

# file1.py
from config import name_dict

def load_data():
    # Carrega dados em name_dict
    pass

# file2.py
from config import name_dict

def process_data():
    # Usa e atualiza name_dict
    pass
