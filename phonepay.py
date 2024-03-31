import streamlit as st 
import time
import pandas as pd
import numpy as np
import plotly.express as px
import requests
import json
import os
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.figure_factory as ff
import seaborn as sns
import psycopg2


#Agg_Trans

input_path="C:/Users/catch/OneDrive/Desktop/phone pay/pulse/data/aggregated/Transaction/country/india/state/"
Agg_state_list=os.listdir(input_path)

clm={'State':[], 'Year':[],'Quater':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

for state in Agg_state_list:
    ip=input_path+state+"/"
    Agg_yr=os.listdir(ip)
    for j in Agg_yr:
        p_j=ip+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              clm['Transaction_type'].append(Name)
              clm['Transaction_count'].append(count)
              clm['Transaction_amount'].append(amount)
              clm['State'].append(state)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))
Agg_Trans=pd.DataFrame(clm)
Agg_Trans.sort_values(by='State', inplace=True)
Agg_Trans['State']=Agg_Trans['State'].str.title()
Agg_Trans['State']=Agg_Trans['State'].str.replace("&",'and')
Agg_Trans['State']=Agg_Trans['State'].str.replace("-",' ')
Agg_Trans['State']=Agg_Trans['State'].str.replace("Andaman and Nicobar Islands",'Andaman & Nicobar')
Agg_Trans.sort_values(by=["Year","Quater"],inplace=True)
Agg_Trans.reset_index(drop=True, inplace=True)


#Agg_User


input_path2="C:/Users/catch/OneDrive/Desktop/phone pay/pulse/data/aggregated/user/country/india/state/"
Agg_User_list=os.listdir(input_path2)
clm={'State':[], 'Year':[],'Quater':[],'Brands':[], 'Transaction_count':[], 'Percentage':[]}

for state in Agg_User_list:
    ip=input_path2+state+"/"
    Agg_yr=os.listdir(ip)
    for j in Agg_yr:
        p_j=ip+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            E=json.load(Data)
            try:
              for z in E['data']['usersByDevice']:
                brand=z['brand']
                count=z['count']
                percentage=z['percentage']
                clm['Brands'].append(brand)
                clm['Transaction_count'].append(count)
                clm['Percentage'].append(percentage)
                clm['State'].append(state)
                clm['Year'].append(j)
                clm['Quater'].append(int(k.strip('.json')))
            except:
              pass


Agg_User=pd.DataFrame(clm)
Agg_User.sort_values(by='State', inplace=True)
Agg_User['State']=Agg_User['State'].str.title()
Agg_User['State']=Agg_User['State'].str.replace("&",'and')
Agg_User['State']=Agg_User['State'].str.replace("-",' ')
Agg_User['State']=Agg_User['State'].str.replace("Andaman and Nicobar Islands",'Andaman & Nicobar')
Agg_User.sort_values(by=["Year","Quater"],inplace=True)
Agg_User.reset_index(drop=True, inplace=True)


#map_Trans

input_path3="C:/Users/catch/OneDrive/Desktop/phone pay/pulse/data/map/Transaction/hover/country/india/state/"
Trans_list=os.listdir(input_path3)
clm={'State':[], 'Year':[],'Quater':[],'Districts':[], 'Transaction_count':[], 'Amount':[]}

for state in Trans_list:
    ip=input_path3+state+"/"
    Agg_yr=os.listdir(ip)
    for j in Agg_yr:
        p_j=ip+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            F=json.load(Data)
            for z in F['data']['hoverDataList']:
              name=z['name']
              count=z['metric'][0]['count']
              amount=z['metric'][0]['amount']
              clm['Districts'].append(name)
              clm['Transaction_count'].append(count)
              clm['Amount'].append(amount)
              clm['State'].append(state)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))
Map_Trans=pd.DataFrame(clm)
Map_Trans.sort_values(by='State', inplace=True)
Map_Trans['Districts']=Map_Trans['Districts'].str.title()
Map_Trans['Districts']=Map_Trans['Districts'].str.replace("District",'')
Map_Trans['State']=Map_Trans['State'].str.title()
Map_Trans['State']=Map_Trans['State'].str.replace("&",'and')
Map_Trans['State']=Map_Trans['State'].str.replace("-",' ')
Map_Trans['State']=Map_Trans['State'].str.replace("Andaman and Nicobar Islands",'Andaman & Nicobar')
Map_Trans.sort_values(by=["Year","Quater"],inplace=True)
Map_Trans.reset_index(drop=True, inplace=True)


#map_user

input_path4="C:/Users/catch/OneDrive/Desktop/phone pay/pulse/data/map/user/hover/country/india/state/"
Trans_list=os.listdir(input_path4)
clm={'State':[], 'Year':[],'Quater':[],'Districts':[], 'RegisteredUser':[], 'Appopens':[]}

