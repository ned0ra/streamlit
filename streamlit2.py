import streamlit as st
import pandas as pd

df1=pd.read_csv('nics-firearm-background-checks.csv')

df1['year']=df1['month'].str.split('-').str[0]
year=df1['year'].tolist()

df = df1[['totals', 'state', 'year']]

states=st.multiselect('Выберите штат',df['state'].unique())
checkbox=st.checkbox('Все штаты', value=False)

year=st.slider('Выберите год', min_value=1998, 
               max_value=2023, step=1)
checkbox2=st.checkbox('Все года', value=False)

if checkbox:
    dff = df.copy()
else:
    dff = df[df['state'].isin(states)]
if not checkbox2:
    dff = dff[dff['year'] == str(year)]

# print(dff)


st.bar_chart(data=dff, x='totals', y='state', use_container_width = True)
btn=st.button('Загрузить данные')
if btn:
    dff.to_excel('data.xlsx', index=False)

st.table(data=dff)
