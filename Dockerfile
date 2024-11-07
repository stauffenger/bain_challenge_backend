FROM python:3.12

WORKDIR /build_dir/

COPY . /build_dir/

RUN python -m pip install -r requirements.txt && \
    pyinstaller --onefile --distpath /bin/ --name bain_challenge app.py

ENTRYPOINT ["bain_challenge"]