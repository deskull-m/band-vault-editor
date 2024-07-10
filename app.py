import streamlit as st
from streamlit_drawable_canvas import st_canvas

stroke_width = st.sidebar.slider("幅: ", 1, 100, 12)
stroke_height = st.sidebar.slider("高さ: ", 1, 100, 12)

canvas_result = st_canvas(
    width=400,
    height=400,
)