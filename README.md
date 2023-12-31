# robosys2023
# mypkg
* このリポジトリは千葉工業大学先進工学部未来ロボティクス学科4sのロボットシステム学の講義で作成したものです。
* このリポジトリを使用するためにはROS2をダウンロードしている必要があります。
![test.bash](https://github.com/m1031/mypkg/actions/workflows/test.yml/badge.svg)
# topicとは
* ノード間でやりとりするデータのことで、相手の状態に関係なく常にデータを発信しており、不特定多数がデータを受け取ることができる仕組みになっている。
# talker.py
* 数字をカウントしてトピック/countupを通して送信する
# listener.py
* /countupからメッセージを受信して表示する。
# talk_listen.launch.py
* talker.pyとlistener.pyを一度に立ち上げることができるもの
## インストール方法
* ubuntu上で以下のコードを入力することでクローンを作成できる
```
git clone https://github.com/m1031/mypkg
```
## 使用例
# talker.py&listener.py
* talker側
```
ros2 run mypkg talker
```
listener側
```
ros2 run mypkg listener
```
と入力するとlistener側に以下の出力が得られる。
```
[INFO] [1703994355.300705431] [listener]: Listen: 107
[INFO] [1703994355.793491557] [listener]: Listen: 108
[INFO] [1703994356.293891845] [listener]: Listen: 109
[INFO] [1703994356.794737857] [listener]: Listen: 110
[INFO] [1703994357.294755341] [listener]: Listen: 111
[INFO] [1703994357.793307521] [listener]: Listen: 112
[INFO] [1703994358.294977861] [listener]: Listen: 113
[INFO] [1703994358.794656592] [listener]: Listen: 114
[INFO] [1703994359.294840084] [listener]: Listen: 115
[INFO] [1703994359.794692290] [listener]: Listen: 116
```
# talk_listen.launch.py
ターミナル上で
```
ros2 launch mypkg talk_listen.launch.py
```
と入力すると以下の出力が得られる。
```
[INFO] [launch]: All log files can be found below /root/.ros/log/2023-12-31-12-40-22-882868-m1031-5017
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [5019]
[INFO] [listener-2]: process started with pid [5021]
[listener-2] [INFO] [1703994023.580000356] [listener]: Listen: 0
[listener-2] [INFO] [1703994024.056569093] [listener]: Listen: 1
[listener-2] [INFO] [1703994024.557010055] [listener]: Listen: 2
[listener-2] [INFO] [1703994025.057129039] [listener]: Listen: 3
[listener-2] [INFO] [1703994025.556519666] [listener]: Listen: 4
[listener-2] [INFO] [1703994026.056180261] [listener]: Listen: 5
[listener-2] [INFO] [1703994026.556928773] [listener]: Listen: 6
[listener-2] [INFO] [1703994027.057160056] [listener]: Listen: 7
[listener-2] [INFO] [1703994027.556680826] [listener]: Listen: 8
[listener-2] [INFO] [1703994028.057051612] [listener]: Listen: 9
[listener-2] [INFO] [1703994028.556841702] [listener]: Listen: 10
[listener-2] [INFO] [1703994029.057428507] [listener]: Listen: 11
[listener-2] [INFO] [1703994029.557080409] [listener]: Listen: 12
[listener-2] [INFO] [1703994030.057077995] [listener]: Listen: 13
[listener-2] [INFO] [1703994030.556571114] [listener]: Listen: 14
```
## 必要なソフトウェア
* Python
* ros2

## テスト環境
* Ubuntu 22.04.2 LTS
## 著作権、ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
* このパッケージのコードの一部やテストの為に使用しているコンテナは下記のスライド(CC-BY-SA 4.0 by Ryuichi Ueda)のものを、本人の許可を得て使用したものです。
 * [ryuichiueda/mypkg](https://github.com/ryuichiueda/mypkg)
* © 2023 Mahiro Yamoto
