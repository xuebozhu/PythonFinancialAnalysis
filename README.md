# PythonFinancialAnalysis

This repository contains utilities to analyse the IBEX35 market.

## Notebooks

`IBEX35Analysis.ipynb` holds the original exploratory analysis.

## ARIMA model

A small script called `prediction.py` loads the historical CSV data and fits an ARIMA model to the closing prices. Use it to produce a simple forecast:

```bash
python prediction.py --csv ibex35b.csv --steps 10
```

## Interactive dashboard

Run the Streamlit application to visualise the data and interact with the model:

```bash
streamlit run app.py
```

Upload a CSV file when prompted, explore the moving averages and generate forecasts for a number of days ahead.
