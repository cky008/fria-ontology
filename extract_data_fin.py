import os
import re
import pandas as pd

# Define the directory and file patterns
directory = "./instances"
claude_file_pattern = "fria-instance-claude-"
gpt_file_pattern = "fria-instance-gpt-"
file_indices = range(1, 51)


# Initialize the data dictionary
def initialize_data_dict():
    data_dict = {
        "file_name": [],
        "report_name": [],
        "organisation_description": [],
        "contributor_details": [],
        "assessment_content": [],
        "technology_description": [],
        "purposes_description": [],
        "report_date": [],
        "aiaaic_link": []
    }
    for i in range(1, 5):
        data_dict[f"challenge_{i}"] = []
        data_dict[f"evaluation_{i}"] = []
        data_dict[f"impact_level_{i}"] = []
        for j in range(1, 7 if i in [1, 4] else 4 if i == 2 else 3):
            data_dict[f"challenge_{i}{j}"] = []
            data_dict[f"evaluation_{i}{j}"] = []
            data_dict[f"impact_level_{i}{j}"] = []
    return data_dict


claude_data = initialize_data_dict()
gpt_data = initialize_data_dict()

# Define the regular expressions for extracting information
basic_things_patterns = {
    "report_name": re.compile(r'fria:hasReportName "(.*?)" ;'),
    "organisation_description": re.compile(r'fria:hasOrganisationPositionDescription "(.*?)" ;'),
    "contributor_details": re.compile(r'fria:hasContributorDetails "(.*?)" ;'),
    "assessment_content": re.compile(r'fria:hasAssessmentContent "(.*?)" ;'),
    "technology_description": re.compile(r'fria:hasTechnologyAndDataDescription "(.*?)" ;'),
    "purposes_description": re.compile(r'fria:hasPurposesAndContextDescription "(.*?)" ;'),
    "report_date": re.compile(r'fria:reportDate "(.*?)"'),
    "aiaaic_link": re.compile(r'fria:hasAIAAICLink\s+"(.*?)"\s*[;.]')
}
challenge_pattern = re.compile(
    r'(fria:FRIA-reportChallenge\d+ a (?:fria:FRIA-reportChallenge|rdfs:Class) ;\s*fria:FRIA-reporthasEvaluation fria:FRIA-reportEvaluation\d+ ;\s*fria:FRIA-reporthasImpactLevel fria:FRIA-reportImpactLevel\d+ ;.*?)(?=fria:FRIA-reportChallenge|$)',
    re.DOTALL)

evaluation_pattern = re.compile(r'fria:hasEvaluationContent "(.*?)" \.', re.DOTALL)
impact_level_pattern = re.compile(r'fria:hasImpactLevelContent "(.*?)" \.', re.DOTALL)


# Define the function to extract information
def extract_information(content):
    extracted_info = {key: None for key in basic_things_patterns.keys()}
    for key, pattern in basic_things_patterns.items():
        match = re.search(pattern, content)
        extracted_info[key] = match.group(1) if match else None

    challenges = re.findall(challenge_pattern, content)
    evaluations = re.findall(evaluation_pattern, content)
    impact_levels = re.findall(impact_level_pattern, content)

    for i in range(1, 5):
        extracted_info[f"challenge_{i}"] = None
        extracted_info[f"evaluation_{i}"] = None
        extracted_info[f"impact_level_{i}"] = None
        for j in range(1, 7 if i in [1, 4] else 4 if i == 2 else 3):
            extracted_info[f"challenge_{i}{j}"] = None
            extracted_info[f"evaluation_{i}{j}"] = None
            extracted_info[f"impact_level_{i}{j}"] = None

    for challenge in challenges:
        challenge_id = re.search(r'fria:FRIA-reportChallenge(\d+)', challenge).group(1)
        comment_match = re.search(r'rdfs:comment "(.*?)"', challenge)
        challenge_text = comment_match.group(1) if comment_match else None
        evaluation_id = re.search(r'fria:FRIA-reportEvaluation(\d+)', challenge)
        evaluation_text = evaluations.pop(0) if evaluations else None
        impact_level_text = impact_levels.pop(0) if impact_levels else None

        if len(challenge_id) == 1:
            extracted_info[f"challenge_{challenge_id}"] = challenge_text
            extracted_info[f"evaluation_{challenge_id}"] = evaluation_text
            extracted_info[f"impact_level_{challenge_id}"] = impact_level_text
        else:
            extracted_info[f"challenge_{challenge_id[:1]}{challenge_id[1:]}"] = challenge_text
            extracted_info[f"evaluation_{challenge_id[:1]}{challenge_id[1:]}"] = evaluation_text
            extracted_info[f"impact_level_{challenge_id[:1]}{challenge_id[1:]}"] = impact_level_text

    return extracted_info


# Process the files
for pattern, data_dict in [(claude_file_pattern, claude_data), (gpt_file_pattern, gpt_data)]:
    for i in file_indices:
        file_name = f"{pattern}{i}.ttl"
        file_path = os.path.join(directory, file_name)

        if not os.path.exists(file_path):
            continue

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        extracted_info = extract_information(content)

        data_dict["file_name"].append(file_name)
        for key in basic_things_patterns.keys():
            data_dict[key].append(extracted_info[key])
        for i in range(1, 5):
            data_dict[f"challenge_{i}"].append(extracted_info[f"challenge_{i}"])
            data_dict[f"evaluation_{i}"].append(extracted_info[f"evaluation_{i}"])
            data_dict[f"impact_level_{i}"].append(extracted_info[f"impact_level_{i}"])
            for j in range(1, 7 if i in [1, 4] else 4 if i == 2 else 3):
                data_dict[f"challenge_{i}{j}"].append(extracted_info[f"challenge_{i}{j}"])
                data_dict[f"evaluation_{i}{j}"].append(extracted_info[f"evaluation_{i}{j}"])
                data_dict[f"impact_level_{i}{j}"].append(extracted_info[f"impact_level_{i}{j}"])

# Transform the data into DataFrames
claude_df = pd.DataFrame(claude_data)
gpt_df = pd.DataFrame(gpt_data)

# Delete the columns that are not needed
columns_to_drop = [
    "challenge_1", "evaluation_1", "impact_level_1",
    "challenge_2", "evaluation_2", "impact_level_2",
    "challenge_3", "evaluation_3", "impact_level_3",
    "challenge_4", "evaluation_4", "impact_level_4",
]

claude_df.drop(columns=columns_to_drop, inplace=True)
gpt_df.drop(columns=columns_to_drop, inplace=True)


# Save the DataFrames to CSV files
claude_output_file = "claude_extracted_data.csv"
gpt_output_file = "gpt_extracted_data.csv"
claude_df.to_csv(claude_output_file, index=False)
gpt_df.to_csv(gpt_output_file, index=False)

# Print Results
print("Claude DataFrame:")
print(claude_df)
print("\nGPT DataFrame:")
print(gpt_df)