for state in Trans_list:
    ip=input_path4+state+"/"
    Agg_yr=os.listdir(ip)
    for j in Agg_yr:
        p_j=ip+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            E=json.load(Data)
            for z in E['data']['hoverData'].items():
              Districts=z[0]
              RegUsers=z[1]['registeredUsers']
              Appopen=z[1]['appOpens']
              clm['Districts'].append(Districts)
              clm['RegisteredUser'].append(RegUsers)
              clm['Appopens'].append(Appopen)
              clm['State'].append(state)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))
Map_User=pd.DataFrame(clm)
Map_User.sort_values(by='State', inplace=True)
Map_User['Districts']=Map_User['Districts'].str.title()
Map_User['Districts']=Map_User['Districts'].str.replace("District",'')
Map_User['State']=Map_User['State'].str.title()
Map_User['State']=Map_User['State'].str.replace("&",'and')
Map_User['State']=Map_User['State'].str.replace("-",' ')
Map_User['State']=Map_User['State'].str.replace("Andaman and Nicobar Islands",'Andaman & Nicobar')
Map_User.sort_values(by=["Year","Quater"],inplace=True)
Map_User.reset_index(drop=True, inplace=True)



#Top_Trans
input_path5="C:/Users/catch/OneDrive/Desktop/phone pay/pulse/data/top/transaction/country/india/state/"
Top_User_list=os.listdir(input_path5)
clm={'State':[], 'Year':[],'Quater':[],'Pincode':[], 'Transaction_count':[], 'Transaction_amount':[]}
for state in Top_User_list:
    ip=input_path5+state+"/"
    Agg_yr=os.listdir(ip)
    for j in Agg_yr:
        p_j=ip+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            F=json.load(Data)
            for z in F['data']['pincodes']:
              entityname=z['entityName']
              count=z['metric']['count']
              amount=z['metric']['amount']
              clm['Pincode'].append(entityname)
              clm['Transaction_count'].append(count)
              clm['Transaction_amount'].append(amount)
              clm['State'].append(state)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))
Top_Trans=pd.DataFrame(clm)
Top_Trans.sort_values(by='State', inplace=True)
Top_Trans['State']=Top_Trans['State'].str.title()
Top_Trans['State']=Top_Trans['State'].str.replace("&",'and')
Top_Trans['State']=Top_Trans['State'].str.replace("-",' ')
Top_Trans['State']=Top_Trans['State'].str.replace("Andaman and Nicobar Islands",'Andaman & Nicobar')
Top_Trans.sort_values(by=["Year","Quater"],inplace=True)
Top_Trans.reset_index(drop=True, inplace=True)



#Top_User

input_path6="C:/Users/catch/OneDrive/Desktop/phone pay/pulse/data/top/user/country/india/state/"
Top_User_list=os.listdir(input_path6)
clm={'State':[], 'Year':[],'Quater':[],'Pincode':[], 'RegisteredUsers':[]}

for state in Top_User_list:
    ip=input_path6+state+"/"
    Agg_yr=os.listdir(ip)
    for j in Agg_yr:
        p_j=ip+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            G=json.load(Data)
            for z in G['data']['pincodes']:
              entityname=z['name']
              RegUsers=z['registeredUsers']
              clm['Pincode'].append(entityname)
              clm['RegisteredUsers'].append(RegUsers)
              clm['State'].append(state)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))
Top_User=pd.DataFrame(clm)
Top_User.sort_values(by='State', inplace=True)
Top_User['State']=Top_User['State'].str.title()
Top_User['State']=Top_User['State'].str.replace("&",'and')
Top_User['State']=Top_User['State'].str.replace("-",' ')
Top_User['State']=Top_User['State'].str.replace("Andaman and Nicobar Islands",'Andaman & Nicobar')
Top_User.sort_values(by=["Year","Quater"],inplace=True)
Top_User.reset_index(drop=True, inplace=True)

#postgresql

# Agg_Trans

db=psycopg2.connect(host='localhost',user='postgres',password='11001100',database='phonepay',port=5432)
access=db.cursor()
db.commit()

drop= "drop table if exists Agg_Trans"
access.execute(drop)
db.commit()
access.execute('''create table if not exists Agg_Trans(State varchar(100),
                                                    Year int,                                                    
                                                    Quater int,
                                                    Transaction_type varchar(200),
                                                    Transaction_count bigint,
                                                    Transaction_amount bigint                                                                                                                             
                                                    )''')         
