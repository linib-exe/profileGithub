import os
import json
from django.core.wsgi import get_wsgi_application

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jsonproject.settings")
application = get_wsgi_application()

# Import your Django model
from core.models import Student  # Adjust based on your project structure

json_files_directory = '/home7/ngsaahco/profileGithub/profileGithub/Profiles'

for filename in os.listdir(json_files_directory):
    if filename.endswith(".json"):
        with open(os.path.join(json_files_directory, filename), 'r') as file:
            data = json.load(file)
            data["full_name"] = data.get("full_name", "Unknown")
            data["image"] = data.get("image", "")
            data["github_link"] = data.get("github_link", "")

            # Check if a record with the same filename already exists
            existing_record = Student.objects.filter(file_name=filename).first()

            if not existing_record:
                # If no duplicate, create and save a new record
                student_instance = Student(
                    full_name=data["full_name"],
                    image=data["image"],
                    github_link=data["github_link"],
                    file_name=filename,
                )
                student_instance.save()
