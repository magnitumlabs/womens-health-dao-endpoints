import argparse
import pandas as pd
import numpy as np

def sqi_heart_rate(hr):
    hr = pd.to_numeric(hr, errors='coerce')
    return ((hr.between(40, 200)).astype(float))

def endpoint_daily_resting_hr(df):
    g = df[df['sleep_flag']==1].groupby('date')['hr'].median().rename('resting_hr_median')
    return g.reset_index()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--seed', type=int, default=42)
    args = ap.parse_args()

    df = pd.read_csv(args.input, parse_dates=['timestamp'])
    df['date'] = df['timestamp'].dt.date
    df['sqi_hr'] = sqi_heart_rate(df['hr'])
    endpoints = endpoint_daily_resting_hr(df)
    endpoints.to_csv(args.out, index=False)
    print(f'Wrote endpoints to {args.out}')

if __name__ == '__main__':
    main()