db.commit()
insert_query='''insert into Agg_Trans(State,
                                    Year,
                                    Quater,
                                    Transaction_type,
                                    Transaction_count,
                                    Transaction_amount)
                                    
                                    values(%s,%s,%s,%s,%s,%s)'''                           
         
if not Agg_Trans.empty:   
    data = [tuple(row) for row in Agg_Trans.values]    
    access.executemany(insert_query, data)
    db.commit()
    print("Data inserted successfully.")
else:
    print("Agg_User DataFrame is empty.")
access.close()
db.close()


#Agg_User
db=psycopg2.connect(host='localhost',user='postgres',password='11001100',database='phonepay',port=5432)
access=db.cursor()
db.commit()

drop= "drop table if exists Agg_User"
access.execute(drop)
db.commit()
access.execute('''create table if not exists Agg_User(State varchar(100),
                                                    Year int,                                                    
                                                    Quater int,
                                                    Brands varchar(200),
                                                    Transaction_count bigint,
                                                    Percentage float                                                                                                                             
                                                    )''')         
db.commit()
insert_query='''insert into Agg_User(State,
                                    Year,
                                    Quater,
                                    Brands,
                                    Transaction_count,
                                    Percentage)
                                    
                                    values(%s,%s,%s,%s,%s,%s)'''                                    

if not Agg_User.empty:   
    data = [tuple(row) for row in Agg_User.values]    
    access.executemany(insert_query, data)
    db.commit()
    print("Data inserted successfully.")
else:
    print("Agg_User DataFrame is empty.")
access.close()
db.close()


#Map_Trans
db=psycopg2.connect(host='localhost',user='postgres',password='11001100',database='phonepay',port=5432)
access=db.cursor()
db.commit()


drop= "drop table if exists Map_Trans"
access.execute(drop)
db.commit()

access.execute('''create table if not exists Map_Trans(State varchar(100),
                                                    Year int,                                                    
                                                    Quater int,
                                                    Districts varchar(200),
                                                    Transaction_count bigint,
                                                    Transaction_amount bigint                                                                                                                             
                                                    )''')         
db.commit()


insert_query='''insert into Map_Trans(State,
                                    Year,
                                    Quater,
                                    Districts,
                                    Transaction_count,
                                    Transaction_amount)
                                    
                                    values(%s,%s,%s,%s,%s,%s)'''                                    
          

if not Map_Trans.empty:   
    data = [tuple(row) for row in Map_Trans.values]    
    access.executemany(insert_query, data)
    db.commit()
    print("Data inserted successfully.")
else:
    print("Agg_User DataFrame is empty.")


access.close()
db.close()


#Map_User
db=psycopg2.connect(host='localhost',user='postgres',password='11001100',database='phonepay',port=5432)
access=db.cursor()
db.commit()

drop= "drop table if exists Map_User"
access.execute(drop)
db.commit()

access.execute('''create table if not exists Map_User(State varchar(100),
                                                    Year int,                                                    
                                                    Quater int,
                                                    Districts varchar(200),
                                                    RegisteredUser bigint,
                                                    Appopens bigint                                                                                                                             
                                                    )''')         
db.commit()


insert_query='''insert into Map_User(State,
                                    Year,
                                    Quater,
                                    Districts,
                                    RegisteredUser,
                                    Appopens)
                                    
                                    values(%s,%s,%s,%s,%s,%s)'''                                    
          

if not Map_User.empty:   
    data = [tuple(row) for row in Map_User.values]    
    access.executemany(insert_query, data)
    db.commit()
    print("Data inserted successfully.")
else:
    print("Map_User DataFrame is empty.")


access.close()
db.close()

#Top_Trans
db=psycopg2.connect(host='localhost',user='postgres',password='11001100',database='phonepay',port=5432)
access=db.cursor()
db.commit()

drop= "drop table if exists Top_Trans"
access.execute(drop)
db.commit()

access.execute('''create table if not exists Top_Trans(State varchar(100),
                                                    Year int,                                                    
                                                    Quater int,
                                                    Pincode int,
                                                    Transaction_count bigint,
                                                    Transaction_amount bigint                                                                                                                             
                                                    )''')         
db.commit()


insert_query='''insert into Top_Trans(State,
                                    Year,
                                    Quater,
                                    Pincode,
                                    Transaction_count,
                                    Transaction_amount)
                                    
                                    values(%s,%s,%s,%s,%s,%s)'''                                    
          

if not Top_Trans.empty:   
    data = [tuple(row) for row in Top_Trans.values]    
    access.executemany(insert_query, data)
    db.commit()
    print("Data inserted successfully.")
else:
    print("Top_Trans DataFrame is empty.")


access.close()
db.close()


