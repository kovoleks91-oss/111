import os

# Папки, які не потрібно відображати
EXCLUDE_DIRS = {'.venv', '__pycache__', '.idea', '.git'}

# Файл для збереження структури
OUTPUT_FILE = "../tree.txt"

def generate_tree(root_dir="."):
    lines = []

    for root, dirs, files in os.walk(root_dir):
        # Відфільтровуємо службові директорії
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        level = root.replace(root_dir, "").count(os.sep)
        indent = "│   " * (level - 1) + ("├── " if level > 0 else "")
        lines.append(f"{indent}{os.path.basename(root) or root}/")

        sub_indent = "│   " * level + "├── "
        for f in files:
            lines.append(f"{sub_indent}{f}")

    return "\n".join(lines)

if __name__ == "__main__":
    print("🔍 Генеруємо структуру проєкту...")
    tree_output = generate_tree("..")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(tree_output)

    print(f"✅ Структуру проєкту збережено у файл '{OUTPUT_FILE}'")
