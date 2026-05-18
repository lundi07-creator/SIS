"""Data loading and processing utilities."""

import pandas as pd
import numpy as np


def load_raw(path):
    """Load raw CSV data file.
    
    Args:
        path: Path to CSV file
    
    Returns:
        df: Pandas DataFrame with raw data
    """
    df = pd.read_csv(path)
    return df


def load_excel(path, sheet_name=0):
    """Load data from Excel file.
    
    Args:
        path: Path to Excel file
        sheet_name: Sheet name or index (default: first sheet)
    
    Returns:
        df: Pandas DataFrame
    """
    df = pd.read_excel(path, sheet_name=sheet_name)
    return df


def save_processed(df, path, index=False):
    """Save processed data to CSV.
    
    Args:
        df: Pandas DataFrame
        path: Output file path
        index: Whether to save index (default: False)
    """
    df.to_csv(path, index=index)


def save_excel(df, path, sheet_name='Sheet1', index=False):
    """Save processed data to Excel.
    
    Args:
        df: Pandas DataFrame
        path: Output file path
        sheet_name: Excel sheet name
        index: Whether to save index (default: False)
    """
    df.to_excel(path, sheet_name=sheet_name, index=index)


def sync_timestamps(df_sending, df_receiving, time_col='timestamp'):
    """Synchronize two-end measurement data by timestamp.
    
    Args:
        df_sending: Sending-end data DataFrame
        df_receiving: Receiving-end data DataFrame
        time_col: Name of timestamp column
    
    Returns:
        df_synced: Merged DataFrame with synced measurements
    """
    df_sending = df_sending.copy()
    df_receiving = df_receiving.copy()
    
    # Merge on timestamp
    df_synced = pd.merge(
        df_sending,
        df_receiving,
        on=time_col,
        suffixes=('_s', '_r')
    )
    
    return df_synced


def validate_measurements(df):
    """Validate measurement data for NaN and outliers.
    
    Args:
        df: DataFrame with measurements
    
    Returns:
        is_valid: Boolean array indicating valid rows
    """
    is_valid = ~df.isnull().any(axis=1)
    return is_valid


def remove_outliers(df, columns, threshold_std=3):
    """Remove outliers using z-score method.
    
    Args:
        df: Input DataFrame
        columns: List of columns to check for outliers
        threshold_std: Z-score threshold (default: 3 std)
    
    Returns:
        df_clean: DataFrame with outliers removed
    """
    df_clean = df.copy()
    
    for col in columns:
        z_scores = np.abs((df_clean[col] - df_clean[col].mean()) / df_clean[col].std())
        df_clean = df_clean[z_scores < threshold_std]
    
    return df_clean