#Top_User
db=psycopg2.connect(host='localhost',user='postgres',password='11001100',database='phonepay',port=5432)
access=db.cursor()
db.commit()

drop= "drop table if exists Top_User"
access.execute(drop)
db.commit()

access.execute('''create table if not exists Top_User(State varchar(100),
                                                    Year int,                                                    
                                                    Quater int,
                                                    Pincode int,
                                                    RegisteredUsers bigint
                                                                                                                                                                                
                                                    )''')         
db.commit()


insert_query='''insert into Top_User(State,
                                    Year,
                                    Quater,
                                    Pincode,                                    
                                    RegisteredUsers)
                                    
                                    values(%s,%s,%s,%s,%s)'''                                    
          

if not Top_User.empty:   
    data = [tuple(row) for row in Top_User.values]    
    access.executemany(insert_query, data)
    db.commit()
    print("Data inserted successfully.")
else:
    print("Top_User DataFrame is empty.")


access.close()
db.close()

#Agg_Trans
db=psycopg2.connect(host='localhost',user='postgres',password='11001100',database='phonepay',port=5432)
access=db.cursor()
access.execute("Select * from Agg_Trans")
db.commit()
tab5=access.fetchall()
Agg_Trans=pd.DataFrame(tab5,columns=("State","Year","Quater","Transaction_type","Transaction_count","Transaction_amount"))

#Agg_User
db=psycopg2.connect(host='localhost',user='postgres',password='11001100',database='phonepay',port=5432)
access=db.cursor()
access.execute("Select * from Agg_User")
db.commit()
tab4=access.fetchall()
Agg_User=pd.DataFrame(tab4,columns=("State","Year","Quater","Brands","Transaction_count","Percentage"))

# Map_Trans
db=psycopg2.connect(host='localhost',user='postgres',password='11001100',database='phonepay',port=5432)
access=db.cursor()
access.execute("Select * from Map_Trans")
db.commit()
tab3=access.fetchall()
Map_Trans=pd.DataFrame(tab3,columns=("State","Year","Quater","Districts","Transaction_count","Transaction_amount"))


# Map_User
db=psycopg2.connect(host='localhost',user='postgres',password='11001100',database='phonepay',port=5432)
access=db.cursor()
access.execute("Select * from Map_User")
db.commit()
tab2=access.fetchall()
Map_User=pd.DataFrame(tab2,columns=("State","Year","Quater","Districts","RegisteredUsers","Appopens"))


# Top_Trans
db=psycopg2.connect(host='localhost',user='postgres',password='11001100',database='phonepay',port=5432)
access=db.cursor()
access.execute("Select * from Top_Trans")
db.commit()
tab1=access.fetchall()
Top_Trans=pd.DataFrame(tab1,columns=("State","Year","Quater","Pincode","Transaction_count","Transaction_amount"))


# Top_User
db=psycopg2.connect(host='localhost',user='postgres',password='11001100',database='phonepay',port=5432)
access=db.cursor()
access.execute("Select * from Top_User")
db.commit()
tab=access.fetchall()
Top_User=pd.DataFrame(tab,columns=("State","Year","Quater","Pincode","RegisteredUsers"))


#Transaction details year wise:
def trans(df,Year):
    data=df[df.Year==Year]
    data.reset_index(drop=True, inplace=True)
    datasum=data.groupby("State")[["Transaction_count","Transaction_amount"]].sum()
    datasum.reset_index(inplace=True)
    # col1, col2 = st.columns([])
    # with col1:        
    fig=px.bar(datasum,x="State",y="Transaction_amount",title=f"{Year} Transaction_amount",height=650,width=700,color_discrete_sequence=['#782AB6'])
    st.plotly_chart(fig, label_visibility=False)        
    # with col2:     
    fig=px.bar(datasum,x="State",y="Transaction_count",title=f"{Year} Transaction_count",height=650,width=700,color_discrete_sequence=['#85660D'])
    st.plotly_chart(fig, label_visibility=False)    
    # col1,col2=st.columns(2,gap= "large")
    # with col1:    
    df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")
    fig = px.choropleth(
    datasum,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State',
    color='Transaction_amount',
    color_continuous_scale='Rainbow',
    range_color=(datasum["Transaction_amount"].max(),datasum["Transaction_amount"].min()),
    hover_name="State",
    title=f"{Year} Transaction_amount",    
    width=800, 
    height=800    
    )
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig, label_visibility=False)        
    # with col2:   
        # fig=px.bar(datasum,x="State",y="Transaction_count",title=f"{Year} Transaction_count",pattern_shape_sequence=["+"],height=650,width=700,color_discrete_sequence=['#85660D'])
        # st.plotly_chart(fig)
      
        
    fig2 = px.choropleth(
    datasum,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State',
    color='Transaction_count',
    color_continuous_scale='Rainbow',
    range_color=(datasum["Transaction_count"].max(),datasum["Transaction_count"].min()),
    hover_name="State",
    title=f"{Year} Transaction_count",
    width=800,height=800    
    )
    fig2.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig2, label_visibility=False)    
    return datasum
    
    
    #Transaction details with quater wise
