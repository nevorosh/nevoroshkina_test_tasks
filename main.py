import pandas as pd
import numpy as np
from ucimlrepo import fetch_ucirepo 


output_type = input("Enter the saving file format (xlsx, markdown, html):\n")
if output_type not in ["xlsx", "markdown", "html"]:
    raise ValueError(f"Unsupported output type: {output_type}")
out_file_name = input("\n")

dataset = fetch_ucirepo(id=53) 
df = dataset.data.features


analise_df = pd.DataFrame(columns=[
    "columns_name",
    "column_type",
    "min",
    "max",
    "mean",
    "median",
    "mode",
    "zero_rows_pr",
    "variance",
    "standard deviation",
    "interquartile_range",
    "coefficient of variation",
    "num_of_distinct_val"
])

for column in df.columns:
    data = df[column]
    new_row = {
        "columns_name": column,
        "column_type": data.dtype,
        "min": data.min() if np.issubdtype(data.dtype, np.number) else None,
        "max": data.max() if np.issubdtype(data.dtype, np.number) else None,
        "mean": data.mean() if np.issubdtype(data.dtype, np.number) else None,
        "median": data.median() if np.issubdtype(data.dtype, np.number) else None,
        "mode": data.mode().iloc[0] if not data.mode().empty else None,
        "zero_rows_pr": data.isnull().sum()/len(data) * 100 if np.issubdtype(data.dtype, np.number) else None,
        "variance": data.var() if np.issubdtype(data.dtype, np.number) else None,
        "standard deviation": data.std() if np.issubdtype(data.dtype, np.number) else None,
        "interquartile_range": (data.quantile(0.75)) - (data.quantile(0.25)) if np.issubdtype(data.dtype, np.number) else None,
        "coefficient of variation":(data.std() / data.mean()) * 100 if np.issubdtype(data.dtype, np.number) and data.mean() != 0 else None,
        "num_of_distinct_val": data.nunique(),
    }
    analise_df = pd.concat([analise_df, pd.DataFrame([new_row])], ignore_index=True)

if output_type == "xlsx":
    analise_df.to_excel(f"{out_file_name}.xlsx", index=False, sheet_name="Sheet1")
elif output_type == "html":
    analise_df.to_html(f"{out_file_name}.html", index=False)
elif output_type == "markdown":
    with open(f"{out_file_name}.md", "w") as f:
        f.write(analise_df.to_markdown(index=False))





