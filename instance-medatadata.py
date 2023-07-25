import requests
import json

def get_instance_metadata():
    base_url = "http://169.254.169.254/latest/meta-data/"
    metadata = {}
    
    # Add more keys as needed to retrieve additional metadata
    keys_to_retrieve = [
        "ami-id",
        "instance-id",
        "instance-type",
        "local-ipv4",
        "public-ipv4",
        "security-groups",
        # Add more keys here if needed
    ]
    
    for key in keys_to_retrieve:
        url = base_url + key
        response = requests.get(url)
        if response.status_code == 200:
            metadata[key] = response.text
        else:
            metadata[key] = "N/A"
    
    return metadata

if __name__ == "__main__":
    instance_metadata = get_instance_metadata()
    json_output = json.dumps(instance_metadata, indent=2)
    print(json_output)
