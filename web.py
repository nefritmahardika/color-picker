import streamlit as st
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import io

def get_dominant_colors(image, n_colors):
    image = image.resize((150, 150)) 
    data = np.array(image)
    data = data.reshape((-1, 3))
    
    kmeans = KMeans(n_clusters=n_colors)
    kmeans.fit(data)
    
    colors = kmeans.cluster_centers_.astype(int)
    return colors

st.title('Masukin Gambar Mas!')
st.write('Tau kan harus apa, kalo gatau dipukul sama sayah')

uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Gambar yang diunggah', use_column_width=True)
    
    st.write("")
    st.write("Menghasilkan palet warna...")

    colors = get_dominant_colors(image, 5)
    
    st.write("Palet warna dominan:")
    cols = st.columns(5)
    for idx, color in enumerate(colors):
        with cols[idx]:
            st.write(f'RGB: {tuple(color)}')
            st.color_picker('Color', value='#%02x%02x%02x' % tuple(color), key=idx)
