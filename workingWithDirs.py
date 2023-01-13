from pathlib import Path

path = Path()
for fileDir in path.glob('*.py'):
    print(fileDir)