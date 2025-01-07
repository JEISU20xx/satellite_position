# ROS2 Satellite Position Publisher
[![test](https://github.com/JEISU20xx/satellite_position/actions/workflows/test.yml/badge.svg)](https://github.com/JEISU20xx/satellite_position/actions/workflows/test.yml)  ## 概要
このROS2パッケージは、[N2YO.com](https://www.n2yo.com/)のAPIを利用して、特定の衛星の現在位置情報（緯度、経度、高度）を取得し、ROS2のトピックとして公開します。
## 動作環境
このパッケージは以下の環境で動作が確認済みです。
- **OS**：Ubuntu 22.04 LTS
- **ROS2 version**：humble
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
1\. APIキーの取得と設定
- [N2YO.com](https://www.n2yo.com/)でアカウントを作成し、APIキーを取得します。
- 環境変数を設定：
```
$ echo "export N2YO_API_KEY='取得したAPIキー'" >> ~/.bashrc
$ source ~/.bashrc
```
2\. NORAD IDの設定
- `satellite_position/fetch_position.py`の18行目で追跡したい衛星のNORAD IDを指定してください。デフォルトは国際宇宙ステーション（ISS）のIDである`25544`です。
## 使用方法
ノードの起動とデータの確認
- **fetch_positionノードの実行**  
端末1で以下を実行：
```
$ ros2 run satellite_position fetch_position
```
- **データの確認**  
端末2で以下を実行し、トピックのデータを表示：
```
$ ros2 topic echo satellite_position
```
## fetch_position.py
- [N2YO.com](https://www.n2yo.com/)のAPIを利用し、衛星の位置情報を取得し、topic`satellite_position`としてパブリッシュするノードです。
- 位置情報はLat（緯度）、Lon（経度）、Alt（高度）で表示されます。
## テスト用コード
- receive_position.py
- test.launch.py
## ライセンス
- このリポジトリは3条項BSDライセンスの下で公開されています。
- 詳細は[LICENSE](https://github.com/JEISU20xx/satellite_position/blob/master/LICENSE)を確認してください。  
  
© 2025 Junya Wada