def trans_q(df,Quater):
    data=df[df.Quater==Quater]
    data.reset_index(drop=True, inplace=True)
    datasum=data.groupby("State")[["Transaction_count","Transaction_amount"]].sum()
    datasum.reset_index(inplace=True)
    col1,col2=st.columns(2)
    with col1:
        fig1=px.bar(datasum,x="State",y="Transaction_amount",title=f"{Quater} Transaction_amount",height=650,width=700,color_discrete_sequence=['#EB663B'])
        st.plotly_chart(fig1, label_visibility=False)
        df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")
        fig1 = px.choropleth(
        datasum,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Transaction_amount',
        color_continuous_scale='Rainbow',
        range_color=(datasum["Transaction_amount"].max(),datasum["Transaction_amount"].min()),
        hover_name="State",
        title=f"{Quater} Transaction Amount",
        width=600,height=600        
        )
        fig1.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig1, label_visibility=False)
    with col2:
        fig2=px.bar(datasum,x="State",y="Transaction_count",title=f"{Quater} Transaction_count",height=650,width=700,color_discrete_sequence=['#00A08B'])
        st.plotly_chart(fig2, label_visibility=False)
        fig2 = px.choropleth(
        datasum,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Transaction_count',
        color_continuous_scale='Rainbow',
        range_color=(datasum["Transaction_count"].max(),datasum["Transaction_count"].min()),
        hover_name="State",
        title=f"{Quater} Tranaction count",
        width=600,height=600        
        )
        fig2.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig2, label_visibility=False)  
    return data

    #Transaction details with state wise
def state(df,State):
    data=df[df.State==State]
    data.reset_index(drop=True, inplace=True)
    datasum=data.groupby("Transaction_type")[["Transaction_count","Transaction_amount"]].sum()
    datasum.reset_index(inplace=True)
    col1,col2=st.columns(2)
    with col1:        
        fig=px.pie(datasum,names="Transaction_type",values="Transaction_amount",title=f"{State}'s Transaction_amount",width=600,hole=0.5)
        st.plotly_chart(fig)
    with col2:
        fig1=px.pie(datasum,names="Transaction_type",values="Transaction_count",title= f"{State}'s Transaction_count",color_discrete_sequence=px.colors.sequential.Bluered_r,width=600,hole=0.5)
        st.plotly_chart(fig1)    
    return datasum
    datasum
    
#Transaction details with District wise
def maptrans(df,Year,Quater):
    tat=df[(df.Year==Year) & (df.Quater==Quater)]
    tat.reset_index(drop=True, inplace=True)
    t=tat.groupby(["State","Districts"])[["Transaction_count","Transaction_amount"]].sum().reset_index()
    col1,col2=st.columns(2)
    with col1:
        fig = px.sunburst(t, path=['State', 'Districts'], values='Transaction_count',hover_name="Districts",width=700,height=700,title=f"All Districts{Year, Quater} Transaction_count")
        st.plotly_chart(fig)
    with col2:        
        fig1 = px.sunburst(t, path=['State', 'Districts'], values='Transaction_amount',hover_name="Districts",width=700,height=700,title=f"All Districts{Year, Quater} Transaction_amount")
        st.plotly_chart(fig1)
    
    
    
def totalvalue(df,Year,Quater):
    di=df[(df.Year==Year) & (df.Quater==Quater)]
    di.reset_index(drop=True, inplace=True)
    t=di.groupby("State")[["Transaction_count","Transaction_amount"]].sum().reset_index()
    t_sum=t["Transaction_count"].sum()
    # t_sum1=t["Transaction_amount"].sum()    
    return t_sum
    st.text(t_sum)

