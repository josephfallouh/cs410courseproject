
# Tesla Twitter Sentiment Analysis and Stock Correlation

This project explores the correlation between Twitter sentiments about Tesla (TSLA) and its corresponding stock performance during a single day: July 11, 2022. Using sentiment analysis tools and statistical methods, we analyze the potential influence of social media sentiments on stock returns.

This code should take roughly 10 minutes to run, due to BERT.

---

## Project Overview

### Objective
- Determine if there is a correlation between Twitter sentiment about Tesla and its stock price performance.
- Evaluate whether such analysis could provide insights into the financial soundness of Twitter's acquisition by Elon Musk.

### Dataset
1. **Tesla Tweets**: Acquired from Kaggle, comprising tweets mentioning Tesla on July 11, 2022.
2. **TSLA Stock Data**: Hourly performance data from TradingView for the same date.

---

## Implementation Details

### 1. Data Preprocessing
- **Tweets**:
  - Removed URLs, mentions, hashtags, special characters, numbers, and leading/trailing whitespaces.
- **Stock Data**:
  - Converted timestamps to Eastern Military Time to align with tweet data.
  - Calculated hourly returns.

### 2. Sentiment Analysis
- **VADER**:
  - Pre-trained rule-based sentiment analyzer.
  - Outputs a compound sentiment score between -1 (negative) and +1 (positive).
- **BERT**:
  - Pre-trained transformer-based sentiment analysis model.
  - Outputs a sentiment score normalized between -1 (negative) and +1 (positive).

### 3. Data Aggregation
- Grouped tweets and stock data by the hour for alignment.
- Calculated average sentiment scores for each hour.

### 4. Statistical Analysis
- **Pearson Correlation**:
  - Measured the linear relationship between hourly sentiment scores (from VADER and BERT) and TSLA stock returns.

### 5. Visualizations
- Scatter plots for sentiment scores vs. stock returns.
- Distribution and boxplots for sentiment scores.
- Line and bar charts for hourly sentiment scores.
- Word clouds for the most positive and negative tweets.

---

## Results

### Correlation Analysis
- **VADER**:
  - Correlation: 0.439
  - P-value: 0.561 (not statistically significant)
- **BERT**:
  - Correlation: 0.589
  - P-value: 0.411 (not statistically significant)

### Observations
- **BERT outperformed VADER** in terms of correlation strength.
- Small dataset and high p-values indicate no statistically significant relationship.

---

## Challenges
- Limited dataset (only 1 day, 4 data points) constrained statistical significance.
- Uneven distribution of tweets across hours may have biased results.
- Switching from Spearman to Pearson correlation due to data size constraints.

---

## Future Applications
- Expanding this process to larger datasets can enable:
  - Enhanced prediction models for stock performance based on sentiment.
  - Improved financial decision-making influenced by social media trends.

---

## Outputs
The following artifacts were generated during this analysis:
- CSV file: `sentiment_analysis_results.csv` (processed data).
- Visualizations:
  - `vader_scatter.png`, `bert_scatter.png`: Scatter plots for sentiment vs. returns.
  - `vader_distribution.png`, `bert_distribution.png`: Sentiment distributions.
  - `negative_tweets_wordcloud.png`, `positive_tweets_wordcloud.png`: Word clouds.

---

## Prerequisites and Setup

### Requirements
- Python 3.x
- Libraries:
  - `pandas`, `numpy`, `nltk`, `matplotlib`, `seaborn`, `wordcloud`, `scipy`, `torch`, `transformers`

### Setup Instructions
1. Clone this repository.
2. Install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Download and place the following datasets:
   - `Tesla.csv` (tweets dataset)
   - `TSLA_stock_data.csv` (stock data)

4. Run the main script:
   ```bash
   jupyter notebook TSLA_sentiment.ipynb
   ```

---

## Authors
- Festus Folan
- Joseph Fallouh
- Reva Jethwani
- Elizabeth Ryser

---

## References
- Tesla Twitter Dataset on Kaggle: [Link](https://www.kaggle.com/datasets/vishesh1412/twitter-dataset-tesla)
- TSLA Stock Data on Trading View: [Link](https://www.tradingview.com/chart/?symbol=NASDAQ%3ATSLA)
