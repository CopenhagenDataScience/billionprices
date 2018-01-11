defualt:
	@echo Install required packages
	@conda install --file=requirements.txt
	@echo Builds python files
	@python build_python.py
