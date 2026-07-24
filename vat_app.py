import streamlit as st
st.title("แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")
price=st.number_input("ระบุราคาราคา")
vat=price*7/100
st.header(f"ราคาคือ : {vat}")
