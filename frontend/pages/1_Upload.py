import streamlit as st

from services.api import upload_document


st.title(
    "📄 Upload Architecture Document"
)


st.write(
    "Upload software architecture documents for analysis."
)


uploaded_file = st.file_uploader(
    "Drag and drop your PDF here",
    type=["pdf"],
)



if uploaded_file:

    st.subheader("Document Information")


    col1, col2 = st.columns(2)


    with col1:

        st.write(
            "Filename"
        )

        st.info(
            uploaded_file.name
        )


    with col2:

        st.write(
            "Size"
        )

        st.info(
            f"{uploaded_file.size / 1024:.2f} KB"
        )


    progress_bar = st.progress(0)


    def update_progress(value):

        progress_bar.progress(value)



    if st.button(
        "Upload Document"
    ):


        try:

            with st.spinner(
                "Uploading document..."
            ):

                response = upload_document(
                    uploaded_file,
                    update_progress,
                )


            st.success(
                response["message"]
            )


            st.subheader(
                "Generated Metadata"
            )


            metadata = response["document"]


            st.json(
                metadata
            )


        except Exception as error:


            st.error(
                f"Upload failed: {error}"
            )