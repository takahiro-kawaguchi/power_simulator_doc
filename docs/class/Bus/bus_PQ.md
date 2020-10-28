# bus_PQ  

PQバス(負荷バス)の実装  

## 変数  

- **P** : 複素電力の実部  
- **Q** : 複素電力の虚部  


## メソッド  

- **obj = bus_PQ(P, Q, shunt)**  
  コンストラクタ  
- **obj = get_constraint(obj, Vr, Vi, P, Q)**  
  入力 : Vr(電圧の実部), Vi(電圧の虚部), P(有効電力), Q(無効電力)  
  出力 : [P-obj.P; Q-obj.Q] (2次元縦ベクトル) : PQバスは自身の消費電力が実部、虚部ともに与えられ、潮流状態ではP=obj.P, Q=obj.Qである  
