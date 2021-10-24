# group14-at3
DSP AT3 - Group 14

## Setting up Streamlit with Docker
If you're a bit unsure about setting up streamlit for this assignment, here is the code that I used in terminal:

```
> docker build -t streamlit_at3:latest .

# To start/run it
> docker run -dit --rm --name at3_2 -p 8501:8501 -v "${PWD}":/app streamlit_at3:latest

> docker ps

# To stop it (once you're finished working)
> docker stop at3_2

> docker ps
```

- Anika


---------------------------
Ezgi:
When I run  below command;
docker build -t streamlit_at3:latest .

ezgikanli@Ezgis-MacBook-Air ~ % docker build -t streamlit_at3:latest .
[+] Building 0.0s (2/2) FINISHED                                                
 => ERROR [internal] load build definition from Dockerfile                 0.1s
 => => transferring dockerfile: 40B                                        0.0s
 => ERROR [internal] load .dockerignore                                    0.0s
 => => transferring context: 40B                                           0.0s
------
 > [internal] load build definition from Dockerfile:
------
------
 > [internal] load .dockerignore:
------
failed to solve with frontend dockerfile.v0: failed to read dockerfile: error from sender: open .Trash: operation not permitted


Thoughts?
-------------------------------






