import toml

pyproject = toml.load('pyproject.toml')
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
if 'project' not in pyproject:
    pyproject['project'] = {}
pyproject['project']['dependencies'] = requirements
with open('pyproject.toml', 'w') as f:
    toml.dump(pyproject, f)

print('Updated pyproject.toml with dependencies from requirements.txt')