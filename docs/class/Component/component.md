# component クラス

バスに接続される機器のスーパークラス

## 抽象メソッド

- **x = initialize(V, I, net)**  
  潮流計算で決まったV, Iを受け取って初期化処理を行う  
  netはpower_networkインスタンス，xは平衡状態

- **nx = get_nx()**  
  状態変数の数を返す

- **nu =get_nu()**  
  入力の数を返す

- **[dx, I] = get_dx_I(x, V, u)**  
  状態x, バス電圧V, 入力uをうけとって，状態の微分dxと電流Iを返す


## メソッド（オーバーライド推奨）

- **[dx, I] = get_dx_I_linear(x, V, u)**  
  線形化した場合について，dxとIを返す  
  power_networkのsimulate_linearで利用される

- **[A, B, C, D, L, R, S] = get_linear_matrix()**  
  線形化したシステムの行列を返す．  
  power_networkのget_sysで利用される．  
  `dx = A*(x-xss) + B*u+L*(V-Vss)+Rd`  
  `(I-Iss)=C*(x-xss)+D*(V-Vss)`  
  `z = S(x-xss)`  
  となるような行列を返す
