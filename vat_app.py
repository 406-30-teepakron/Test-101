import streamlit as st
st.title("แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")
price=st.number_input("ระบุราคาราคา")
vat=price*7/100
st.header(f"ภาษีมูลค่าเพิ่ม (VAT 7%) : {vat:.2f} บาท")
st.header(f"ราคาสุทธิ : {price-vat:.2f} บาท")
st.divider()
st.write("นายทีปกร พลหาญ เลขที่30 4/6")
