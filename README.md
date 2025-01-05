# ROS2 Satellite Position Publisher
[![test](https://github.com/JEISU20xx/satellite_position/actions/workflows/test.yml/badge.svg)](https://github.com/JEISU20xx/satellite_position/actions/workflows/test.yml)
## fetch_position.py
- 衛星の位置情報を取得し、topic`satellite_position`としてパブリッシュするノード

### テスト用コード
- receive_position.py
  - fetch_position.pyが正しく動作しているか確認する
    - topic`satellite_position`をサブスクライブする
- test.launch.py
  - fetch_position.pyをテストするために実行するlaunch
    - fetch_position.pyとreceive_position.pyを実行し、衛星の位置情報の取得とパブリッシュ、サブスクライブを同時に行う

## テスト環境
- Ubuntu 22.04
- ros2 latest

## ライセンス
- このリポジトリはBSD-3-Clauseライセンスの下で公開されています。
- 詳細は[LICENSE](https://github.com/JEISU20xx/satellite_position/blob/master/LICENSE)を確認してください。

## 著作権
© 2025 Junya Wada
