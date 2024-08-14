import json

# Path to the file
file_path = r"C:\VietnameseEnglishIdiomsProverbsDataset\VEIPD.jsonp"

# Function to load JSONP file and parse the JSON content
def load_jsonp(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the file content and remove any non-JSON parts
        content = file.read()
        json_content = content.strip('callback();')
        
        # Parse the JSON data
        data = json.loads(json_content)
        
        # Convert the list of dictionaries into a dictionary structure
        dictionary = {entry["vi"]: entry["en"] for entry in data}
        
        return dictionary

# Load the data into a dictionary
dictionary = load_jsonp(file_path)

# Print the resulting dictionary
print(dictionary)
