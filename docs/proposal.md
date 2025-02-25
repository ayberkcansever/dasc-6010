# **Cryptocurrency Market Correlation Analysis**

## **Problem Statement**
Cryptocurrency markets are volatile, and altcoins often react to Bitcoin’s price movements.

- **Importance**: Understanding correlations helps traders manage risks and optimize their portfolios.
- **Research Question**: How do altcoin price movements correlate with Bitcoin’s price and dominance?

---

## **Data Collection & Description**
- **Source**: Fetching real-time and historical data from Binance, Coinbase, and Kraken APIs.
- **Scope**: At least 5 major altcoins (ETH, BNB, ADA, SOL, XRP) over 1 year.
- **Dataset Structure**:
  - **Timestamps** (15-minute intervals)
  - **OHLC** (Open, High, Low, Close)
  - **Volume**
- **Storage**: PostgreSQL for efficient querying & processing.

---

## **Methodology & Tools**
### **Tools**
- **Python** (Requests, Pandas, NumPy, SciPy)
- **PostgreSQL** (for data storage)
- **Matplotlib/Seaborn** (for visualization)
- **Statsmodels & Scikit-learn** (for correlation analysis)

### **Steps**
1. Fetch & store data in PostgreSQL.
2. Perform data cleaning (handling NaNs, duplicates).
3. Compute correlation coefficients between BTC and altcoins.
4. Visualize trends and patterns.

---

## **Correlation Analysis Approach**
- **Statistical Approach**:
  - **Pearson Correlation**: Measures linear relationship (r-value).
  - **Spearman Rank Correlation**: Captures nonlinear trends.
  - **Rolling Window Correlation**: How correlation changes over time.

---

## **Planned Visualizations**
- **Correlation Heatmap** (to compare multiple altcoins with BTC).
- **Scatter Plots** (visualizing BTC vs. individual altcoins).
- **Rolling Correlation Line Graph** (tracking correlation shifts over time).
- **Histogram of Returns** (to see distribution differences).

---

## **Hypothesis**
- Some altcoins (**ETH, BNB**) will be **highly correlated** with BTC.
- Others (**ADA, SOL**) might be **less correlated** due to independent market drivers.
- **Use Case**: Traders can use these correlations for **hedging strategies** and **diversification**.
- **Limitations**:
  - Market sentiment & news events influence prices unpredictably.
  - External factors like regulations impact correlations.

---

## **Timeline**
| **Week** | **Task** |
|----------|------------------------------------------------|
| **Week 1** | Determine altcoins and identify public APIs for data fetching |
| **Week 2** | Set up PostgreSQL & design the database |
| **Week 3** | Write initial API call scripts and persist data for different crypto coins |
| **Week 4** | Compute descriptive statistics and Pearson/Spearman correlation |
| **Week 5** | Visualize price movements, heatmaps, and scatter plots for correlation |
| **Week 6** | Prepare the final presentation with findings |

## **Timeline**
![Project Timeline](timeline.png)

---

📌 *This project aims to provide actionable insights into Bitcoin’s influence on altcoin markets, helping traders develop better strategies based on historical data and statistical correlations.*
