from werkzeug.utils import secure_filename

# Define the original filename
original_filename = "Book1.xlsx"

# Sanitize the filename using secure_filename
sanitized_filename = secure_filename(original_filename)

# Now, 'sanitized_filename' contains a safe and sanitized version of the original filename
print(sanitized_filename)
