# ROS2 衛星位置取得公開パッケージ
[![test](https://github.com/JEISU20xx/satellite_position/actions/workflows/test.yml/badge.svg)](https://github.com/JEISU20xx/satellite_position/actions/workflows/test.yml)  
## パッケージ概要
[N2YO.com](https://www.n2yo.com/)のAPIを利用して、5秒毎に指定された衛星の現在位置データを取得し、トピックにパブリッシュするROS2のパッケージです。
## ノード概要
### `fetch_position`
- [N2YO.com](https://www.n2yo.com/)のAPIを利用して、5秒毎に指定された衛星の現在位置を取得します。
- 取得したデータを、緯度、経度、高度に分けて３つのトピックにパブリッシュします。
#### 公開されるトピック
- 公開されるトピックは以下の３つです。
  - `satellite_latitude`
    - 衛星の地球上の緯度
  - `satellite_longitude`
    - 衛星の地球上の経度
  - `satellite_altitude`
    - 衛星の高度（単位はkm）


## 動作環境
このパッケージは以下の環境で動作が確認済みです。
- Ubuntu 22.04 LTS
- ROS2 humble
## 依存関係
このパッケージを動かすために必要なライブラリ：
- `requests`: HTTPリクエストを処理するために必要です。  
インストール方法：
```
$ pip install requests
```
## ディレクトリ構造
```
satellite_position/
|-- LICENSE
|-- README.md
|-- launch/
|   `-- test.launch.py
|-- package.xml
|-- resource/
|   `-- satellite_position
|-- satellite_position/
|   |-- __init__.py
|   |-- fetch_position.py
|   `-- receive_position.py
|-- setup.cfg
|-- setup.py
`-- test/
    |-- test.bash
    |-- test_copyright.py
    |-- test_flake8.py
    `-- test_pep257.py
```
## セットアップ
### APIキーの取得と設定
- [N2YO.com](https://www.n2yo.com/)でアカウントを作成し、APIキーを取得します。
- 環境変数を設定：
```
$ echo "export N2YO_API_KEY='取得したAPIキー'" >> ~/.bashrc
$ source ~/.bashrc
```
### NORAD IDの設定
- `fetch_position.py`の18行目で追跡したい衛星のNORAD IDを指定してください。
  - デフォルトは国際宇宙ステーションのID`25544`です。  
- 以下はNORAD IDの一例です。

| Satellite Name          | ID |
|-------------------------|---------|
| H-II Transfer Vehicle-2 | 37838    |
| Hayabusa-2              | 39239    |
| GOSAT Ibuki             | 40025    |
| Kounotori-5             | 40930    |
| Himawari-9              | 41897    |

## 使用方法
### ノードの起動とデータの確認
- **`fetch_position`の実行**  
```
$ ros2 run satellite_position fetch_position
```
- **データの確認**  
別々の端末で以下を実行し、トピックのデータを表示：
```
$ ros2 topic echo satellite_latitude
```
```
$ ros2 topic echo satellite_longitude
```
```
$ ros2 topic echo satellite_altitude
```
#### 出力例
```

```
## テスト用コード
- `receive_position.py`
- `test.launch.py`
## ライセンス
- このリポジトリは3条項BSDライセンスの下で公開されています。
- 詳細は[LICENSE](https://github.com/JEISU20xx/satellite_position/blob/master/LICENSE)を確認してください。  
  
© 2025 Junya Wada
