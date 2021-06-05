from pathlib import Path

path = Path("C:\\Users\\Admin\\OneDrive\\Desktop\\aditya\\pythondir\\basicProgramms")
print(path)
for file in path.glob('*.py'):
    print(file)

