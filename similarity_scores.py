import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re


def extract_impact_level(sentence):
    if pd.isna(sentence):
        return None
    sentence = str(sentence).lower()  # 转换为小写
    levels = ["low", "medium", "high", "very high"]
    for level in levels:
        if re.search(r'\b' + level + r'\b', sentence):
            return level
    return None


def calculate_similarity(text1, text2):
    if pd.isna(text1) or pd.isna(text2):
        return 0.0
    text1, text2 = str(text1).lower(), str(text2).lower()  # 转换为小写
    if not text1.strip() or not text2.strip():
        return 0.0
    vectorizer = TfidfVectorizer(lowercase=True)
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]


def impact_similarity_score(sentence1, sentence2):
    if pd.isna(sentence1) or pd.isna(sentence2):
        return 0.0
    sentence1, sentence2 = str(sentence1).lower(), str(sentence2).lower()  # 转换为小写
    level1 = extract_impact_level(sentence1)
    level2 = extract_impact_level(sentence2)

    if level1 and level2:
        levels = ["low", "medium", "high", "very high"]
        if level1 == level2:
            return 1.0
        else:
            distance = abs(levels.index(level1) - levels.index(level2))
            return 1.0 - (distance / (len(levels) - 1))

    text_similarity = calculate_similarity(sentence1, sentence2)

    if not level1 and not level2:
        return text_similarity

    return text_similarity * 0.5


def compare_csv_files(file1, file2):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    result = pd.DataFrame(columns=df1.columns)

    for col in df1.columns:
        if col == 'file_name':
            result[col] = [f'fria-report-{i + 1}' for i in range(len(df1))]
        elif col == 'report_date':
            result[col] = df1[col].eq(df2[col]).astype(float)
        elif 'impact_level' in col:
            result[col] = df1[col].combine(df2[col], impact_similarity_score)
        else:
            result[col] = df1[col].combine(df2[col], calculate_similarity)

    return result


# 使用函数
gpt_file = 'gpt_extracted_data.csv'
claude_file = 'claude_extracted_data.csv'

similarity_result = compare_csv_files(gpt_file, claude_file)

# 保存结果
similarity_result.to_csv('similarity_scores.csv', index=False)

print(f'Similarity scores saved to similarity_results.csv')
