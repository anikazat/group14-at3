# DSP - AT3 - Group 14

## Description
This interactive web application uses streamlit to perform exploratory data analysis (EDA) on a csv file. The application is containerised with Docker and uses python 3.8.2.

The web application will be composed of 4 different sections:
1. Overall information of the dataset
2. Information on each numeric column
3. Information on each text column
4. Information on each datetime column

## Authors
Anika Zatschler, Junjie Hua, Ezgi Kanli, Mingpeng Wang

## Structure
```
├── Dockerfile
├── README.md
├── requirements.txt
├── app
│   └── streamlit_app.py
└── src
    ├── __init__.py
    ├── data.py
    ├── datetime.py
    ├── numeric.py
    ├── text.py
    └── test
        ├── test_data.py
        ├── test_datetime.py
        ├── test_numeric.py
        └── test_text.py
```


## Instructions
To run this application:

1. If you do not already have Docker installed, follow the download and install [instructions](https://docs.docker.com/get-docker/) for your operating system

2. Open your command-line terminal and clone this repository to your local computer using the following command

`git clone https://github.com/anikazat/group14-at3.git`

3. Navigate to the folder of this cloned repository using:

`cd group14-at3`

4. When your current directory is 'group14-at3', build the Docker image using:

`docker build -t streamlit_at3:latest .`

5. Once the image is built, run the image using:

`docker run -dit --rm --name at3 -p 8501:8501 -v "${PWD}":/app streamlit_at3:latest`

6. To check that it is running properly, you can list all the running containers using:

`docker ps`

7. Open http://localhost:8501/ in your browser and then upload a csv file (either drag and drop or use the 'Browse files' button)

8. Once you are finished using the application, stop the running container using:

`docker stop at3`


