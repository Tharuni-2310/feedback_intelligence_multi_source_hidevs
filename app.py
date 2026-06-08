import streamlit as st
import pandas as pd
from textblob import TextBlob
from google_play_scraper import reviews
import matplotlib.pyplot as plt
from collections import Counter
from fpdf import FPDF
import os

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Feedback Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------------
# TITLE
# -----------------------------------

st.title("📊 Feedback Intelligence Dashboard")
st.markdown(
    "Monitor customer feedback, sentiment trends, and critical issues across multiple feedback sources."
)

# -----------------------------------
# LOAD GOOGLE PLAY REVIEWS
# -----------------------------------

@st.cache_data
def fetch_google_reviews():
    try:
        result, _ = reviews(
            'com.whatsapp',
            lang='en',
            country='us',
            count=100
        )

        df = pd.DataFrame(result)

        df = df[['content', 'score', 'at']]
        df.columns = ['review', 'rating', 'date']

        df['source'] = 'Google Play'

        return df

    except Exception as e:
        st.warning(f"Google Play fetch failed: {e}")
        return pd.DataFrame()

# -----------------------------------
# LOAD CSV REVIEWS
# -----------------------------------

@st.cache_data
def load_csv_reviews():
    try:
        df = pd.read_csv("survey.csv")

        if "date" not in df.columns:
            df["date"] = pd.Timestamp.now()

        df["source"] = "Survey"

        return df

    except Exception as e:
        st.warning(f"CSV load failed: {e}")
        return pd.DataFrame()

# -----------------------------------
# SENTIMENT ANALYSIS
# -----------------------------------

def get_sentiment(text):

    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0:
        return pd.Series(["Positive", round(abs(polarity), 2)])

    elif polarity < 0:
        return pd.Series(["Negative", round(abs(polarity), 2)])

    return pd.Series(["Neutral", 0])

# -----------------------------------
# FETCH DATA
# -----------------------------------

google_df = fetch_google_reviews()
csv_df = load_csv_reviews()

if not google_df.empty:
    df = pd.concat([google_df, csv_df], ignore_index=True)
else:
    df = csv_df.copy()

df[['sentiment', 'confidence']] = df['review'].apply(get_sentiment)

df["date"] = pd.to_datetime(df["date"])

# -----------------------------------
# SIDEBAR FILTERS
# -----------------------------------

st.sidebar.header("🔍 Filters")

source_filter = st.sidebar.selectbox(
    "Source",
    ["All"] + list(df["source"].unique())
)

sentiment_filter = st.sidebar.selectbox(
    "Sentiment",
    ["All", "Positive", "Neutral", "Negative"]
)

if source_filter != "All":
    df = df[df["source"] == source_filter]

if sentiment_filter != "All":
    df = df[df["sentiment"] == sentiment_filter]

# -----------------------------------
# KPI SECTION
# -----------------------------------

total_reviews = len(df)

positive_reviews = len(
    df[df["sentiment"] == "Positive"]
)

negative_reviews = len(
    df[df["sentiment"] == "Negative"]
)

avg_rating = round(
    df["rating"].mean(),
    2
) if "rating" in df.columns else 0

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "📋 Total Reviews",
    total_reviews
)

col2.metric(
    "😊 Positive",
    positive_reviews
)

col3.metric(
    "😡 Negative",
    negative_reviews
)

col4.metric(
    "⭐ Avg Rating",
    avg_rating
)

st.divider()

# -----------------------------------
# TABS
# -----------------------------------

tab1, tab2, tab3 = st.tabs(
    [
        "📊 Overview",
        "🚨 Issues",
        "📝 Reviews"
    ]
)

# -----------------------------------
# TAB 1 - OVERVIEW
# -----------------------------------

with tab1:

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Sentiment Distribution")

        fig1, ax1 = plt.subplots()

        df["sentiment"].value_counts().plot.pie(
            autopct="%1.1f%%",
            ax=ax1
        )

        ax1.set_ylabel("")

        st.pyplot(fig1)

    with col2:

        st.subheader("Feedback Trend")

        trend = (
            df.groupby(
                df["date"].dt.date
            )
            .size()
        )

        st.line_chart(trend)

# -----------------------------------
# TAB 2 - ISSUES
# -----------------------------------

with tab2:

    st.subheader("🚨 Top Complaints")

    negative_df = df[
        df["sentiment"] == "Negative"
    ]

    words = []

    for review in negative_df["review"]:
        words.extend(
            str(review).lower().split()
        )

    common_words = Counter(words).most_common(15)

    issues_df = pd.DataFrame(
        common_words,
        columns=["Keyword", "Mentions"]
    )

    st.dataframe(
        issues_df,
        use_container_width=True
    )

    st.subheader("Negative Reviews")

    st.dataframe(
        negative_df[
            ["review", "source", "date"]
        ],
        use_container_width=True
    )

# -----------------------------------
# TAB 3 - REVIEWS
# -----------------------------------

with tab3:

    st.subheader("All Reviews")

    st.dataframe(
        df.sort_values(
            by="date",
            ascending=False
        ),
        use_container_width=True
    )

# -----------------------------------
# PDF GENERATION
# -----------------------------------

def generate_pdf():

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        "B",
        16
    )

    pdf.cell(
        0,
        10,
        "Weekly Feedback Report",
        ln=True
    )

    pdf.ln(5)

    pdf.set_font(
        "Arial",
        size=12
    )

    pdf.cell(
        0,
        10,
        f"Total Reviews: {total_reviews}",
        ln=True
    )

    pdf.cell(
        0,
        10,
        f"Positive Reviews: {positive_reviews}",
        ln=True
    )

    pdf.cell(
        0,
        10,
        f"Negative Reviews: {negative_reviews}",
        ln=True
    )

    pdf.ln(5)

    pdf.multi_cell(
        0,
        10,
        "Top detected issues are based on frequently occurring words in negative reviews."
    )

    pdf.output(
        "weekly_report.pdf"
    )

# -----------------------------------
# REPORT SECTION
# -----------------------------------

st.divider()

st.subheader("📄 Weekly Report")

if st.button("Generate PDF Report"):

    generate_pdf()

    st.success(
        "PDF report generated successfully!"
    )

if os.path.exists(
    "weekly_report.pdf"
):

    with open(
        "weekly_report.pdf",
        "rb"
    ) as file:

        st.download_button(
            label="⬇ Download Report",
            data=file,
            file_name="weekly_report.pdf",
            mime="application/pdf"
        )