import streamlit as st
from st_pages import Page, show_pages, add_page_title
from PIL import Image

st.image('img_sources\Thumbnail Web.gif')

# Judul aplikasi
st.title('MRI Segmentation Modelling')

# Penjelasan aplikasi
st.write("""
Selamat datang di website kami, website ini menampilkan hasil Modelling dari MRI Segmentation. Website ini menggunakan teknologi 
Machine Learning untuk mengidentifikasi Condyle yang didapatkan dari segmentation MRI. 
Dengan menggunakan algoritma klasifikasi canggih, website ini dapat membantu bagi para pembaca, 
peneliti, dan sekaligus dokter dalam melihat hasil segmentasi Condyle yang sudah kami dapatkan.
""")

# Menjelaskan Segmentation Condyle
st.header('Contoh dari Segmentation')
st.write("""
 Segmentation sendiri merupakan proses dimana bertujuan untuk memisahkan struktur anatomi yang berbeda dalam gambar MRI, 
dalam penelitian ini kami memisahkan struktur tersebut yang dinamakan "Condyle" yang terdapat pada rahang manusia. 
Segmentasi Condyle sendiri sangat membantu para ahli medis untuk mengidentifikasi dan menganalisis struktur anatomi 
yang berkaitan dengan penyakit atau kondisi pasien. Hal ini membantu para ahli medis dalam mengidentifikasi masalah kesehatan, merumuskan pengobatan, 
         dan memantau pengembangan penyakit pasien.

Berikut adalah contoh segmentasi yang kami dapatkan dari Google.com:        
""")
st.image('img_sources\Gradient-based-genetic-algorithm-i-Original-MRI-imageii-Brain-tumor-segmentation.png')

# Menambahkan beberapa penjelasan tambahan jika diperlukan
st.header('Cara Penggunaan')
st.write("""
- Siapkan gambar raw MRI
- Upload Gambar tersebut (tidak boleh melebihi 200 mb)
- Klik pada tombol segmentasi
- Hasil segmentasi MRI akan muncul
""")

st.divider()
st.header('Tentang Kami')
st.write("""
Aplikasi ini dikembangkan oleh tim yang berdedikasi dalam bidang Teknologi Artificial Intelligence. 
Kami berkomitmen akan terus mengembangkan apa yang sudah kami pelajari dengan baik.
""")

show_pages(
    [
        Page("Homepage.py", "🖥️Homepage"),
         Page("pages\Segmentation", "Segmentation"),
    ]
)