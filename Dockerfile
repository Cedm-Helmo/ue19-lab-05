FROM python:3.11-slim
WORKDIR /app
COPY ../../AppData/Local/Temp/vmware-cedme/VMwareDnD/a2b5fb7f .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
