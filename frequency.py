import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load datasets
gpt_df = pd.read_csv("gpt_to_analysis_data_s.csv")
claude_df = pd.read_csv("claude_to_analysis_data_s.csv")

# Remove the first column (event number)
FRIA_gpt = gpt_df.drop(gpt_df.columns[0], axis=1)
FRIA_claude = claude_df.drop(claude_df.columns[0], axis=1)

# Print the contents of the challenge_12 column
# print("GPT challenge_12 data:")
# print(FRIA_gpt['challenge_12'])
#
# print("Claude challenge_12 data:")
# print(FRIA_claude['challenge_12'])

# Calculate the frequency of each value
def calculate_value_frequencies(df):
    freq_1 = (df >= 0.6).sum()
    freq_0_5 = ((df >= 0.45) & (df < 0.6)).sum()
    freq_0 = (df < 0.45).sum()
    return pd.DataFrame({'1': freq_1, '0.5': freq_0_5, '0': freq_0})

freq_gpt = calculate_value_frequencies(FRIA_gpt)
freq_claude = calculate_value_frequencies(FRIA_claude)

# Prepare plot data
properties = freq_gpt.index
n_properties = len(properties)
bar_width = 0.35

# Create chart
fig, ax = plt.subplots(figsize=(20, 10))

# Define new color scheme
gpt_colors = ['#1995AD', '#5CB3C1', '#A1D6E2']  # Blue-green series remains unchanged
claude_colors = ['#c04851', '#f07c82', '#eeb8c3']  # Deepened yellow series

# GPT data
gpt_bottom = np.zeros(n_properties)
for value, color in zip(['1', '0.5', '0'], gpt_colors):
    ax.bar(np.arange(n_properties), freq_gpt[value], bar_width,
           bottom=gpt_bottom, label=f'GPT {value}', color=color, alpha=0.8)
    gpt_bottom += freq_gpt[value]

# Claude data
claude_bottom = np.zeros(n_properties)
for value, color in zip(['1', '0.5', '0'], claude_colors):
    ax.bar(np.arange(n_properties) + bar_width, freq_claude[value], bar_width,
           bottom=claude_bottom, label=f'Claude {value}', color=color, alpha=0.8)
    claude_bottom += freq_claude[value]

# Set chart properties
ax.set_xlabel('Property', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)
ax.set_title('GPT vs Claude Annotation Distribution', fontsize=16)
ax.set_xticks(np.arange(n_properties) + bar_width / 2)
ax.set_xticklabels(properties, rotation=90)

# Add legend
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.savefig('combined_annotation_distribution.pdf')
plt.show()

# Draw a clearer chart
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 16))

freq_gpt.plot(kind='bar', stacked=True, ax=ax1)
ax1.set_title("GPT Annotation Distribution")
ax1.set_xlabel("Property")
ax1.set_ylabel("Frequency")
ax1.legend(title="Value")

freq_claude.plot(kind='bar', stacked=True, ax=ax2)
ax2.set_title("Claude Annotation Distribution")
ax2.set_xlabel("Property")
ax2.set_ylabel("Frequency")
ax2.legend(title="Value")

plt.tight_layout()
plt.savefig('annotation_distribution.pdf')
plt.show()

# Heatmap section
import seaborn as sns

# Create heatmap function
def create_heatmap(value):
    # Combine GPT and Claude data
    combined_data = pd.DataFrame({
        'GPT': freq_gpt[value],
        'Claude': freq_claude[value]
    })

    plt.figure(figsize=(10, 20))  # Increase the height of the figure
    ax = sns.heatmap(combined_data, annot=True, cmap="viridis", fmt='g')
    plt.title(f"GPT vs Claude Annotation Comparison Heatmap for Value {value}")

    # Adjust y-axis labels
    plt.yticks(rotation=0)  # Make y-axis labels horizontal
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=8)  # Reduce font size

    # If labels still overlap, try showing only some labels
    # Show every nth label
    # n = 2  # Adjust as needed
    # for i, label in enumerate(ax.get_yticklabels()):
    #     if i % n != 0:
    #         label.set_visible(False)

    plt.tight_layout()
    plt.savefig(f'annotation_heatmap_{value}.pdf', dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()

# Create heatmap for each value
for value in ['1', '0.5', '0']:
    create_heatmap(value)

print("Heatmaps have been generated and saved.")