#User details with quater wise
def user_analysis(df,Year,Quater):
    data=df[(df.Year==Year)&(df.Quater==Quater)]
    datasum=data.groupby(["State","Districts"])[["RegisteredUsers","Appopens"]].sum()
    datasum.reset_index(inplace=True)
    col1,col2=st.columns(2)
    with col1:        
        fig = px.sunburst(datasum, path=['State',"Districts"],hover_name="State", values='RegisteredUsers',title=f" {Year} Registered Users")
        # fig.update_traces(hovertemplate='<b>District:</b> %{label}<br><b>State:</b> %{parent}<br><b>Registered Users:</b> %{value}')
        st.plotly_chart(fig)
    with col2:
        fig = px.sunburst(datasum, path=['State',"Districts"],hover_name="State", values='Appopens',title=f"{Year} App opens")
        # fig.update_traces(hovertemplate='<b>District:</b> %{label}<br><b>State:</b> %{parent}<br><b>Registered Users:</b> %{value}')
        st.plotly_chart(fig)
    col1,col2=st.columns(2)
    with col1:        
        fig = px.pie(datasum, values='RegisteredUsers', names='State',title=f"{Year} Registered Users")
        fig.update_traces(textposition='inside')
        fig.update_layout(uniformtext_minsize=16, uniformtext_mode='hide')
        st.plotly_chart(fig)
    with col2:        
        fig = px.pie(datasum, values='Appopens', names='State',title=f"{Year} App opens")
        fig.update_traces(textposition='inside')
        fig.update_layout(uniformtext_minsize=16, uniformtext_mode='hide')
        st.plotly_chart(fig)
    
    #User details with year wise
def user_count(df,Year):

    data=df[df.Year==Year]
    data.reset_index(drop=True, inplace=True)
    df=data.groupby(["State","Brands"])[["Transaction_count","Percentage"]].sum()
    df.reset_index(inplace=True)
    col1,col2=st.columns(2)
    with col2:        
        fig = px.sunburst(df, path=['Brands'], values='Percentage',title=f"{Year} Brand Used")
        st.plotly_chart(fig)

    with col1:
        fig = px.pie(df, values='Transaction_count', names='State',title=f"{Year} Transaction Count")
        fig.update_traces(textposition='inside')
        fig.update_layout(uniformtext_minsize=16, uniformtext_mode='hide')
        st.plotly_chart(fig)





#streamlit part

st.set_page_config(layout="wide")
st.title(":violet[Phonepe Pulse Data Visualization and Exploration:]")



with st.sidebar:
    
    option = st.selectbox(
    "Select Page",
    ('Home', 'Explore Data', 'Data Analysing'))
    

    st.write('You selected:', option)
    
    
if option =="Home":
    
    col1,col2= st.columns(2)

    with col1:
        st.image(r"C:\Users\catch\OneDrive\Desktop\download (1).svg",width=200)
        
        st.markdown(":violet[INDIA'S  DIGITAL PAYMENT PLATFORM] ")

        st.write("****:blue[Simple, Fast & Secure]****")
        st.write(":black[One app for all things money.]")
        st.write("*Pay bills, recharge, send money, buy gold, invest and shop at your favourite stores.")
        st.write("---------------------------------------------------------------------------------------------")
        st.write("Pay whenever you like, wherever you like.")
        st.write("Choose from options like UPI, the PhonePe wallet or your Debit and Credit Card.")
        st.write("---------------------------------------------------------------------------------------------")
        st.write('''Find all your favourite apps on PhonePe Switch.
                 Book flights, order food or buy groceries. Use all your favourite apps without downloading them.''')
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    with col2:
        video_file = open(r"C:\Users\catch\OneDrive\Desktop\home-fast-secure-v3.mp4", 'rb')
        video_bytes = video_file.read()

        st.video(video_bytes)
        
        
    st.image(r"C:\Users\catch\OneDrive\Desktop\nt_insurance.png")
    st.image(r"C:\Users\catch\OneDrive\Desktop\download (1).svg")

    col3,col4= st.columns(2)
    
    with col3:
        
        st.image(r"C:\Users\catch\OneDrive\Desktop\jjjjjjjj.png")
        
        

    with col4:
        container = st.container(border=True,height=200)
        container.write()
        container.write()
        container.write()
        container.write()
        container.write()
        container.write("""Your money stays safe.
                        PhonePe protects your money with the best-in-class security systems that help minimize frauds.""")
        st.image(r"C:\Users\catch\OneDrive\Desktop\download.png")
        
        
    col5,col6=st.columns(2)
    with col5:
        st.image(r"C:\Users\catch\OneDrive\Desktop\sales-anim.png")
        
    with col6:
        st.header(":violet[For Business]")
        
        st.write("Find the digital payment solution that fits your business needs")
        st.write("")
        st.write("I want to:")
        st.write("")
        st.write("""Be on PhonePe Switch
                Get new users for your app""")
        st.write("-----------------------------------------")
        st.write("""Accept payments at stores
                Help your business go cashless""")
        st.write("-----------------------------------------")
        st.write("""Integrate PhonePe Payment Gateway
                Process online payments seamlessly""")
        st.write("-----------------------------------------")
        st.write("""Advertise on PhonePe
                Advertise & let customers know about you""")
       
    

