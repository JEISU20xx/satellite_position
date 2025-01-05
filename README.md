# ROS2 Satellite Position Publisher
[![test](https://github.com/JEISU20xx/satellite_position/actions/workflows/test.yml/badge.svg)](https://github.com/JEISU20xx/satellite_position/actions/workflows/test.yml)
## fetch_position.py
- 衛星の位置情報を取得し、topic`satellite_position`としてパブリッシュするノードです。
- 位置情報はLat(緯度)、Lon(経度)、Alt(高度)で表示されます。
### 実行準備
1\. [N2YO.com](https://www.n2yo.com/)でアカウントを作成し、APIキーを取得してください。   
2\. fetch_posiiton.pyの17行目の`os.getenv('N2YO_API_KEY')`を取得したAPIキーに変更するか、`~/.bashrc`に`export N2YO_API_KEY='取得したAPIキー'`を追加してください。  
3\. fetch_position.pyの18行目の`25544`を取得したい衛星のNORAD IDに変更してください。  
(25544は国際宇宙ステーションのNORAD IDです。)

### 端末1でfetch_position.pyを実行し、別の端末2でtopic確認した例
端末1
```
$ ros2 run satellite_position fetch_position
[INFO] [1736086501.854790270] [satellite_position_node]: Published satellite position: Lat: -14.18630938, Lon: 129.04303749, Alt: 34366.78
[INFO] [1736086506.799973612] [satellite_position_node]: Published satellite position: Lat: -14.20007997, Lon: 129.04026218, Alt: 34365.72
```
端末2
```
$ ros2 topic echo satellite_position
data: 'Lat: -14.18630938, Lon: 129.04303749, Alt: 34366.78'
---
data: 'Lat: -14.20007997, Lon: 129.04026218, Alt: 34365.72'
---
data: 'Lat: -14.21384991, Lon: 129.03749002, Alt: 34364.65'
---
```
### テスト用コード
- receive_position.py
  - fetch_position.pyが正しく動作しているか確認します。
    - topic`satellite_position`をサブスクライブします。
- test.launch.py
  - fetch_position.pyをテストするためのlaunchです。
    - fetch_position.pyとreceive_position.pyを実行し、衛星の位置情報の取得とパブリッシュ、サブスクライブを同時に行います。

## テスト環境
- Ubuntu 22.04

## ライセンス
- このリポジトリはBSD-3-Clauseライセンスの下で公開されています。
- 詳細は[LICENSE](https://github.com/JEISU20xx/satellite_position/blob/master/LICENSE)を確認してください。

## 著作権
© 2025 Junya Wada
