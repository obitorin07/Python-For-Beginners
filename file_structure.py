## ==========================================================
##  STRUCTURE GENERATOR SCRIPT: Creates structure.txt with
##  a visual tree layout of your entire project directory
## ==========================================================

import os

# 🔧 Set your main project folder path
project_dir = r"C:\Users\kiran\OneDrive\Desktop\Python-For-Beginners"
output_file = os.path.join(project_dir, "structure.txt")

def generate_structure(directory, prefix=""):
    lines = []
    entries = sorted(os.listdir(directory))

    for index, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        is_last = index == len(entries) - 1
        connector = "└── " if is_last else "├── "

        lines.append(f"{prefix}{connector}{entry}")

        if os.path.isdir(path):
            extension = "    " if is_last else "│   "
            lines.extend(generate_structure(path, prefix + extension))

    return lines

# 📝 Generate the directory tree and write to structure.txt
with open(output_file, "w", encoding="utf-8") as f:
    f.write(f"{os.path.basename(project_dir)}\n")
    f.writelines("\n".join(generate_structure(project_dir)))

print("✅ structure.txt created successfully!")
