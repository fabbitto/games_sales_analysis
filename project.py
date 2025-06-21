import streamlit as st
import pandas as pd

# function to load csv
def load_data(filepath):
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        st.error("file not found")
        return None

# count total games by platform
def count_games_by_platform(df):
    return df['Platform'].value_counts()

# count total games by genre
def count_games_by_genre(df):
    return df['Genre'].value_counts()

# get top N publishers
def top_publishers(df, top_n=10):
    return df['Publisher'].value_counts().head(top_n)

# main streamlit app
def main():
    st.title("🎮 video game sales analysis")

    filepath = 'vgsales.csv'
    data = load_data(filepath)

    if data is not None:
        st.subheader("games by platform")
        platform_counts = count_games_by_platform(data)
        st.bar_chart(platform_counts)

        st.subheader("games by genre")
        genre_counts = count_games_by_genre(data)
        st.bar_chart(genre_counts)

        st.subheader("top publishers")
        top_publishers_counts = top_publishers(data)
        st.bar_chart(top_publishers_counts)

if __name__ == "__main__":
    main()
