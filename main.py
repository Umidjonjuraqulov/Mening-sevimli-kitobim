import streamlit as st 

st.title("Mening sevimli kitobim")
st.subheader("Sariq devni minib")
col1, col2 = st.columns((3, 7)) 
col1.image("images/3552.JPG")
col2.write("O'zbekiston xalq yozuvchisi, bolalarning sevimli adibi Xudoyberdi To'xtaboyevning asarlari nafaqat respublikamizda, balki chet ellarda ham ma'lum va mashhurdir.“Sariq devni minib” sarguzasht romani esa bolalar hayotidan olib yozilgan bo'lib, ularning sevimli kitoblaridandir. Bu asarda orzu-havasga eltadigan chinakam yo'l halol mehnat, yaxshi xulq-odob va qunt bilan o'qishda ekanligi ta'kidlanadi.Ushbu kitob dunyoning 28 ta mamlakatida rus, ingliz, fransuz va nemis tillarida nashr etilgan.")
col2.write("**Muallif:** Xudoyberdi To'xtaboyev")
col2.write("**Sahifasi:** 544 bet")
col2.write("**Yozilgan yili:** 1968-yil")
