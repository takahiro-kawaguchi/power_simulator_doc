# controller_broadcast_PI

ブロードキャストコントローラ（PIコントローラ）の実装

周波数偏差の平均値をフィードバックする．



## メソッド

- **obj = controller_broadcast_PI(net, y_idx, u_idx, Kp, Ki)**  
  - net: ネットワーク
  - y_idx: 出力を観測するバス
  - u_idx: 入力を印加するバス
  - Kp: Pゲイン
  - Ki: Iゲイン

