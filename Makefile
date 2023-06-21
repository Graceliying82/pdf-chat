setup:
	pip install venv
	python -m venv venv
	source venv/bin/activate


install:
	@ pip install -r requirements.txt
	@ pip install streamlit

run:
	python -m streamlit run app.py

clean:
	rm -rf __pycache__


.PHONY: run install clean