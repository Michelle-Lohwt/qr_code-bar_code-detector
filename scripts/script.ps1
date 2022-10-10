# Create build\lib folder
mkdir .\build\lib

# Run tox in parallel
tox -p

# Delete build\lib folder where project-egg.info file exists
python -c "from setuptools import setup; setup()" clean --all

# Remove the .coverage file created during testing
Remove-Item .\.coverage

# Remove the __pycache__ folder and its subfiles created during testing
Get-ChildItem .\tests\__pycache__\ | Remove-Item
del .\tests\__pycache__