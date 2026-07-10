import streamlit as st
st.title("แอปพลิเคชั่นแปลงปี พ.ศ. เป็น ค.ส.")

bh_year=st.number_input("กรอกปี พ.ศ. ที่ต้องการแปลง",value=2569)
ce_year=bh_year-543
st.header(f"ปี ค.ศ. คือ : {ce_year}")
#f = เชื่อมการแสดงผลตัวเลขกับตัวหนังสือ

ce_year2=st.number_input("กรอกปี ค.ศ. ที่ต้องการแปลง",value=2026)
bh_year2=ce_year2+543
st.header(f"ปี พ.ศ. คือ : {bh_year2}")
