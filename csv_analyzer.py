import pandas as pd

# ------------------------------
# BASIC CSV ANALYSIS
# ------------------------------
def analyze_csv(uploaded_file):
    df = pd.read_csv(uploaded_file)

    summary = {
        "num_rows": len(df),
        "num_columns": len(df.columns),
        "columns": list(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "data_types": df.dtypes.astype(str).to_dict(),
        "head": df.head().to_dict()
    }

    return df, summary
