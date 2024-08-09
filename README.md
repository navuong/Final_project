Classification of Earnings Transcripts for Trading Signals

In this project, we analyzed earnings transcripts to classify their impact on stock prices: positive, neutral, negative.
It gives investors insights from earning call, on whether they should buy, sell or hold their positions.

Key steps and findings:

Data Collection:
- Transcripts: Earning transcript from April 2019 to Feb 2023, filtered on 431 companies within S&P 500 Index.
In total we have 3198 data points.
Source: https://www.kaggle.com/datasets/tpotterer/motley-fool-scraped-earnings-call-transcripts
Download and save the file to the project directory, file name is 'motley-fool-data.pkl'
- Stock Prices: Daily prices within the same period.
Source: yahoo finance

Labelling: We calculate the price change between 1 day after the earning call and 1 day before the earning call:
Label = Positive (2): Price change ≥ +2%
Label = Neutral (1): Price change between -2% and +2%
Label = Negative (0): Price change ≤ -2%

Data Processing:
We removed companies having less than 4 earning transcripts.
Earning transcripts are converted into 768-dimensional vectors using RoBERTa pre-trained models.
We split data into training (April 2019-Dec. 2021) and test (Jan 2022-Feb 2023) sets.

Model Evaluation:
We tested 4 models on the embedded data: 
feedforward neural networks FNN,
gated graph neural network GNN inspired by whitepaper: https://arxiv.org/pdf/2203.12460,
support vector machine SVM, 
and logistic regression.

Metric used is F1 score.
Feedforward neural network has highest F1 Score: 38.27
Baseline model: Logistic regression: F1 score: 37.09

Hyperparameter Fine-Tuning:
Used Optuna for systematic optimization on FNN and GNN
Dropout was introduced to GNN to avoid overfitting
Used grid search for SVM
No optimisation on logistic regression

Future Improvements:
Analyze performance at the sector level.
Expand the dataset to longer history for robustness.
Integrate a stock trading strategy and backtest for practical evaluation of the output.
Reassess the threshold for labelling criteria to enhance model sensitivity and specificity.
