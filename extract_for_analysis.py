import os
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 定义目录路径和文件名模式
directory = "./instances"
claude_file_pattern = "fria-instance-claude-"
gpt_file_pattern = "fria-instance-gpt-"
file_indices = range(1, 51)

# 初始化数据字典
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
        for j in range(1, 7 if i in [1, 4] else 4 if i == 2 else 3):
            data_dict[f"challenge_{i}{j}"] = []
            data_dict[f"evaluation_{i}{j}"] = []
            data_dict[f"impact_level_{i}{j}"] = []
    return data_dict

claude_data = initialize_data_dict()
gpt_data = initialize_data_dict()

# 定义正则表达式模式
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

# 检查默认内容
def is_default_content(text, default_keywords):
    return any(keyword in text for keyword in default_keywords)

# 计算文本相似性
def compute_similarity(text, reference_text):
    if text is None or reference_text is None:
        return 0
    vectorizer = TfidfVectorizer().fit_transform([text, reference_text])
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity(vectors)
    return cosine_sim[0, 1]

# 定义函数提取信息并计算相似性得分
def extract_information(content, reference_texts):
    default_keywords = ["evaluation content", "impact level content"]
    extracted_info = {key: None for key in basic_things_patterns.keys()}
    for key, pattern in basic_things_patterns.items():
        match = re.search(pattern, content)
        if match:
            value = match.group(1).strip()
            if value:
                extracted_info[key] = 1
            else:
                extracted_info[key] = 0.5
        else:
            extracted_info[key] = 0

    challenges = re.findall(challenge_pattern, content)
    evaluations = re.findall(evaluation_pattern, content)
    impact_levels = re.findall(impact_level_pattern, content)

    for i in range(1, 5):
        for j in range(1, 7 if i in [1, 4] else 4 if i == 2 else 3):
            extracted_info[f"challenge_{i}{j}"] = 0
            extracted_info[f"evaluation_{i}{j}"] = 0
            extracted_info[f"impact_level_{i}{j}"] = 0

    for challenge in challenges:
        challenge_id = re.search(r'fria:FRIA-reportChallenge(\d+)', challenge).group(1)
        comment_match = re.search(r'rdfs:comment "(.*?)"', challenge)
        challenge_text = comment_match.group(1).strip() if comment_match else None
        evaluation_id = re.search(r'fria:FRIA-reportEvaluation(\d+)', challenge)
        evaluation_text = evaluations.pop(0).strip() if evaluations else None
        impact_level_text = impact_levels.pop(0).strip() if impact_levels else None

        challenge_key = f"challenge_{challenge_id[:1]}{challenge_id[1:]}" if len(challenge_id) > 1 else f"challenge_{challenge_id}"
        evaluation_key = f"evaluation_{challenge_id[:1]}{challenge_id[1:]}" if len(challenge_id) > 1 else f"evaluation_{challenge_id}"
        impact_level_key = f"impact_level_{challenge_id[:1]}{challenge_id[1:]}" if len(challenge_id) > 1 else f"impact_level_{challenge_id}"

        extracted_info[challenge_key] = compute_similarity(challenge_text, reference_texts[challenge_key])
        extracted_info[evaluation_key] = 1 if evaluation_text and not is_default_content(evaluation_text, default_keywords) else 0.5 if evaluation_id else 0
        extracted_info[impact_level_key] = 1 if impact_level_text and not is_default_content(impact_level_text, default_keywords) else 0.5 if evaluation_id else 0

    return extracted_info

