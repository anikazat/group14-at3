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
