FROM nvidia/cuda:12.6.2-cudnn-devel-ubuntu22.04

RUN sudo apt-get install -y python3-docker
RUN sudo apt-get install -y python3-pip

WORKDIR /app

COPY ./telegram/requirements.txt tele-reqs.txt
COPY ../requirements.txt pozd-reqs.txt

RUN pip3 install -r tele-reqs.txt
RUN pip3 install -r pozd-reqs.txt
RUN pip3 install --upgrade torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu121

COPY ./telegram ./telegram
COPY ./pozdnyakov ./telegram/pozdnyakov

CMD ["python", "telegram/main.py"]
