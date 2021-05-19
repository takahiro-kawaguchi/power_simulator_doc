# 【第四回】電力系統の自作

- 本ステップでできるようになること  
    自分で用意したシステムをpower_simulatorに実装できるようになる

### 自分用のメモ(後で消すべし)


#### 参考サイト

- [illustrationprize.com 系統バスの分類](https://illustrationprize.com/ja/455-classification-of-power-system-buses.html)

- [matlab: IEEE 9bus](https://jp.mathworks.com/help/physmod/sps/examples/ieee-9-bus-loadflow.html#d122e1492)

- [どこかのスライド](http://www.egr.unlv.edu/~eebag/Power%20Flow%20Analysis.pdf)

- [wikipedia: slack bus](https://en.wikipedia.org/wiki/Slack_bus)

## 解説

### バスの定義

バスの定義は次のように行う．

```matlab
net = power_network(); % 何も定義されていないネットワーク
net.bus = cell(3, 1);
net.bus{1} = bus_slack(…);
net.bus{2} = bus_PV(…);
net.bus{3} = bus_PQ(…);
```

- 出力変数`net`  
    ネットワーク内部の情報としてbus, branch, generator, controllerなどの情報が含まれる

### バスの変数

一般的にバスに関係する変数として以下の6つのものがあります．

- $P$: 有効電力
- $Q$: 無効電力
- $|V|$: 電圧
- $\delta$: 位相角
- $G_{shunt}, B_{shunt}$: 地面に繋がっているシャント抵抗のインピーダンス

以下の３つのバスは$P,Q,V,\delta$のうち2つの変数とシャント抵抗の値を指定します．

### swing bus (slack bus)

基準として機能する特殊なバス．電圧と位相角は固定されているが有効電力と無効電力は未知である．
swing busの定義は以下のように行う

```matlab
net.bus{idx} = bus_slack(V_abs, V_angle, [G_shunt, B_shunt]);
```

- 入力引数
    - V_abs
        電圧．
    - V_angle
        位相角．通常0となる．
    - [G_shunt, B_shunt]
        地面に繋がっているシャント抵抗のインピーダンスの実部と虚部．

### generator bus (PV bus)

```matlab
net.bus{idx} = bus_PV(V_abs, P_gen, [G_shunt, B_shunt]);
```

- 入力引数
    - V_abs
        電圧
    - P_gen
        有効電力
    - [G_shunt, B_shunt]
        地面に繋がっているシャント抵抗のインピーダンスの実部と虚部．

### load bus (PQ bus)

有効電力と無効電力が指定され，バス電圧が計算されるバス．発電機が接続されてないバスは

load busの定義は以下のように行う

```matlab
net.bus{idx} = bus_non_unit([G_shunt, B_shunt]);
```

- 入力引数
    - [G_shunt, B_shunt]
        地面に繋がっているシャント抵抗のインピーダンスの実部と虚部．

#### nagative generation

```matlab
net.bus{idx} = bus_PQ(-Pload, -Qload, [G_shunt, B_shunt]);
```

- 入力引数
    - Pload
        有効電力．
    - Qload
        無効電力．
    - [G_shunt, B_shunt]
        地面に繋がっているシャント抵抗のインピーダンスの実部と虚部．

#### 例: IEEE 9busのbusの定義

```matlab
net.bus{1} = bus_slack(1.040000, 0.000000, [0.000000, 0.000000])
net.bus{2} = bus_PV(1.025000, 1.630000, [0.000000, 0.000000])
net.bus{3} = bus_PV(1.025000, 0.850000, [0.000000, 0.000000])
net.bus{4} = bus_non_unit([0.000000, 0.000000])
net.bus{5} = bus_PQ(-1.250000, -0.500000, [0.000000, 0.000000])
net.bus{6} = bus_PQ(-0.900000, -0.300000, [0.000000, 0.000000])
net.bus{7} = bus_non_unit([0.000000, 0.000000])
net.bus{8} = bus_PQ(-1.000000, -0.350000, [0.000000, 0.000000])
net.bus{9} = bus_non_unit([0.000000, 0.000000])
```

### ブランチの定義

```matlab
net.branch = branch;
```
この`branch`という変数はブランチの情報を含んだtableになっていて，例えばIEEE 9busだと以下のようになる

```matlab

  9×7 table

    bus_from    bus_to    x_real    x_imag      y       tap    phase
    ________    ______    ______    ______    ______    ___    _____

       1          4            0    0.0576         0     1       0  
       2          7            0    0.0625         0     1       0  
       3          9            0    0.0586         0     1       0  
       4          5         0.01     0.085     0.088     0       0  
       4          6        0.017     0.092     0.079     0       0  
       5          7        0.032     0.161     0.153     0       0  
       6          9        0.039      0.17     0.179     0       0  
       7          8       0.0085     0.072    0.0745     0       0  
       8          9       0.0119    0.1008    0.1045     0       0  
```

- bus_from_phase
    接続元のバスの番号
- bus_to
    接続先のバスの番号
- x_real

- x_imag

- y

- tab

- phase


<span style="color: red; ">この辺のパラメータについて</span>

### 機器の定義

バスへの機器を接続は以下のように行う．

```matlab
net.bus{1}.add_component(component);
```

componentには以下のような種類のものがある

- generator
- load_const_impedance
- load_const_power
- load_random_power

<span style="color: red; ">ここではすべての機器について書くと厄介そうなのでgeneratorのみを書くだけにしようと思っている．</span>

#### generatorの定義

generatorは以下のように定義する．

```matlab
gen = generator(mac, exc, pss);
```
##### mac

19個のフィールドをもつtableとなる．以下その例である．

```matlab
1×19 table

No_machine    No_bus    MVA_base     Xl      Xa     Xd       Xdp     Xdpp     Tdo      Tdop      Xq       Xqp     Xqpp     Tqo    Tqop     M     d    P_low    flag_adj
__________    ______    ________    _____    __    _____    _____    _____    ____    ______    _____    _____    _____    ___    ____    ___    _    _____    ________

    1           1         1000      0.204    0     1.569    0.324    0.249    5.14    0.0437    1.548    0.918    0.248    0.5    0.07    100    2     100        1   
```

<span style="color: red; ">この辺のパラメータについて</span>

##### exc

20個のフィールドをもつtableとなる．以下その例である．

```matlab
1×20 table

exc_con1    exc_con2    exc_con3    Ka     Te     exc_con6    exc_con7    exc_con8    exc_con9    exc_con10    exc_con11    exc_con12    exc_con13    exc_con14    exc_con15    exc_con16    exc_con17    exc_con18    exc_con19    exc_con20
________    ________    ________    __    ____    ________    ________    ________    ________    _________    _________    _________    _________    _________    _________    _________    _________    _________    _________    _________

    0           1          0.01      2     0.05       0           0           5           -5           0            0            0            0            0            0            0            0            0            0            0    
```

<span style="color: red; ">この辺のパラメータについて</span>

#### 例: IEEE 9busの機器の定義

<span style="color: red; ">例としてIEEE9busを一から作るみたいなものを書きたいけど，いらない入力引数とかを削って整理したあとにしたほうが良さそう</span>
