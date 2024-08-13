# Stock Price Prediction Script
 
## Overview

This Python script processes stock price data from different stock exchanges, samples data from the files provided, and predicts the next three stock prices based on a simple prediction algorithm.
 
## Features

- Randomly selects 10 consecutive data points from the provided stock data files.

- Predicts the next 3 stock prices based on the selected data.

- Outputs the predictions into a new CSV file for each processed file.
 
## Prediction Logic

The prediction is based on a simple heuristic:

1. The first predicted value is the second-highest value in the selected 10 data points.

2. The second predicted value is halfway between the last data point and the first predicted value.

3. The third predicted value is one-fourth the difference between the first and second predicted values.
 
## Requirements

- Python 3.6 or later

- The following Python libraries:

  - `pandas`

  - `numpy`

You can install the required libraries using pip:

```bash

pip install pandas numpy

 
