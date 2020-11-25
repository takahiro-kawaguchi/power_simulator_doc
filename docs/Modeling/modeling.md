# モデリング

## convert_area2retrofit



## get_model_area
サブシステムモデルと環境モデルの構成.

- 入力変数
  - net
    power_networkクラスを継承する子クラスのインスタンス
  - area
    サブシステムのノードを表すインデックスのベクトル
  - bound
    境界のノードを表すインデックスのベクトル（省略可能）
- 出力変数
  - sys_local_inv
    サブシステムの状態空間モデル
  - sys_others
    環境の状態空間モデル
  - bound
  　境界のノードを表すインデックスのベクトル
  - sys_fb
    フィードバック系の状態空間モデル

- get_model(net, area, bound, with_controller)
  ネットワークとサブシステムのノード、境界のノードからシステムの状態空間モデルを求める関数


## get_model_area_infinite_bus



