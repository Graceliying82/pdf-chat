setup:
	pip install venv pre-commit
	pre-commit install
	python -m venv venv
	source venv/bin/activate

install:
	@ pip install -r requirements.txt
	@ pip install streamlit

run:
	@python -m streamlit run app.py

clean:
	@echo "cleaning"
	@rm -rf __pycache__


.PHONY: run install clean