import streamlit as st

st.title("Image Processing Web Application")

st.sidebar.title("Navigation")
st.sidebar.write("Use the menu to navigate.")
st.sidebar.write("About Group")
st.sidebar.write("Image processing")

st.title("About the Group")
st.write("This page provides information about the group members.")

group_members = [
    {"Name": "Sandi", "Role": "Leader", "Email": "alice@example.com"},
    {"Name": "Ruddi", "Role": "Developer", "Email": "bob@example.com"},
    {"Name": "Raden", "Role": "Tester", "Email": "charlie@example.com"},
]

for member in group_members:
    st.subheader(member["Name"])
    st.write(f"**Role:** {member['Role']}")
    st.write(f"**Email:** {member['Email']}")
    st.write("---")

st.title("Image Processing Application")
st.write("Upload an image to apply processing.")

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.write("Choose an image processing operation:")
    operation = st.selectbox("Operation", ["Original", "Grayscale", "Blur"])

    if operation == "Grayscale":
        processed_image = image.convert("L")
        st.image(processed_image, caption="Grayscale Image", use_column_width=True)

    elif operation == "Blur":
        processed_image = image.filter(ImageFilter.BLUR)
        st.image(processed_image, caption="Blurred Image", use_column_width=True)

    else:
        st.write("No processing applied.")
