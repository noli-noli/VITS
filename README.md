# VITS
本リポジトリはText-to-Speechの一種であるVITSを使用するにあたり、個人的に纏めたものである。詳しい論文や引用リポジトリは、**クレジット**を確認の程。


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

# 環境構築
本リポジトリはDocker環境を提供しています。Docker環境を使用する場合は**手段1**を、Docker環境を使用せず手動で動作させたい場合は**手段2**を確認してください。



## [手段1]dockerを使用して環境セットアップ
リポジトリのクローン
```sh
git clone https://github.com/noli-noli/VITS.git
```
dockerコンテナを立ち上げる
```ssh
docker compose up -d
```
コンテナにアタッチ
```ssh
docker exec -it vits-vits-exp-1 bash
```



## [手段2]docker環境を使用せず、手動で環境セットアップ
リポジトリのクローン
```sh
git clone https://github.com/noli-noli/VITS.git
```
ワークディレクトリに移動
```sh
cd VITS/vits-workspace
```
Pythonモジュールのインストール
```sh
pip install -r requirements.txt
```


# データセット準備～学習
データセットの準備において、**シングル学習(話者が1人)** と **マルチ学習(話者が複数人)** でそれぞれ設定方と学習時のプログラムが異なります。 

**シングル学習**
1. `datasets/`ディレクトリ内部に、任意の名称でディレクトリを作成
2. 音声ファイル(22050Hz / 16-bit / モノラル)を作成したディレクトリ内に配置
3. 音声ファイルと同じディレクトリに「音声ファイルのパス | 字幕」の内容でテキストファイルを作成。train用とval用をそれぞれ作成  

- 例(train.txt) 100サンプル程
```bash
dataset/001.wav|こんにちは
dataset/002.wav|初めまして
        ・
        ・
dataset/100.wav|よろしく
```  

- 例(val.txt) 10サンプル程
```bash
dataset/004.wav|わたしはほげほげと申します
dataset/009.wav|本当ですか
dataset/053.wav|では
        ・
        ・
dataset/088.wav|作業を開始します
```  

4. `vits_preprocess.py`を実行し、テキストファイル内の「字幕」を前処理
```bash
python3 vits_preprocess.py --filelists ./datasets/sample/train.txt ./datasets/sample/val.txt
```  


5. `config-single.json`内の **training_files** と **validation_files** をそれぞれ手順3で作成したtrain用とval用のファイルパスに書き換える  

6. `train_simgle.py`を実行し、学習を開始する。**手順5**で作成したconfigファイルを` -c `で指定し、` -m `で`models`内に学習経過が保存されるディレクトリを指定する。
```bash
python3 vits_train_single.py -c configs/config-single.json -m sample
```  

## マルチ学習


## クレジット
 - 論文：https://arxiv.org/abs/2106.06103
 - オリジナル：https://github.com/jaywalnut310/vits
 - フォーク元：https://github.com/SayaSS/vits-finetuning
 - テキストクリーニング：https://github.com/CjangCjengh/vits
