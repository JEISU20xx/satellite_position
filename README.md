# ROS2 Satellite Position Publisher
[![test](https://github.com/JEISU20xx/satellite_position/actions/workflows/test.yml/badge.svg)](https://github.com/JEISU20xx/satellite_position/actions/workflows/test.yml)  
このROS2パッケージは、[N2YO.com](https://www.n2yo.com/)のAPIを利用し、衛星の緯度、経度および高度を取得する機能を持ちます。これらの情報を取得し、定期的にパブリッシュする`fetch_position`ノードと、テスト用にその情報を受信してログに出力する`receive_position`ノードで構成されています。
## fetch_position.py
- [N2YO.com](https://www.n2yo.com/)のAPIを利用し、衛星の位置情報を取得し、topic`satellite_position`としてパブリッシュするノードです。
- 位置情報はLat（緯度）、Lon（経度）、Alt（高度）で表示されます。
### 実行準備
1\. [N2YO.com](https://www.n2yo.com/)でアカウントを作成し、APIキーを取得してください。   
2\. fetch_posiiton.pyの17行目の`os.getenv('N2YO_API_KEY')`を取得したAPIキーに変更するか、`~/.bashrc`に`export N2YO_API_KEY='取得したAPIキー'`を追加してください。  
3\. fetch_position.pyの18行目の`25544`を取得したい衛星のNORAD IDに変更してください。  
（25544は国際宇宙ステーションのNORAD IDです。）

### 端末1でfetch_position.pyを実行し、別の端末2でtopic確認した例
端末1
```
$ ros2 run satellite_position fetch_position

```
端末2
```
$ ros2 topic echo satellite_position
data: 'Lat: -14.18630938, Lon: 129.04303749, Alt: 34366.78'
---
data: 'Lat: -14.20007997, Lon: 129.04026218, Alt: 34365.72'
---
```
### テスト用コード
- receive_position.py
- test.launch.py
## 動作環境
このパッケージは以下の環境で動作が確認済みです。
- **OS**：Ubuntu 22.04 LTS
- **ROS2 version**：humble
## ライセンス
- このリポジトリは3条項BSDライセンスの下で公開されています。
- 詳細は[LICENSE](https://github.com/JEISU20xx/satellite_position/blob/master/LICENSE)を確認してください。  
  
© 2025 Junya Wada
