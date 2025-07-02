import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg before importing pyplot

# Enable high-resolution display
plt.rcParams['figure.dpi'] = 1080
plt.rcParams['savefig.dpi'] = 780

# Sales data
data = {
    "Month": [
        "2024-01", "2024-02", "2024-03", "2024-04", "2024-05", "2024-06",
        "2024-07", "2024-08", "2024-09", "2024-10", "2024-11", "2024-12"
    ],
    "Sales": [
        200, 1000, 4000, 2000, 212, 400,
        2199, 500, 5000, 3000, 200, 5000
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)
df["Month"] = pd.to_datetime(df["Month"])

mean_value = df["Sales"].mean()
median_value = df["Sales"].median()
mode_value = df["Sales"].mode()[0]
standard_deviation = df["Sales"].std()

# Probability of next year sales
pdf = df["Sales"].div(df["Sales"].sum())

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Standard Deviation: {standard_deviation}")
print(f"Probability Density Function: {pdf}")

# # Create the plot
# plt.figure(figsize=(12, 6))
# plt.plot(df["Month"], df["Sales"], marker='0', linestyle='-', linewidth=2, markersize=8)
#
# # Customize the plot
# plt.title("Monthly Sales", fontsize=14, pad=20)
# plt.xlabel("2024", fontsize=12, labelpad=15)
# plt.ylabel("Sales", fontsize=12, labelpad=15)
# plt.grid(True, linestyle='-', alpha=0.4)
#
# # Rotate x-axis labels for better readability
# plt.xticks(rotation=50)
#
# # Format y-axis labels
# plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${int(x):,}'))
#
# # Adjust layout to prevent label cutoff
# plt.tight_layout()
#
# # Save the plot to a file instead of showing it
# plt.savefig('sales_plot.png',)
