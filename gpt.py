import csv

import tiktoken
from openai import OpenAI

# Set up the OpenAI client with your API key
client = OpenAI(
    base_url="https://api.wlai.vip/v1",
    api_key="sk-OzWhpnKkKjB6n7uiF94fDe9aEe654e75B4F78d80Fd858b71",
)


# Function to read the ontology from a .ttl file
def read_ontology_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        ontology = file.read()

    # print(f'Ontology:\n{ontology}')
    return ontology


# Function to read input data from processed_data.csv
def read_input_data_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skip the header
        first_row = next(reader)  # Read the first row of data
    # print(f'Input Data:\n{first_row}')
    return first_row


# Define your prompt template
def create_prompt(input_data_part):
    prompt = f"Based on the input data part, generate a part of the FRIA report instance:\n\nInput Data Part:\n{input_data_part}\n\nFRIA Report Part:"
    # print(f"Prompt:\n{prompt}")
    return prompt


def count_tokens(text, model="gpt-4-turbo"):
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    return len(tokens)


# Function to call OpenAI's API in segments
def generate_fria_report_segmented(client, ontology, input_data, max_tokens_per_segment=5000, chunk_size=2000):
    # Split the input data into chunks
    input_data_chunks = [input_data[i:i + chunk_size] for i in range(0, len(input_data), chunk_size)]

    response_parts = []
    for input_data_part in input_data_chunks:
        try:
            prompt = create_prompt(input_data_part)
            response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": f"You will be provided with an ontology and input data. Your task is to generate a FRIA report instance based on those data. When given an incident report, find the relevant information for each part of the RDF definition and fill in the Turtle format using the information found. So you need to return Turtle representation for the incident report. Always include all of the properties in the RDF output. If there is no relevant information for a given property in the report, return a blank value in the RDF. However, if you can understand and fill in the blank value based on the available information, start the value with 'LLM understand: '. For Basic Things like fria:hasAssessmentContent, if the provided information is too long, you then need to summarize appropriately based on the content. For the date, try to access the specific AIAAIC Link and retrieve the time information, if you can't access the provided link, try to find it based on provided information. If there are some details you cannot find or understand, leave those properties blank. For the Challenges, Evaluation, and Impact Level sections, follow the guidelines provided: Review the FRIA template's pre-listed challenges, adding any system-specific ones. Evaluate each challenge's relevance to the AI system, explaining its embedding and impact within the law enforcement context. Assess the severity of prejudice and affected population to determine the overall impact level using the provided matrix. Consider the predetermined context of use, including target group, geographical area, deployment period, and trigger conditions. Provide detailed explanations for each evaluation and impact estimate. Regularly update the FRIA to reflect changes in the AI system's functioning or deployment circumstances. When evaluating the impact level, follow the guidelines provided in the prompt:1. Determine the severity of prejudice: Negligible, Critical, or Catastrophic. 2. Evaluate the number of affected individuals: Low, Medium, or High.3. Use the impact matrix to determine the overall impact level: Low, Medium, High, or Very High.**Based on the instructions provided, you can only have 4 impact level! Decide inside 4 of them(Low, Medium, High, or Very High)!!**You need to return complete RDF/Turtle representation for the incident report, including all basic things, challenges, evaluations and impact levels for each challenge.\n\nOntology:\n{ontology}"
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=max_tokens_per_segment,
                top_p=1
            )

            # Extract the generated text
            response_text = response.choices[0].message.content.strip()
            print(f'Full Response:\n{response_text}')
            response_parts.append(response_text)

            # Check if the response is complete or if more tokens are needed
            if len(response_text) < max_tokens_per_segment:
                break

        except Exception as e:
            print(f"Error occurred: {e}")
            break

    # Combine all parts of the response
    report_instance = "\n".join(response_parts)
    return report_instance


# Read ontology from .ttl file
ontology_file_path = 'fria-report.ttl'
ontology = read_ontology_from_file(ontology_file_path)

# Read input data from processed_data.csv
input_data_file_path = 'processed_data.csv'
input_data_row = read_input_data_from_csv(input_data_file_path)
input_data = " ".join(input_data_row)  # Combine input data row into a single string

# Combine ontology and input data for token count
combined_input = f"You will be provided with an ontology and input data. Your task is to generate a FRIA report instance based on those data. When given an incident report, find the relevant information for each part of the RDF definition and fill in the Turtle format using the information found. So you need to return Turtle representation for the incident report. Always include all of the properties in the RDF output. If there is no relevant information for a given property in the report, return a blank value in the RDF. However, if you can understand and fill in the blank value based on the available information, start the value with 'LLM understand: '. For Basic Things like fria:hasAssessmentContent, if the provided information is too long, you then need to summarize appropriately based on the content. For the date, try to access the specific AIAAIC Link and retrieve the time information, if you can't access the provided link, try to find it based on provided information. If there are some details you cannot find or understand, leave those properties blank. For the Challenges, Evaluation, and Impact Level sections, follow the guidelines provided: Review the FRIA template's pre-listed challenges, adding any system-specific ones. Evaluate each challenge's relevance to the AI system, explaining its embedding and impact within the law enforcement context. Assess the severity of prejudice and affected population to determine the overall impact level using the provided matrix. Consider the predetermined context of use, including target group, geographical area, deployment period, and trigger conditions. Provide detailed explanations for each evaluation and impact estimate. Regularly update the FRIA to reflect changes in the AI system's functioning or deployment circumstances. When evaluating the impact level, follow the guidelines provided in the prompt:1. Determine the severity of prejudice: Negligible, Critical, or Catastrophic. 2. Evaluate the number of affected individuals: Low, Medium, or High.3. Use the impact matrix to determine the overall impact level: Low, Medium, High, or Very High.**Based on the instructions provided, you can only have 4 impact level! Decide inside 4 of them(Low, Medium, High, or Very High)!!**You need to return complete RDF/Turtle representation for the incident report, including all basic things, challenges, evaluations and impact levels for each challenge.\n\nOntology:\n{ontology}\n\nInput Data Part:\n{input_data}\n\nFRIA Report Part:"

# Calculate total tokens
total_tokens = count_tokens(combined_input)
print(f"Total tokens: {total_tokens}")

# Generate the FRIA report instance
fria_report_instance = generate_fria_report_segmented(client, ontology, input_data)

# Output the generated FRIA report instance
print(fria_report_instance)
