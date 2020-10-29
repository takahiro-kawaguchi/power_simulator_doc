# bus_PV  

PVバス(slackバスを除く発電機バス)の実装  

## 変数  

- **Vabs** : 電圧の絶対値  
- **P** : 複素電力の実部  


## メソッド  

- **obj = bus_PV(Vabs, P, shunt)**   
  コンストラクタ．Vabsは電圧の絶対値，Pは複素電力の実部  
- **obj = get_constraint(obj, Vr, Vi, P, Q)**  
  入力 : Vr(電圧の実部), Vi(電圧の虚部), P(有効電力), Q(無効電力)  
  出力 : [|V|-obj.Vabs; P-obj.P] (2次元縦ベクトル) :PVバスは自身の消費電力の実部と電圧フェーザの絶対値が与えられ、潮流状態ではP=obj.P, |V|=obj.Vabsである  
  (|V|は[Vr; Vi]のノルム)  