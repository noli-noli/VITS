# VITS
本リポジトリはText-to-Speechの一種であるVITSを使用するにあたり、個人的に纏めたものである。詳しい論文や引用リポジトリは、"クレジット"章を確認の程。


## 動作環境(確認済環境)
Python3 (Python3.7)
Cython (3.0.10)
librosa (0.9.1)
matplotlib (3.8.3)
numpy (1.26.3)
torch (1.13.1)
torchvision (0.17.1)
scipy (1.12.0)
tensorboard (2.16.2)
pyopenjtalk (0.3.3)
protobuf (5.26.1)
tqdm (4.65.0)

# 利用法(環境構築編)
本リポジトリはDocker環境を提供しています。Docker環境を使用する場合は[手段1]を、Docker環境を使用せず手動で動作させたい場合は[手段2]を確認してください。



## [手段1]dockerを使用して環境セットアップ
## リポジトリのクローン
```sh
git clone https://github.com/noli-noli/VITS.git
```
## dockerコンテナを立ち上げる
```ssh
docker compose up -d
```
## コンテナにアタッチ
```ssh
docker exec -it vits-vits-exp-1 bash
```



## [手段2]docker環境を使用せず、手動で環境セットアップ
## リポジトリのクローン
```sh
git clone https://github.com/noli-noli/VITS.git
```
## ワークディレクトリに移動
```sh
cd VITS/vits-workspace
```
## Pythonモジュールのインストール
```sh
pip install -r requirements.txt
```


## 利用法(学習編)
### シングル学習


## マルチ学習


## クレジット
 - 論文：https://arxiv.org/abs/2106.06103
 - オリジナル：https://github.com/jaywalnut310/vits
 - フォーク元：https://github.com/SayaSS/vits-finetuning
 - テキストクリーニング：https://github.com/CjangCjengh/vits
