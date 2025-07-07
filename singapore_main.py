import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import datetime
import pickle

# Page configuration and styles
st.set_page_config(page_title='Singapore Resale Flat Price Prediction', page_icon='home', initial_sidebar_state='expanded', layout='wide')
st.markdown("""
    <style>
    .main-menu {font-size:20px; margin-top:-40px;}
    .content {padding: 20px;}
    .header {margin-top: 20px; padding-top: 30px; text-align: center; background-color:#002b36 ; padding-bottom: 10px;}
    img {
        max-height: 300px !important;
    }
    </style>
    """, unsafe_allow_html=True)
c1,_,c2=st.columns([2,1,2])

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  
        options=["Home", "Get Prediction"], 
        icons=['house', "star"],  
        default_index=0, 
        orientation="vertical",
        styles={
            "container": {"padding": "5px"},
            "nav-link": {"font-size": "18px", "text-align": "left", "margin": "5px", "--hover-color": "#d2d2d2"},
            "nav-link-selected": {"background-color":"#AEA648"},  
        })

#user input values for selectbox and encoded for respective features
class option:
    option_months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

    encoded_month= {"January" : 1,"February" : 2,"March" : 3,"April" : 4,"May" : 5,"June" : 6,"July" : 7,"August" : 8,"September" : 9,
            "October" : 10 ,"November" : 11,"December" : 12}

    option_town=['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH','BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI',
        'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST','KALLANG/WHAMPOA', 'MARINE PARADE', 'QUEENSTOWN', 'SENGKANG','SERANGOON',
        'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN','LIM CHU KANG', 'SEMBAWANG', 'BUKIT PANJANG', 'PASIR RIS','PUNGGOL']
    
    encoded_town={'ANG MO KIO' : 0 ,'BEDOK' : 1,'BISHAN' : 2,'BUKIT BATOK' : 3,'BUKIT MERAH' : 4,'BUKIT PANJANG' : 5,'BUKIT TIMAH' : 6,
        'CENTRAL AREA' : 7,'CHOA CHU KANG' : 8,'CLEMENTI' : 9,'GEYLANG' : 10,'HOUGANG' : 11,'JURONG EAST' : 12,'JURONG WEST' : 13,
        'KALLANG/WHAMPOA' : 14,'LIM CHU KANG' : 15,'MARINE PARADE' : 16,'PASIR RIS' : 17,'PUNGGOL' : 18,'QUEENSTOWN' : 19,
        'SEMBAWANG' : 20,'SENGKANG' : 21,'SERANGOON' : 22,'TAMPINES' : 23,'TOA PAYOH' : 24,'WOODLANDS' : 25,'YISHUN' : 26}
    
    option_flat_type=['1 ROOM', '2 ROOM','3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE','MULTI-GENERATION']

    encoded_flat_type={'1 ROOM': 0,'2 ROOM' : 1,'3 ROOM' : 2,'4 ROOM' : 3,'5 ROOM' : 4,'EXECUTIVE' : 5,'MULTI-GENERATION' : 6}

    option_flat_model=['2-ROOM','3GEN','ADJOINED FLAT', 'APARTMENT' ,'DBSS','IMPROVED' ,'IMPROVED-MAISONETTE', 'MAISONETTE',
                    'MODEL A', 'MODEL A-MAISONETTE','MODEL A2' ,'MULTI GENERATION' ,'NEW GENERATION', 'PREMIUM APARTMENT',
                    'PREMIUM APARTMENT LOFT', 'PREMIUM MAISONETTE','SIMPLIFIED', 'STANDARD','TERRACE','TYPE S1','TYPE S2']

    encoded_flat_model={'2-ROOM' : 0,'3GEN' : 1,'ADJOINED FLAT' : 2,'APARTMENT' : 3,'DBSS' : 4,'IMPROVED' : 5,'IMPROVED-MAISONETTE' : 6,
                'MAISONETTE' : 7,'MODEL A' : 8,'MODEL A-MAISONETTE' : 9,'MODEL A2': 10,'MULTI GENERATION' : 11,'NEW GENERATION' : 12,
                'PREMIUM APARTMENT' : 13,'PREMIUM APARTMENT LOFT' : 14,'PREMIUM MAISONETTE' : 15,'SIMPLIFIED' : 16,'STANDARD' : 17,
                'TERRACE' : 18,'TYPE S1' : 19,'TYPE S2' : 20}


