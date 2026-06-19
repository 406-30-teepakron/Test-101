import streamlit as st

# ส่วนหัวข้อเว็บ (Header)
st.title("ยินดีต้อนรับสู่โปรไฟล์ของฉัน ✨")
st.write("นี่คือเว็บแอปพลิเคชันแรกในชีวิตของผม เขียนด้วยภาษา Python ครับ/ค่ะ")

st.divider() # เส้นคั่นแบ่งสัดส่วนให้สวยงาม

# ส่วนข้อมูลส่วนตัว (Profile Info)
st.header("👤 ข้อมูลส่วนตัว")
st.write("**ชื่อ-นามสกุล:** นายทีปกร พลหาญ เรียนดี มีความรู้")
st.write("**ชั้น ม.4/6** เลขที่ 30")
st.write("**โรงเรียน:** ยุพราชวิทยาลัย")

# ส่วนปุ่มกดแสดงความรู้สึก
if st.button("คลิกบอกความรู้สึกกับการเขียนเว็บครั้งแรก"):
    st.success(f"ว้าว! สนุกและง่ายกว่าที่คิดมาก ๆ! 🎉")
st.divider()
st.link_button("Free cookie", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def page2():
    st.title("Second page")

pg = st.navigation([
    st.Page("page1.py", title="First page", icon="🔥"),
    st.Page(page2, title="Second page", icon=":material/favorite:"),
    st.Page(
        "https://docs.streamlit.io",
        title="Streamlit Docs",
        icon=":material/open_in_new:"
    ),
])
pg.run()