if option =='Explore Data':

    tab1, tab2 = st.tabs(["Transactions", "Users"])


    with tab1:
        st.header("Transactions") 
        Agg_Trans.sort_values(by="Year", ascending=True, inplace=True) 
        years_at= st.selectbox("Select the Year", Agg_Trans["Year"].unique(),index=None,
        placeholder="Select the Year")    
        a=trans(Agg_Trans,years_at)
        
        
            
        # with col2:
        Agg_Trans.sort_values(by="Quater", ascending=True, inplace=True)   
        option = st.selectbox(
        "Select the quater",
        Agg_Trans["Quater"].unique(),
        index=None,
        placeholder="Select the Quater",
        )
        b=trans_q(Agg_Trans,option)

        state_Y_Q= st.selectbox("Select the State",Agg_Trans["State"].unique(),index=None,
        placeholder="Select the State")

        state_value=state(Agg_Trans,state_Y_Q)       
        map=maptrans(Map_Trans,years_at,option)


    with tab2:
        st.header("Users")
        
        Agg_User["Year"].unique().sort()
        years= st.selectbox("Select the Year", Agg_User["Year"].unique(),index=None,
            placeholder="Select the Year")
       
        
        user_value=user_count(Agg_User,years)
        # Agg_User.sort_values(by="Quater", ascending=True, inplace=True)
        quaters = st.selectbox(
            "Select the quater",
            Agg_User["Quater"].unique(),
            index=None,
            placeholder="Select the Quater",
            )
        user_map=user_analysis(Map_User,years,quaters)
  

        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()
        st.snow()





