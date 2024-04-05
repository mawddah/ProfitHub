from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Profit Hub", page_icon=":tada:", layout="wide")
st.title('Profit Hub :wave:')

imge1 = Image.open("images/Picture1.png")
imge2 = Image.open("images/Picture2.png")
imge3 = Image.open("images/Picture3.png")
imge5 = Image.open("images/Picture5.png")

with st.container():
    tab1, tab2, tab3, tab4 = st.tabs(["الرئيسية", "اشترك","المشاريع" ,"طلب تمويل"])
    
with st.container():
    tab1.write("تصفح واستثمر")
    
with tab1:
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(imge1)
        
    with text_column:
        st.subheader("Simple Home")
        st.write(
            """

انطلاقاً من جدة نختص بالمشاريع السكنية والتجارية , والواجهات السياحية
"""
            )
        st.caption('Balloons. Hundreds of them...')

        result = st.button('استثمر')
        if result:
            st.write(':confetti_ball:')
        
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(imge2)
        with text_column:
            st.subheader("متجر روشيه")
            st.write(
            """
متجر روشيه يقدم الستر المحبوكة بسعر رمزي والتصميم بطلب العميل .
""")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(imge3)
    with text_column:
        st.subheader("Crème")
        st.write(
            """

صناعه منزليه للمخبوزات بمختلف الانواع . 

""")
    def unauthenticated_menu():
        st.page_link("profit-2.py", label="Home", icon="🏠")
   
with st.container():
    tab2.write("this is tab 2")

with st.container():
    tab3.write("this is tab 2")
with st.container():
    tab4.write("this is tab 2")
