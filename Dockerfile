FROM python:3.10

EXPOSE 8599

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN sed -i 's/\(runOnSave =\).*/\1 false/' .streamlit/config.toml

CMD ["streamlit", "run", "app.py"]
