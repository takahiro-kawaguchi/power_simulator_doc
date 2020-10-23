# controller_retrofit_type1

レトロフィットコントローラの実装．

- 線形化されたネットワークを対象
- 相互作用信号はw=x, v=V


## 変数

- **model**: 環境のモデル
- **K_inter**: 内部コントローラ


## メソッド

- **obj = controller_retrofit_type1(net, idx, ratio, sys_model)**  
  コンストラクタ  
  - net: 付加されるネットワーク
  - idx: 付加されるバスの番号．複数バスをまとめて局所システムとするときはベクトルを指定
  - ratio: 入力へのペナルティ．0だと入力制約なし，infでK_inter=0になる．  
    controller_retrofit_type1(net, idx)と呼ぶと，ratio=0となる．
  - sys_model: 環境モデル  
    ssクラスが与えられるとそのモデルを用いる．  
    実数を入れると，実環境をその次数で低次元化したモデルが用いられる  
    [] を入れると，環境モデルを用いない．