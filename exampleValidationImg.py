import streamlit as st
from PIL import Image, ImageFilter

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
    # VALIDATION IMAGE
    def validate_image(image):
        try:
            img = Image.open(image)
            img.verify() 
        except Exception as e:
            st.error("Invalid image file. Please upload a valid image file (.jpg, .jpeg, .png).")
            return False

        # Check file type
        if not image.name.lower().endswith(('.jpg', '.jpeg', '.png')):
            st.error("Invalid file type. Please upload a .jpg, .jpeg, or .png image.")
            return False

        # Check size
        max_size_MB = 2  # 2 MB
        max_size_bytes = max_size_MB * 1024 * 1024  # 2 MB in bytes
        if image.size > max_size_bytes:
            st.error(f"File size too large. Maximum allowed size is {max_size_MB} MB.")
            return False

        # Check dimensions
        img_width, img_height = img.size
        min_dim = 100  # Minimum dimension (width / height)
        max_dim = 2000  # Maximum dimension (width / height)
        if img_width < min_dim or img_width > max_dim or img_height < min_dim or img_height > max_dim:
            st.error(f"Invalid image dimensions. Image dimensions should be between {min_dim}x{min_dim} and {max_dim}x{max_dim} pixels.")
            return False
        return True

    # CONTENT IMAGE
    st.title("Image Processing Application")
    st.write("Upload an image to apply processing.")
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        if validate_image(uploaded_image):
            image = Image.open(uploaded_image)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            operation = st.radio("Operation", ["Original", "Grayscale", "Blur"], key="operation")
            
            if operation == "Grayscale":
                processed_image = image.convert("L")
                st.image(processed_image, caption="Grayscale Image", use_column_width=True)

            elif operation == "Blur":
                processed_image = image.filter(ImageFilter.BLUR)
                st.image(processed_image, caption="Blurred Image", use_column_width=True)

            else:
                st.write("No processing applied.")
        else:
            st.write("Invalid image uploaded.")