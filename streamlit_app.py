# Libera Dados @pmrtys 2021

#print('Olá, essa é a contrução!')

"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

print('Olá, essa é a contrução!')
df = pd.DataFrame({
  'Coluna 1': [1, 2, 3, 4],
  'Coluna 2': [10, 20, 30, 40]
})

df
