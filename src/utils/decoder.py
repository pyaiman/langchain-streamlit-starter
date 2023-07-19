import json

def decode_response(response: str) -> dict:
    try:
        start_index = response.find("{")
        end_index = response.rfind("}")
        json_string = response[start_index:end_index + 1]
        parsed_response = json.loads(json_string)
        return parsed_response
    
    except ValueError:
        return False