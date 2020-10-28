# bus_slack  

slackバス(発電機バスのうち、電圧フェーザの位相を指定したもの、詳細は電力システム制御理論2.1.2を参照)の実装  

## 変数  

- **Vabs** : 電圧の絶対値  
- **Vangle** : 複素電力の実部  


## メソッド  

- **obj = bus_PV(Vabs, Vangle, shunt)**   
  コンストラクタ．Vabsは電圧の絶対値，Vangleは電圧の偏角  
- **obj = get_constraint(obj, Vr, Vi, P, Q)**  
  入力 : Vr(電圧の実部), Vi(電圧の虚部), P(有効電力), Q(無効電力)  
  出力 : [|V|-obj.Vabs; angle(V)-obj.Vangle] (2次元縦ベクトル) :slackバスは自身の電圧フェーザの位相と絶対値が与えられ、潮流状態では|V|=obj.Vabs, angle(V)=obj.Vangleである  
  (|V|は[Vr; Vi]のノルム, angle(V)は[Vr; Vi]の位相)  