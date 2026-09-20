from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "loans.csv"
OUTPUT_DIR = PROJECT_ROOT / "graphs"
REPORT_FILE = PROJECT_ROOT / "reports" / "loan_data_report.txt"
FEATURES = ["income", "credit_score", "loan_amount", "employment_years"]


def save_data_report(data):
    with REPORT_FILE.open("w", encoding="utf-8") as report:
        report.write("LOAN DATASET REPORT\n")
        report.write("===================\n\n")
        report.write(f"Rows: {len(data)}\n")
        report.write(f"Columns: {', '.join(data.columns)}\n\n")
        report.write("DESCRIPTIVE STATISTICS\n")
        report.write(data.describe().to_string())
        report.write("\n\nLOAN STATUS COUNTS\n")
        report.write(data["loan_status"].value_counts().sort_index().to_string())
        report.write("\n\nFULL CSV DATA\n")
        report.write(data.to_string(index=False))


def save_visualizations(data):
    OUTPUT_DIR.mkdir(exist_ok=True)
    plt.style.use("seaborn-v0_8-whitegrid")

    figure, axes = plt.subplots(2, 2, figsize=(13, 9))
    for axis, feature in zip(axes.flat, FEATURES):
        axis.hist(data.loc[data["loan_status"] == 0, feature], bins=20, alpha=0.65, label="Rejected", color="#a94b43")
        axis.hist(data.loc[data["loan_status"] == 1, feature], bins=20, alpha=0.65, label="Approved", color="#2878ad")
        axis.set_title(f"{feature.replace('_', ' ').title()} Distribution")
        axis.set_xlabel(feature.replace("_", " ").title())
        axis.set_ylabel("Applicants")
        axis.legend()
    figure.tight_layout()
    figure.savefig(OUTPUT_DIR / "feature_distributions.png", dpi=160)
    plt.close(figure)

    figure, axes = plt.subplots(2, 2, figsize=(13, 9))
    for axis, feature in zip(axes.flat, FEATURES):
        bins = pd.qcut(data[feature], q=5, duplicates="drop")
        approval_rates = data.groupby(bins, observed=False)["loan_status"].mean() * 100
        approval_rates.plot(kind="bar", ax=axis, color="#2878ad")
        axis.set_title(f"Approval Rate by {feature.replace('_', ' ').title()}")
        axis.set_xlabel("Value quintile")
        axis.set_ylabel("Approved (%)")
        axis.tick_params(axis="x", rotation=35)
    figure.tight_layout()
    figure.savefig(OUTPUT_DIR / "approval_patterns.png", dpi=160)
    plt.close(figure)

    figure, axes = plt.subplots(1, 2, figsize=(13, 5))
    for status, color, label in [(0, "#a94b43", "Rejected"), (1, "#2878ad", "Approved")]:
        subset = data[data["loan_status"] == status]
        axes[0].scatter(subset["income"], subset["loan_amount"], color=color, alpha=0.75, label=label)
    axes[0].set_title("Income vs Loan Amount")
    axes[0].legend()
    for status, color, label in [(0, "#a94b43", "Rejected"), (1, "#2878ad", "Approved")]:
        subset = data[data["loan_status"] == status]
        axes[1].scatter(subset["credit_score"], subset["loan_amount"], color=color, alpha=0.75, label=label)
    axes[1].set_title("Credit Score vs Loan Amount")
    axes[1].legend()
    figure.tight_layout()
    figure.savefig(OUTPUT_DIR / "approval_relationships.png", dpi=160)
    plt.close(figure)

    figure, axis = plt.subplots(figsize=(8, 6))
    correlation = data[FEATURES + ["loan_status"]].corr()
    image = axis.imshow(correlation, cmap="Blues", vmin=-1, vmax=1)
    axis.set_xticks(range(len(correlation.columns)), correlation.columns, rotation=45, ha="right")
    axis.set_yticks(range(len(correlation.columns)), correlation.columns)
    for row in range(len(correlation)):
        for column in range(len(correlation)):
            axis.text(column, row, f"{correlation.iloc[row, column]:.2f}", ha="center", va="center")
    figure.colorbar(image, ax=axis)
    axis.set_title("Loan Dataset Correlation Matrix")
    figure.tight_layout()
    figure.savefig(OUTPUT_DIR / "correlation_heatmap.png", dpi=160)
    plt.close(figure)


dataframe = pd.read_csv(DATA_FILE)
save_data_report(dataframe)
save_visualizations(dataframe)
print(f"Saved complete data report to {REPORT_FILE}")
print(f"Saved visualizations to {OUTPUT_DIR}/")