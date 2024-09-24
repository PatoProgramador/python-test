def validate_presence(key):
    def validator(data):
        if key not in data or not data[key]:
            raise ValueError(f"{key} is required")
    return validator

def validate_number(key):
    def validator(data):
        if key in data and not isinstance(data[key], (int, float)):
            raise ValueError(f"{key} must be a number")
    return validator

validators = [
    validate_presence('title'),
    validate_presence('author'),
    validate_presence('year'),
    validate_number('year')
]

def validate_request(data):
    for validator in validators:
        validator(data)
