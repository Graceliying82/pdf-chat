setup:
	pip install pre-commit
	pre-commit install
	python -m venv venv
	source venv/bin/activate


	pre-commit autoupdate



install:
	@ pip install -r requirements.txt
	@ pip install streamlit

run:
	@python -m streamlit run app.py

clean:
	@echo "cleaning"
	@rm -rf __pycache__


.PHONY: run install clean
