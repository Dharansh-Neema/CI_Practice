#origin
FROM python:3.9-slim

#Set the working dir in container
WORKDIR /app

#copy the content from source to destination
COPY app.py /app/

#Run and install the dependency
RUN pip install --no-cache-dir streamlit

#Expose the port 
EXPOSE 8501

#CMD to execute the streamlit application
ENTRYPOINT ["streamlit","run","app.py"]