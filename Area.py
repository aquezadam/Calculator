# ••• Build a Streamlit app that can help users calculate geometrical areas of square
# and circle when the input is side and radius respectively.

import streamlit as st

st.markdown('''
    <h1 
    style='background-color:#DCDCDC;
    text-align:center;
    color:#1A5276;'>
    GEOMETRICAL CALCULATIONS
    </h1>
    ''', unsafe_allow_html=True)
st.markdown("")
shape_choice = st.selectbox("Choose the shape you wish to know its area:", ["SELECT", "SQUARE", "CIRCLE"])
if shape_choice == "SQUARE":
    dim_side = st.number_input("Please enter the dimension of one side of the square in cm: ", min_value=1.0, step=0.1)
    area_square = dim_side**2
    if st.button("Calculate area of square:"):
        st.success(f"The area of the square is {area_square:,.2f} cm.")
elif shape_choice == "CIRCLE":
    radius_side = st.number_input("Please enter the dimension of the radius of the circle in cm: ")
    area_circle = 3.14*(radius_side**2)
    if st.button("Calculate area of circle:"):
        st.success(f"The area of the circle is {area_circle:,.2f} cm.")
elif shape_choice == "SELECT":
    text_prompt = st.text("Please choose between circle and square.")






# --- AS COLUMNS

# columns = st.columns(2)
# sq = columns[0].number_input("Please enter the dimensions of the side of the rectangle: ")
# cr = columns[1].number_input("Please enter the dimensions of the radius of the circle: ")
# formula_area_square = sq**2
# formula_area_circle = 3.14*(cr**2)
# area_square = columns[0].text(f"The area of the square is {formula_area_square:,.2f} cm.")
# area_circle = columns[1].text(f"The area of the circle is {formula_area_circle:,.2f} cm.")


