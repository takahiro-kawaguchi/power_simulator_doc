# Step2（線形化したシステムを使う）

- 対象者：制御工学の技術者
- できるようになること：
    - 線形化したシステムのシミュレーションを行う
    - 線形化したシステムの状態空間表現を取得する


## 解説
### ネットワークの定義

ネットワークの定義はSTEP1と同様に以下のように行う．
```
net = network_68bus_AGC_varying_impedance();
```
- 出力変数`net`  
    ネットワーク内部の情報としてbus, branch, generator, controllerなどの情報が含まれる
<br>

### 線形化したシステムのシュミレーションの実行
シュミレーションは以下のように行う。
```
out = net.simulate_linear([0 20], option)
```
引数の詳細については[STEP1](./step1.md)に示されている`net.simulate(t,option)`と同様であるため、そちらを参照していただきたい。

<br>

### 線形化したシステムの状態空間表現を得る
線形化した状態空間モデルを得る
```
sys =  net.get_sys(with_controller);
```
get_sysで得られるシステムは平衡点からの偏差を状態ととっていることに注意．
- **入力引数**`with_controller`  
    true　のとき，コントローラが付加されたシステム，falseならばコントローラなしのシステムを返す．規定値はfalse
    - 今はfalseの場合のみ考える。trueにする場合コントローラーの設定が必要となる。詳細は[STEP3](./step3.md)を参照。


- **出力変数**`sys` 
    -  __状態方程式の係数行列__`A,B,C,D`  
        線形化したシステムのA行列,B行列,C行列,D行列の各要素の情報を格納している。
        <span style="color: red; ">行列Eについて</span>
    - __状態State__  
         各発電機の状態パラメータ7つずつの情報をもつ。
         今`net`にはIEEE68busシステムの情報を格納していたため、このシステムの線形化した時の状態Xには16個の発電機の各パラメータ7つずつで構成された112行の行列となっている。  
        - 状態に関するパラメータ
         <span style="color: red; ">StateName,StateUnit,InputDelayの操作</span>
    - __入力信号__  
         slackバスを除くバスへの入力:各2入力(AGCポート、AVRポート)
         外乱ポートへの入力：各3入力
         で構成された行列。
         この例ではIEEE68バスシステムを解析しているため
         non-unitバスは17つあり、それを除く51個のPQバス・PVバス・slackバスへの入力が2つずつ(51×2=102)、外乱ポートへの入力が3つずつ(16×3)より計150個の入力情報を格納  
        - `InputGroup` :  
            状態空間方程式の入力値uの各チャネルがどのバス/発電機の値に対応しているか示す。 
        - 入力信号に関するパラメータ
         <span style="color: red; ">InputName,InputUnit,InputDelay操作</span>
    - __出力信号__  
         各バス・発電機の抵抗値、電圧フェーザ、電流フェーザの値を表す。
         発電機でのスカラーの抵抗値？:各１要素
         各バスでの電圧の値:各2要素(実部と虚部の情報)
         各バスでの電流の値:各2要素(実部と虚部の情報)
         この例ではIEEE68バスシステムを解析しているため
         発電機16×1要素、バスの電圧68×2要素、バスの電流68×2要素、の計288個の出力情報を格納している。  
        - `OutputGroup` :  
            状態空間方程式の出力値Yの各チャネルがどのバス/発電機の値に対応しているか示す。  
        - 出力信号に関するパラメータ
         <span style="color: red; ">OutputName,OutputUnit,OutputDelay操作</span>
    [](
        行列ABCDの行数列数を見てみると\
       A行列：112×112行列、\
       B行列：112×150行列、\
       C行列：288×112行列、\
       D行列：288×150行列、となっていることが確認できる。\
       )  

##　例１：コントローラーを追加する
```
sys =  net.get_sys(true);
```
コントローラの設定については[STEP3](./step3.md)を参照。


## 例２：特定の入力から出力までのシステムを見る
例えば入力`d1`から出力`z1`までのシステムを見たい場合、以下のように実行することで見ることができる。
```
sys('z1','d1')
```


## 例３：線形化したシステムのシミュレーション結果を見る

以下のコードは68busシステムを線形化し、その出力をグラフで表示するものである。
```
net= network_68bus();
option_fault = struct();
option_fault.fault = {{[0, 0.01], 1}};
out_fault = net.simulate_linear([0, 0.01], option_fault);
option = struct();
option.x_init = out_fault.X;
out_linear = net.simulate_linear([0 100], option);
sys = net.get_sys();
x0 = horzcat(out_fault.X{:});
x0 = x0(end, :)' - net.x_ss;
[z, t, x] = initial(sys, x0);
x = x+net.x_ss';
names = {'\delta', '\Delta\omega', 'E', 'V_{fd}', '\xi_1', '\xi_2', '\xi_3'};
for i = 1:16
	figure
	for j = 1:7
		subplot(3, 3, j), plot(out_linear.t, out_linear.X{i}(:, j), '.-', t, x(:, (i-1)*7+j), '.-'), title(names{j}, 'Interpreter', 'tex');
	end
end
```
         