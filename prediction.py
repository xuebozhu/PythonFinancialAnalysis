import argparse
from pathlib import Path

import pandas as pd
import statsmodels.api as sm


def load_data(csv_path: Path) -> pd.DataFrame:
    """Load CSV with IBEX35 data and return a DataFrame indexed by date."""
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['<DTYYYYMMDD>'].astype(str), format='%Y%m%d')
    df = df.set_index('Date').sort_index()
    return df


def train_arima(df: pd.DataFrame, order=(5, 1, 0)):
    """Train ARIMA model on the CLOSE column."""
    model = sm.tsa.ARIMA(df['<CLOSE>'], order=order)
    return model.fit()


def forecast(model, steps: int) -> pd.Series:
    """Forecast future closing prices."""
    return model.forecast(steps=steps)


def main() -> None:
    parser = argparse.ArgumentParser(description="ARIMA forecasting for IBEX35")
    parser.add_argument('--csv', required=True, help='Path to CSV file with data')
    parser.add_argument('--steps', type=int, default=5, help='Days to forecast')
    args = parser.parse_args()

    df = load_data(Path(args.csv))
    model = train_arima(df)
    fc = forecast(model, args.steps)
    print(fc)


if __name__ == '__main__':
    main()
