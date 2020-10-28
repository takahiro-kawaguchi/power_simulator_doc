# bus_non_unit  

non-unit バス(発電機、負荷ともに接続されていないバス)の実装  

## メソッド  

- **obj = bus_non_unit(shunt)**  
  コンストラクタ  

- **obj = get_constraint(obj, Vr, Vi, P, Q)**  
  入力 : Vr(電圧の実部), Vi(電圧の虚部), P(有効電力), Q(無効電力)  
  出力 : [P; Q] (2次元縦ベクトル) : non-unitバスは自身の消費電力が0なので、潮流状態ではP=0, Q=0である  
