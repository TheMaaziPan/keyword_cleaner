import streamlit as st
import pandas as pd

# Title of the app
st.title("Keyword Cleaner Tool")

# Step 1: Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file with keywords", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file, header=None)  # Assuming no header in the CSV
    st.write("Original Keywords:")
    st.write(df)

    # Step 2: Input keywords to remove
    keywords_to_remove = st.text_area(
        "Enter keywords to remove (one per line or comma-separated):"
    )

    if keywords_to_remove:
        # Split the input into a list of keywords
        keywords_to_remove = [
            keyword.strip() for keyword in keywords_to_remove.replace(",", "\n").split("\n") if keyword.strip()
        ]

        # Step 3: Remove keywords from the list
        cleaned_df = df[~df[0].isin(keywords_to_remove)]  # Filter out the keywords
        st.write("Cleaned Keywords:")
        st.write(cleaned_df)

        # Step 4: Download the cleaned CSV file
        if not cleaned_df.empty:
            csv = cleaned_df.to_csv(index=False, header=False).encode("utf-8")
            st.download_button(
                label="Download Cleaned CSV",
                data=csv,
                file_name="cleaned_keywords.csv",
                mime="text/csv",
            )
        else:
            st.warning("All keywords were removed. No data to download.")
else:
    st.info("Please upload a CSV file to get started.")