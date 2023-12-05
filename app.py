import streamlit as st
from st_pages import Page, show_pages, add_page_title
from PIL import Image

st.image('img_sources\Thumbnail Web.gif')

# Judul aplikasi
st.title('MRI Segmentation Modelling')

# Penjelasan aplikasi
st.write("""
Selamat datang di website hasil Modelling dari MRI Segmentation. Website ini menggunakan teknologi 
machine learning untuk mengidentifikasi Condyle yang didapatkan dari segmentation MRI. 
Dengan menggunakan algoritma klasifikasi canggih, website ini dapat membantu bagi para pembaca, 
peneliti, dan sekaligus dokter dalam melihat hasil segmentasi Condyle yang sudah kami dapatkan.
""")

# Menambahkan beberapa penjelasan tambahan jika diperlukan
st.header('Cara Penggunaan')
st.write("""
- belum kepikiran der
""")

st.divider()
st.header('Tentang Kami')
st.write("""
Aplikasi ini dikembangkan oleh tim yang berdedikasi dalam bidang Teknologi Artificial Intelligence. 
Kami berkomumitmen akan terus mengembangkan apa yang sudah kami pelajari dengan baik.
""")

# Foto pertama
image1 = "Jackyyy.jpg"

# Foto kedua
image2 = "Jackyyy.jpg"

# Foto ketiga
image3 = "Jackyyy.jpg"

# Ukuran foto
image_width = 200

# Buat kolom
st.columns(3)

# Tambahkan foto pertama ke kolom pertama
st.column(1).image(image1, width=200)

# Tambahkan foto kedua ke kolom kedua
st.column(2).image(image2, width=200)

# Tambahkan foto ketiga ke kolom ketiga
st.column(3).image(image3, width=200)

show_pages(
    [
        Page("app.py", "Pendahuluan"),
         Page("pages/ Penjelasan Segmentasi"),
    ]
)