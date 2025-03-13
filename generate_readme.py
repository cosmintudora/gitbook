import yaml  # Import PyYAML
import json

# Load OpenAPI YAML

# manifest (or anything else file) with a for loop 
with open("pets/openapi.yaml", "r") as f:
    openapi = yaml.safe_load(f)  # Convert YAML to Python dictionary

readme_content = "# API Documentation\n\n"

# Iterate over all paths in OpenAPI
for path, methods in openapi.get("paths", {}).items():
    for method, details in methods.items():
        # Format the method and path in the openapi tag
        readme_content += f"{{% openapi src=\"./openapi.yaml\" path=\"{path}\" method=\"{method}\" expanded=\"true\" %}}\n"
        readme_content += f"{{% endopenapi %}}\n\n"

# Write the updated README.md
with open("pets/README.md", "w") as f:
    f.write(readme_content)

print("README.md updated successfully!")
