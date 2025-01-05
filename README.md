# ROS2 Satellite Position Publisher
[![test](https://github.com/JEISU20xx/satellite_position/actions/workflows/test.yml/badge.svg)](https://github.com/JEISU20xx/satellite_position/actions/workflows/test.yml)
## fetch_position.py
- 衛星の位置情報を取得し、topic`satellite_position`としてパブリッシュするノード
### 実行準備
1\. [N2YO.com](https://www.n2yo.com/)でアカウントを作成し、APIキーを取得してください。   
2\. fetch_posiiton.pyの17行目の`os.getenv('N2YO_API_KEY')`を取得したAPIキーに変更するか、`~/.bashrc`に`export N2YO_API_KEY='取得したAPIキー'`を追加してください。  
3\. fetch_position.pyの18行目の`25544`を取得したい衛星のNORAD IDに変更してください。  
(25544は国際宇宙ステーションのNORAD IDです。)

### 実行し別端末で`$ ros2 topic echo satellite_position`をした例
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
  - fetch_position.pyが正しく動作しているか確認する
    - topic`satellite_position`をサブスクライブする
- test.launch.py
  - fetch_position.pyをテストするためのlaunch
    - fetch_position.pyとreceive_position.pyを実行し、衛星の位置情報の取得とパブリッシュ、サブスクライブを同時に行う

## テスト環境
- Ubuntu 22.04
- ros2 latest

## ライセンス
- このリポジトリはBSD-3-Clauseライセンスの下で公開されています。
- 詳細は[LICENSE](https://github.com/JEISU20xx/satellite_position/blob/master/LICENSE)を確認してください。

## 著作権
© 2025 Junya Wada
