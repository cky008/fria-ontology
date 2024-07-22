import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re

# Load the similarity scores CSV
df = pd.read_csv("similarity_scores.csv")

# Drop the 'file_name' column to focus on the properties
df.drop("file_name", axis=1, inplace=True)

# Define the columns for Basic Things explicitly
basic_things_cols = [
    'report_name', 'organisation_description', 'contributor_details',
    'assessment_content', 'technology_description', 'purposes_description',
    'report_date', 'aiaaic_link'
]

# Use regex to match columns for Challenge, Evaluation, and Impact Level
challenge_cols = [col for col in df.columns if re.match(r'challenge_\d+', col)]
evaluation_cols = [col for col in df.columns if re.match(r'evaluation_\d+', col)]
impact_level_cols = [col for col in df.columns if re.match(r'impact_level_\d+', col)]

# Function to calculate average scores for a given list of columns
def calculate_average_scores(columns):
    return df[columns].mean()

# Calculate the average similarity scores for each category
avg_score_basic_things = calculate_average_scores(basic_things_cols)
avg_score_challenge = calculate_average_scores(challenge_cols)
avg_score_evaluation = calculate_average_scores(evaluation_cols)
avg_score_impact_level = calculate_average_scores(impact_level_cols)

# Plotting the bar plots
fig, axes = plt.subplots(2, 2, figsize=(20, 15))  # Two rows, two columns
fig.suptitle('Average Similarity Scores for AIAAIC Properties by Category', fontsize=16)

# Plot for Basic Things
axes[0, 0].bar(avg_score_basic_things.index, avg_score_basic_things.values)
axes[0, 0].set_title("Basic Things")
axes[0, 0].set_xlabel("Property")
axes[0, 0].set_ylabel("Average Score")
axes[0, 0].set_xticks(range(len(avg_score_basic_things.index)))
axes[0, 0].set_xticklabels(avg_score_basic_things.index, rotation=45, ha="right")

# Plot for Challenge
axes[0, 1].bar(challenge_cols, avg_score_challenge[challenge_cols])
axes[0, 1].set_title("Challenge")
axes[0, 1].set_xlabel("Property")
axes[0, 1].set_ylabel("Average Score")
axes[0, 1].set_xticks(range(len(challenge_cols)))
axes[0, 1].set_xticklabels(challenge_cols, rotation=45, ha="right")

# Plot for Evaluation
axes[1, 0].bar(evaluation_cols, avg_score_evaluation[evaluation_cols])
axes[1, 0].set_title("Evaluation")
axes[1, 0].set_xlabel("Property")
axes[1, 0].set_ylabel("Average Score")
axes[1, 0].set_xticks(range(len(evaluation_cols)))
axes[1, 0].set_xticklabels(evaluation_cols, rotation=45, ha="right")

# Plot for Impact Level
axes[1, 1].bar(impact_level_cols, avg_score_impact_level[impact_level_cols])
axes[1, 1].set_title("Impact Level")
axes[1, 1].set_xlabel("Property")
axes[1, 1].set_ylabel("Average Score")
axes[1, 1].set_xticks(range(len(impact_level_cols)))
axes[1, 1].set_xticklabels(impact_level_cols, rotation=45, ha="right")

# Adjust layout and save plot
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('average_similarity_scores.png')
plt.show()

# Sorting the averages for heatmaps
avg_score_basic_things_sorted = avg_score_basic_things.sort_values(ascending=False)
avg_score_challenge_sorted = avg_score_challenge.sort_values(ascending=False)
avg_score_evaluation_sorted = avg_score_evaluation.sort_values(ascending=False)
avg_score_impact_level_sorted = avg_score_impact_level.sort_values(ascending=False)

# Plotting the heatmaps
fig, axes = plt.subplots(2, 2, figsize=(24, 16))  # Two rows, two columns
fig.suptitle('Average Similarity Scores Heatmaps for AIAAIC Properties by Category', fontsize=16)

# Heatmap for Basic Things
sns.heatmap(avg_score_basic_things_sorted.to_frame().transpose(), annot=True, cmap="coolwarm", ax=axes[0, 0])
axes[0, 0].set_title("Basic Things")
axes[0, 0].set_xticklabels(axes[0, 0].get_xticklabels(), rotation=45, ha="right")

# Heatmap for Challenge
sns.heatmap(avg_score_challenge_sorted.to_frame().transpose(), annot=True, cmap="coolwarm", ax=axes[0, 1])
axes[0, 1].set_title("Challenge")
axes[0, 1].set_xticklabels(axes[0, 1].get_xticklabels(), rotation=45, ha="right")

# Heatmap for Evaluation
sns.heatmap(avg_score_evaluation_sorted.to_frame().transpose(), annot=True, cmap="coolwarm", ax=axes[1, 0])
axes[1, 0].set_title("Evaluation")
axes[1, 0].set_xticklabels(axes[1, 0].get_xticklabels(), rotation=45, ha="right")

# Heatmap for Impact Level
sns.heatmap(avg_score_impact_level_sorted.to_frame().transpose(), annot=True, cmap="coolwarm", ax=axes[1, 1])
axes[1, 1].set_title("Impact Level")
axes[1, 1].set_xticklabels(axes[1, 1].get_xticklabels(), rotation=45, ha="right")

# Adjust layout and save plot
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('average_similarity_heatmaps.png')
plt.show()

# Calculate the average similarity score for each incident
avg_score_by_incident = df.mean(axis=1)

# Plotting the average similarity score by incident (line plot)
plt.figure(figsize=(12, 6))
avg_score_by_incident.plot(kind="line", marker="o")
plt.title("Average Similarity Scores by Incident")
plt.xlabel("Incident")
plt.ylabel("Average Score")
plt.grid(True)
plt.tight_layout()
plt.savefig('average_similarity_by_incident.png')
plt.show()