if option == 'Data Analysing': 
    
    
    db=psycopg2.connect(host='localhost',user='postgres',password='11001100',database='phonepay',port=5432)
    access=db.cursor()

    db.commit()

    Queries = st.selectbox('Select your queries',("Select Your Queries",
                                                "1) Top 10 States with most Transactions",
                                                "2) Tamil Nadu's 10 Districts with highest Transactions",
                                                "3) Tamil Nadu's 10 Districts with highest Users",
                                                "4) Top 10 States with highest userbase",
                                                "5) Top 10 postal codes of Tamil Nadu with highest userbase",
                                                "6) Average transactions of Top states ",
                                                "7) Top categories Payment methods",
                                                "8) Top 10 Districts with most Transactions",
                                                "9) Top 10 least number of Users",
                                                "10)Top 10 Districts with more number of userbase"))




    if Queries == "1) Top 10 States with most Transactions": 
        Query1='''select year,state, sum(transaction_count)as transaction_count,sum(transaction_amount)as transaction_amount from agg_trans  group by year,state order by transaction_amount desc limit 10'''
        access.execute(Query1)
        db.commit()
        t1=access.fetchall()
        data=pd.DataFrame(t1,columns=['year','States','Transaction_Count','Transaction_Amount'])
      
        
        fig = px.line(data, x='Transaction_Amount', y='Transaction_Count', title= "Highest Transactions in India",hover_data=['year'],color='States', markers=True)


        st.plotly_chart(fig)
        st.write(data)
        
    elif Queries == "2) Tamil Nadu's 10 Districts with highest Transactions": 
        Query2='''select year, Districts,sum(transaction_count) as transaction_count,sum(transaction_amount)as transaction_amount from map_trans  where state ='Tamil Nadu' group by  year,districts order by transaction_amount desc limit 10'''
        access.execute(Query2)
        db.commit()
        t1=access.fetchall()
        data=pd.DataFrame(t1,columns=['year','Districts','Transaction_Count','Transaction_Amount'])
        
        fig = px.bar(data, x="Transaction_Amount", y="Transaction_Count", color="Districts",hover_data=['year'], title="Highest Transactions in Tamil Nadu")

        st.plotly_chart(fig)
        st.write(data)
        
        
    elif Queries == "3) Tamil Nadu's 10 Districts with highest Users": 
        Query3='''select  year,Districts,sum(registereduser) as Registered_users,sum(appopens)as appopens from map_user  where state ='Tamil Nadu' group by districts,year order by Registered_users desc limit 10'''
        access.execute(Query3)
        db.commit()
        t1=access.fetchall()
        data3=pd.DataFrame(t1,columns=['year','Districts','Registered_Users','App_opens'])
              
        fig = px.bar(data3, x='Districts', y='Registered_Users',
             hover_data=['Registered_Users', 'App_opens','year'], color='Districts',title= "District wise Userbase in TamilNadu",
             labels={'Registered_Users':'Registered_Users'}, height=400)

        st.plotly_chart(fig)
        st.write(data3)
        
    
    elif Queries == "4) Top 10 States with highest userbase": 
        Query4='''select year,state,districts,sum(registereduser) as registerusers from map_user group by year,state,districts order by registerusers desc limit 10'''
        access.execute(Query4)
        db.commit()
        t1=access.fetchall()
        data=pd.DataFrame(t1,columns=['year','state','Districts','Registered_Users'])
        
        fig = px.bar(data, x='Districts', y='Registered_Users',
             hover_data=['Registered_Users', 'Districts','year'], color='state',title= "Highest Userbase in India",
             labels={'pop':'population of Canada'}, height=400)

        st.plotly_chart(fig)
        st.write(data)
        
        
    
    elif Queries == "5) Top 10 postal codes of Tamil Nadu with highest userbase": 
        Query5='''select year,pincode,sum(registeredusers) as registeruser from top_user where state='Tamil Nadu' group by pincode,year order by registeruser desc limit 10'''
        access.execute(Query5)
        db.commit()
        t1=access.fetchall()
        data=pd.DataFrame(t1,columns=['year','pincode','Registered_Users'])
        
        fig = px.line(data, x='year', y='Registered_Users', title= "Area wise Userbase in TamilNadu",color='pincode', markers=True)

        st.plotly_chart(fig) 
        st.write(data)
        
        
    
    
    elif Queries == "6) Average transactions of Top states ": 
        Query6='''select state, avg(transaction_amount)as transaction_amount from map_trans  group by state order by transaction_amount desc  limit 10'''
        access.execute(Query6)
        db.commit()
        t1=access.fetchall()
        data=pd.DataFrame(t1,columns=['state','Avg'])
        
        fig = px.bar(data, x='state', y='Avg'          
             , height=700,title= "Avg Transactions")

        st.plotly_chart(fig)
        st.write(data) 
        
        
    elif Queries == "7) Top categories Payment methods": 
        Query7='''select year,state,transaction_type ,sum(transaction_count) as transaction_count, sum(transaction_amount) as transaction_amount from agg_trans group by transaction_type,year,state order by transaction_amount desc limit 10'''
        access.execute(Query7)
        db.commit()
        t1=access.fetchall()
        data=pd.DataFrame(t1,columns=['year','state','transaction_type','transaction_count','transaction_amount'])
        
        colorscale = [[0, '#4d004c'],[.5, '#f2e5ff'],[1, '#ffffff']]
        fig =  ff.create_table(data,colorscale=colorscale)

        st.plotly_chart(fig)
        st.write(data) 
        
        
    elif Queries == "8) Top 10 Districts with most Transactions": 
        Query8='''select year,state,districts,sum(transaction_count) as transaction_count,sum(transaction_amount) as transaction_amount from map_trans group by year,state,districts order by transaction_amount desc limit 10'''
        access.execute(Query8)
        db.commit()
        t1=access.fetchall()
        data=pd.DataFrame(t1,columns=['year','state','districts','transaction_count','transaction_amount'])
        
        colorscale = [[0, '#4d004c'],[.5, '#f2e5ff'],[1, '#ffffff']]
        fig =  ff.create_table(data,colorscale=colorscale)

        st.plotly_chart(fig) 
        st.write(data)
        
        
        
    elif Queries == "9) Top 10 least number of Users": 
        Query9='''select year,state,districts,sum(registereduser) as registerusers from map_user group by year,state,districts order by registerusers  limit 10'''
        access.execute(Query9)
        db.commit()
        t1=access.fetchall()
        data=pd.DataFrame(t1,columns=['year','state','districts','Registerusers'])
        
        fig = px.pie(data, values='Registerusers', names='districts',title= "Least Userbase",hover_data=['state'],hover_name='state', color_discrete_sequence=px.colors.sequential.RdBu)

        st.plotly_chart(fig)
        st.write(data) 
        
        
    elif Queries == "10)Top 10 Districts with more number of userbase": 
        Query10='''select year,state,districts,sum(registereduser) as registerusers from map_user group by year,state,districts order by registerusers desc limit 10'''
        access.execute(Query10)
        db.commit()
        t1=access.fetchall()
        
        data=pd.DataFrame(t1,columns=['year','state','districts','Registerusers'])
        data['year'] = data['year'].astype(str)

        # Remove commas and convert to integers
        data['year'] = data['year'].str.replace(',', '').astype(int)


        
        
        fig = px.pie(data, values='Registerusers', names='districts',hover_data=['state'],hover_name='year',title= "District wise Userbase in India", color_discrete_sequence=px.colors.sequential.RdBu)

        st.plotly_chart(fig) 
        st.write(data)
        
        
        