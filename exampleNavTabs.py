import streamlit as st

# TABS SECTION
tab1, tab2, tab3 = st.tabs(["Home", "About Group", "Image Processing Application"])


# HOME CONTENT
with tab1:
    st.title("Welcome to the Image Processing Web Application")
    st.write("Navigate using the sidebar to explore different sections of the application.")


# ABOUT CONTENT
with tab2:
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


# UPLOAD IMAGE CONTENT
with tab3:
    st.title("Image Processing Application")
    st.write("Upload an image to apply processing.")
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("Choose an image processing operation:")
        operation = st.radio("Operation", ["Original", "Grayscale", "Blur"])

        if operation == "Grayscale":
            processed_image = image.convert("L")
            st.image(processed_image, caption="Grayscale Image", use_column_width=True)

        elif operation == "Blur":
            processed_image = image.filter(ImageFilter.BLUR)
            st.image(processed_image, caption="Blurred Image", use_column_width=True)

        else:
            st.write("No processing applied.")
