# 📊 Feedback Intelligence System

A Python-based Feedback Intelligence System that aggregates customer feedback from multiple sources, performs sentiment analysis, identifies recurring issues, tracks trends, and generates stakeholder-ready reports through an interactive Streamlit dashboard.
## 🚀 Project Overview
Product teams receive feedback from multiple channels such as app store reviews and customer surveys. Manually analyzing this feedback is time-consuming and makes it difficult to identify critical issues quickly.
This project automates the process by:
* Collecting feedback from multiple sources
* Analyzing customer sentiment
* Detecting recurring complaints and bugs
* Tracking feedback trends over time
* Generating downloadable PDF reports
* Providing an interactive dashboard for monitoring customer satisfaction
## ✨ Features
### Multi-Source Feedback Collection
* Google Play Store Reviews
* Survey CSV Exports
### Sentiment Analysis
* Positive Reviews
* Neutral Reviews
* Negative Reviews
* Confidence Scores
### Trend Monitoring
* Feedback volume trends
* Sentiment distribution visualization
### Issue Detection
* Extracts common keywords from negative reviews
* Highlights recurring complaints
* Helps prioritize product improvements
### Interactive Dashboard
* KPI Cards
* Source Filters
* Sentiment Filters
* Trend Charts
* Sentiment Pie Charts
* Review Explorer
### PDF Reporting
* One-click report generation
* Weekly feedback summary
* Downloadable PDF reports
## 🛠️ Technology Stack

| Component          | Technology          |
| ------------------ | ------------------- |
| Dashboard          | Streamlit           |
| Data Processing    | Pandas              |
| Sentiment Analysis | TextBlob            |
| Data Source        | Google Play Scraper |
| Charts             | Matplotlib          |
| PDF Reports        | FPDF                |
| Language           | Python              |


## 📂 Project Structure
feedback_intelligence_multi_source_hidevs/
├── app.py
├── survey.csv
├── weekly_report.pdf
├── README.md
├── screenshots/
│ ├── dashboard.png
│ ├── trends.png
│ └── report.png
└── requirements.txt

## ⚙️ Installation
### Step 1: Clone Repository
```bash
git clone https://github.com/Tharuni-2310/feedback_intelligence_multi_source_hidevs.git
cd feedback_intelligence_multi_source_hidevs
```
### Step 2: Install Dependencies
```bash
pip install streamlit pandas textblob matplotlib fpdf google-play-scraper
```
### Step 3: Run Application
```bash
streamlit run app.py
```
Application opens in browser:
```text
http://localhost:8501
```
## 📄 Sample Survey Data
Create a file named:
```text
survey.csv
```
Example:
```csv
date,review
2025-06-01,App crashes every time I open it
2025-06-02,Love the new design
2025-06-03,Login issue still not fixed
2025-06-04,Great experience
2025-06-05,Payment feature is broken
```
## 📊 Dashboard Features
### KPI Metrics
* Total Reviews
* Positive Reviews
* Negative Reviews
* Average Rating
### Visualizations
* Sentiment Distribution Pie Chart
* Feedback Trend Analysis
### Issue Prioritization
Common complaints are identified using keyword frequency analysis on negative reviews.
### Review Explorer
Browse reviews with:
* Source Information
* Date
* Sentiment Classification
## 📄 PDF Report Generation
The dashboard allows users to:
1. Generate a weekly feedback report
2. Download the report as PDF
3. Share insights with stakeholders
## 📸 Screenshots
### Dashboard Overview
Add screenshot:
```text
screenshots/dashboard.png
```
### Trend Analysis
Add screenshot:
```text
screenshots/trends.png
```
### PDF Report
Add screenshot:
```text
screenshots/report.png
```
## 🎥 Demo Video

YouTube Demo Link:

https://www.youtube.com/watch?v=sz0mVyw20PQ

The demo demonstrates:
* Real-time review fetching
* Sentiment analysis
* Trend monitoring
* Issue detection
* PDF report generation
## 🔮 Future Enhancements
* Apple App Store RSS Integration
* Real-Time Scheduled Data Collection
* Advanced NLP Topic Modeling
* Word Cloud Visualization
* Database Storage
* Email Report Delivery
* AI-Based Issue Categorization
## 👨‍💻 Author
Project developed as part of a Feedback Intelligence System assignment demonstrating:
* Data Aggregation
* Sentiment Analysis
* Dashboard Development
* Reporting Automation
* Product Analytics
## 📜 License
This project is intended for educational and demonstration purposes.
