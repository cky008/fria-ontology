import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets with updated paths
gpt_df = pd.read_csv("gpt_to_analysis_data_s.csv")
claude_df = pd.read_csv("claude_to_analysis_data_s.csv")

# Drop the first column (incident number) from each dataframe
FRIA_gpt = gpt_df.drop(gpt_df.columns[0], axis=1)
FRIA_claude = claude_df.drop(claude_df.columns[0], axis=1)


# Calculate frequencies for each dataset
freq_FRIA_gpt = FRIA_gpt.sum()
freq_FRIA_claude = FRIA_claude.sum()


# Combine frequencies into a single DataFrame
frequencies = pd.DataFrame(
    {
        "FRIA_GPT": freq_FRIA_gpt,
        "FRIA_Claude": freq_FRIA_claude,

    }
)

# Plotting frequencies for each LLM and ontology
frequencies.plot(kind="bar", figsize=(5, 5))
plt.title("Frequency of Annotations Across LLMs and Ontologies")
plt.xlabel("Property")
plt.ylabel("Frequency")
plt.gcf().set_size_inches(20, 8)  # 设置图形尺寸为 10x8 英寸
plt.savefig('1.png')
plt.show()

# 查看行标签
row_labels = frequencies.index

sns.heatmap(frequencies, annot=True, cmap="viridis")
plt.title("Heatmap of Annotation Frequencies")
plt.yticks(range(len(row_labels)), row_labels)  # 使用自定义的行标签
plt.tight_layout()
plt.gcf().set_size_inches(10, 24)  # 设置图形尺寸为 10x8 英寸
plt.savefig('2.png')
plt.show()
