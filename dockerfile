FROM pytorch/pytorch:2.2.1-cuda12.1-cudnn8-devel

#docker-composeから環境変数の引数を受け取る
ARG http_tmp
ARG https_tmp

#環境変数を環境に設定
ENV http_proxy=$http_tmp
ENV https_proxy=$https_tmp

#llama-cppでgpuを使うための環境変数
ENV CMAKE_ARGS="-DLLAMA_CUBLAS=on"
ENV FORCE_CMAKE=1

#タイムゾーンを東京に設定
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#apt関連の設定
RUN apt update -y && apt upgrade -y
RUN apt install -y systemd init

#pip関連 
#RUN mkdir -p /tmp
#COPY requirements.txt /tmp
#WORKDIR /tmp
#RUN pip install -r requirements.txt
