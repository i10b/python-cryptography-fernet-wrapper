PYTHON = python3

.DEFAULT_GOAL = help

help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "To upload the project to PyPI type make upload"
	@echo "To clean type make clean"	
	@echo "To run the project type make run"
	@echo "------------------------------------"

setup: clean
	${PYTHON} -m pip install -r requirements.txt

upload: clean
	${PYTHON} setup.py sdist bdist_wheel
	${PYTHON} -m twine upload dist/*

clean:
	rm --force --recursive *.pyc
	rm --force --recursive *.pyo
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info
	rm --force --recursive *.build/

run: clean
	Echo Nothing to run