# 定义参考文本
reference_texts = {
    "challenge_11": "The AI system does not communicate that a decision/advice or outcome is the result of an algorithmic decision.",
    "challenge_12": "The AI system does not provide percentages or other indication on the degree of likelihood that the outcome is correct/incorrect, prejudicing the user that there is no possibility of error and therefore that the outcome is undoubtedly incriminating.",
    "challenge_13": "The AI system produces an outcome that forces a reversal of burden of proof upon the suspect, by presenting itself as an absolute truth, practically depriving the defence of any chance to counter it.",
    "challenge_14": "There is no explanation of reasons and criteria behind a certain output of the AI system that the user can understand.",
    "challenge_15": "There is no indication of the extent to which the AI system influences the overall decision-making process.",
    "challenge_16": "There is no set of measures that allow for redress in case of the occurrence of any harm or adverse impact.",
    "challenge_21": "The AI system targets members of a specific social group.",
    "challenge_22": "There are no mechanisms to flag and correct issues related to bias, discrimination, or poor performance.",
    "challenge_23": "The AI system does not consider the diversity and representativeness for specific population or problematic use cases.",
    "challenge_31": "There is no mechanism to limit the deployment of the AI system to suspected individuals.",
    "challenge_32": "The data stored, recorded, and produced are not easily accessible to concerned individuals.",
    "challenge_41": "There are no mechanisms for the user to exercise control over the processing of personal data.",
    "challenge_42": "There are no measures to ensure the lawfulness of the processing of personal data.",
    "challenge_43": "There are no procedures to limit the access to personal data and to the extent and amount necessary for those purposes.",
    "challenge_44": "There is no mechanism allowing to comply with the exercise of data subject’s rights (access, rectification and erasure of data relating to a specific individual).",
    "challenge_45": "There are no specific measures in place to enhance the security of the processing of personal data (via encryption, anonymisation and aggregation).",
    "challenge_46": "There is no procedure to conduct a data protection impact assessment.",
    # Add additional reference texts as needed...
}

# 处理文件并提取信息
for pattern, data_dict in [(claude_file_pattern, claude_data), (gpt_file_pattern, gpt_data)]:
    for i in file_indices:
        file_name = f"{pattern}{i}.ttl"
        file_path = os.path.join(directory, file_name)

        if not os.path.exists(file_path):
            continue

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        extracted_info = extract_information(content, reference_texts)

        data_dict["file_name"].append(file_name)
        for key in basic_things_patterns.keys():
            data_dict[key].append(extracted_info[key])
        for i in range(1, 5):
            for j in range(1, 7 if i in [1, 4] else 4 if i == 2 else 3):
                data_dict[f"challenge_{i}{j}"].append(extracted_info[f"challenge_{i}{j}"])
                data_dict[f"evaluation_{i}{j}"].append(extracted_info[f"evaluation_{i}{j}"])
                data_dict[f"impact_level_{i}{j}"].append(extracted_info[f"impact_level_{i}{j}"])

# 确保所有列表长度一致
def ensure_list_lengths(data_dict):
    max_length = max(len(lst) for lst in data_dict.values())
    for key in data_dict:
        while len(data_dict[key]) < max_length:
            data_dict[key].append(None)

# 确保数据字典中的所有列表长度一致
ensure_list_lengths(claude_data)
ensure_list_lengths(gpt_data)

# 转换为DataFrame
claude_df = pd.DataFrame(claude_data)
gpt_df = pd.DataFrame(gpt_data)

# # 删除指定的无用列
# columns_to_drop = [
#     "challenge_1", "evaluation_1", "impact_level_1",
#     "challenge_2", "evaluation_2", "impact_level_2",
#     "challenge_3", "evaluation_3", "impact_level_3",
#     "challenge_4", "evaluation_4", "impact_level_4",
# ]
#
# claude_df.drop(columns=columns_to_drop, inplace=True)
# gpt_df.drop(columns=columns_to_drop, inplace=True)

# 将challenge列中的值限制在0到1之间
challenge_columns = [col for col in claude_df.columns if col.startswith('challenge_')]
claude_df[challenge_columns] = claude_df[challenge_columns].clip(lower=0, upper=1)
gpt_df[challenge_columns] = gpt_df[challenge_columns].clip(lower=0, upper=1)

# 保存为CSV文件
claude_output_file = "claude_to_analysis_data_s.csv"
gpt_output_file = "gpt_to_analysis_data_s.csv"
claude_df.to_csv(claude_output_file, index=False)
gpt_df.to_csv(gpt_output_file, index=False)

# 打印DataFrame
print("Claude DataFrame:")
print(claude_df)
print("\nGPT DataFrame:")
print(gpt_df)