if selected == "Home":
    st.markdown('<h1 style="text-align: center; color: #002b36;">Singapore Resale Flat Price Prediction</h1>', unsafe_allow_html=True)
    st.image(r"C:\Users\ranji\OneDrive\Desktop\hdb-building-singapore-condo-nguyen-thu-hoai-via-unsplash.jpg.webp", use_column_width=True)
    st.subheader(':blue[About SG-HDB]')
    st.markdown('''Singapore's public housing authority, responsible for planning, developing, and managing quality homes and vibrant towns. Established in 1960 to address a housing crisis, HDB quickly replaced slums with modern flats—building 21,000 homes in under three years and 54,000 by 1965. Today, HDB has completed over 1 million flats in 24 towns and 3 estates, providing homes for about 80% of Singapore’s residents, with a high home ownership rate. For over 50 years, HDB has delivered affordable, quality housing and continues to shape Singapore’s living environment.''',unsafe_allow_html=True)
    st.subheader(':blue[About the Project]')
    st.markdown('''This project aims to predict the resale price of HDB flats in Singapore using machine learning techniques. The dataset includes historical resale flat data, which has been preprocessed and cleaned to ensure accuracy. The project involves feature engineering, outlier detection, and model selection to create a robust prediction model. The final model is deployed in a user-friendly Streamlit application, allowing users to input relevant features and receive predictions on resale prices.''',unsafe_allow_html=True)
    st.subheader(':blue[Project Objective]')
    st.markdown('''The objective of this project is to develop a machine learning model that can accurately predict the resale price of HDB flats in Singapore based on various features such as location, flat type, size, and other relevant factors. The model aims to assist potential buyers and sellers in making informed decisions in the real estate market.''',unsafe_allow_html=True)


if selected == "Get Prediction":
    st.markdown("<h3 style=color:black>Please provide the below details to predict the price",unsafe_allow_html=True)
    st.write('')

    # creted form to get the user input 
    with st.form('prediction'):
        col1,col2=st.columns(2)
        
        with col1:
            user_month=st.selectbox(label='Month',options=option.option_months,index=None)
            user_town=st.selectbox(label='Town',options=option.option_town,index=None)
            user_flat_type=st.selectbox(label='Flat Type',options=option.option_flat_type,index=None)
            user_flat_model=st.selectbox(label='Flat Model',options=option.option_flat_model,index=None)
            floor_area_sqm=st.number_input(label='Floor area sqm',min_value=10.0)
            price_per_sqm=st.number_input(label='Price Per sqm',min_value=100.00)

        with col2:
            year=st.text_input(label='Year',max_chars=4)
            block=st.text_input(label='Block',max_chars=3)
            lease_commence_date=st.text_input(label='Year of lease commence',max_chars=4)
            remaining_lease=st.number_input(label='Remaining lease year',min_value=0,max_value=99)
            years_holding=st.number_input(label='Years Holding',min_value=0,max_value=99)

            c1,c2=st.columns(2)
            with c1:
                storey_start=st.number_input(label='Storey start',min_value=1,max_value=50)
            with c2:
                storey_end=st.number_input(label='Storey end',min_value=1,max_value=51)

            st.markdown('<br>', unsafe_allow_html=True)
            button=st.form_submit_button('PREDICT',use_container_width=True)

    if button:
        with st.spinner("Predicting..."):

            # check if all required fields are filled
            if not all([user_month,user_town,user_flat_type,user_flat_model,floor_area_sqm,price_per_sqm,year,block,
                        lease_commence_date,remaining_lease,years_holding,storey_start,storey_end]):
                st.error("Please fill in all required fields.")
            else:
                current_year=datetime.datetime.now().year
                current_remaining_lease=remaining_lease-(current_year-(int(year)))
                age_of_property=current_year-int(lease_commence_date)
                month=option.encoded_month[user_month]
                town=option.encoded_town[user_town]
                flat_type=option.encoded_flat_type[user_flat_type]
                flat_model=option.encoded_flat_model[user_flat_model]
                floor_area_sqm_log=np.log(floor_area_sqm)
                remaining_lease_log=np.log1p(remaining_lease)
                price_per_sqm_log=np.log(price_per_sqm)

                # Predict the resale price with user data
                with open('Decisiontree.pkl','rb') as files:
                    model=pickle.load(files)

                user_data=np.array([[month, town, flat_type, block, flat_model, lease_commence_date, year, storey_start,
                                    storey_end, years_holding, current_remaining_lease, age_of_property, floor_area_sqm_log, 
                                    remaining_lease_log,price_per_sqm_log ]])

                predict=model.predict(user_data)
                resale_price=np.exp(predict[0])

                # Result
                st.subheader(f"Predicted Resale price is: :green[{resale_price:.2f}]")
