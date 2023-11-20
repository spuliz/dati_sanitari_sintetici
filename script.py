from openai import OpenAI
import os
from dotenv import load_dotenv
import random

# Load environment variables from .env file
load_dotenv()

client = OpenAI()


#Function to read template
def read_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()

template = read_template('example.xml')

# Function to generate fake patient CDA data
def generate_patient_data():
    OpenAI.api_key = os.getenv('OPENAI_API_KEY')
    response = client.chat.completions.create(
    model="gpt-4-0613",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. This is an example of Italian CDA health record for a random patient. Example:{template}"},
        {"role": "user", "content": "Generate a new CDA record in XML, for a new Italian patient. Be creative add many details and populare always with many new details and information about the clinical history. Do not add any additional comment, provide only the answer in XML. Answer in Italian"},
        {"role": "assistant", "content": "Risposta:"},
    ]
    )
    print(response)
    return response.choices[0].message.content

def remove_first_last_line(xml_content):
    # Split the XML content into lines
    lines = xml_content.strip().split('\n')

    # Check if the first line contains ```xml and remove it
    if lines[0].strip() == "```xml":
        lines = lines[1:]

    # Check if the last line contains ``` and remove it
    if lines[-1].strip() == "```":
        lines = lines[:-1]

    # Join the lines back into a single string
    return '\n'.join(lines)

# Function to save data to a file with a random number in the file name
def save_to_file(patient_data, base_file_name, folder="dati"):
    processed_data = remove_first_last_line(patient_data)
    # Generate a random number
    random_number = random.randint(1, 1000000)  # You can adjust the range as needed

    # Create a new file name with the random number
    new_file_name = f"{base_file_name}_{random_number}.xml"
    
    file_path = os.path.join(folder, new_file_name)

    # Write the patient data to the new file
    with open(file_path, 'w') as file:
        file.write(processed_data)

    return new_file_name

# Function to push files to GitHub
def push_to_github(file_name, repo_path, commit_message):
    repo = git.Repo(repo_path)
    repo.git.add(file_name)
    repo.git.commit(m='-m "{}"'.format(commit_message))
    repo.git.push()

# Main script
if __name__ == "__main__":
    # Generate fake patient data
    patient_data = generate_patient_data()
    # File details
    base_file_name = "patient_cda"  # Without .xml
    file_name_with_random_number = save_to_file(patient_data, base_file_name)
    # print(f"Data saved in: {file_name_with_random_number}")