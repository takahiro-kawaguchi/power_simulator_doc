# （準備中）電力系統モデルについて

## power_network

[@power_network/power_network.m]()

全ての電力系統モデルの基底クラス．  

### メンバ変数
- bus
    - バスのセル配列
- branch
    - ブランチのテーブル
- omega0(=2*pi*60)
    - 基準角周波数（デフォルトは60Hz）
- str_display(='none')
    - 非線形の方程式求解の際の表示レベル（デフォルトは出力を表示しない）
- display_simulate(=true)
    - 常微分方程式求解の進捗の表示有無（デフォルトは表示する）
- x_ss
    - 状態の平衡点配列
- V_ss
    - 電圧の平衡点配列
- I_ss
    - 電流の平衡点配列
- controllers
    - コントローラのセル配列
- controllers_global
    - グローバルコントローラのセル配列
- tol
    - 数値計算(ode)における許容誤差
- plotfunc(=@odephas2)
    - 数値計算(ode)における描画処理（[]を指定することで描画しないこともできる）
- reset_time(=5)
    - 数値計算(ode)のタイムアウト時間（デフォルトは5秒）
- retry(=true)
    - 数値計算(ode)のタイムアウト時の処理（デフォルトはリトライ）

### メンバ関数
- `out = simulate(t, u, idx_u, options)`
    - 入力変数 `t`  
        シミュレーション時間の設定
    - 入力変数 `u`  
        バスへの入力
    - 入力変数 `idx_u`  
        入力するバスの指定  
    - 入力引数 `option`  
        シミュレーションのオプションを設定する  
        - x_init：  
            状態の初期値（規定値: x_ss）  
            バスごとのセル配列あるいは，すべてをスタックしたベクトル．  
            out.Xを入れると，outの最後の状態からスタートする
        - V_init：  
            電圧の初期値（規定値: x_init に対応した値）  
            バスごとのセル配列あるいは，すべてをスタックしたベクトル．  
        - I_init：  
            電流の初期値（規定値: x_init に対応した値）  
            バスごとのセル配列あるいは，すべてをスタックしたベクトル．  
        - xk_init：  
            レトロフィットコントローラの状態の初期値（規定値: 0）  
            コントローラごとのセル配列，あるいは，すべてをスタックしたベクトル．  
            out.Xkを入れると，outの最後の状態からスタートする．
        - xkg_init：  
            グローバルコントローラの状態の初期値（規定値: 0）  
            コントローラごとのセル配列，あるいは，すべてをスタックしたベクトル．  
            out.Xk_globalを入れると，outの最後の状態からスタートする．
        - fault：  
            地絡の条件．  
            {[tstart, tend], idx_fault}というセル配列のセル配列．
        - linear：  
            線形化したシステムでシミュレーションを行うかどうか（規定値: false）
    - 出力引数 `out`  
        16の機器（generator）ごとの時間応答データが含まれる  
        - t：時刻
        - X：バスの状態（バスごとのセル配列）
        - V：バスの電圧（バスごとのセル配列）
        - Xk：レトロフィットコントローラの状態（コントローラごとのセル配列）
        - Xk_global：グローバルコントローラの状態（コントローラごとのセル配列）
        - U：レトロフィットコントローラが生成した入力（コントローラごとのセル配列）
        - U_global：グローバルコントローラが生成した入力（コントローラごとのセル配列）
        - sol：ode15sが返す解sol

## network_68bus

[network_68bus.m]()

IEEE 68bus 16machine システムの実装．  
発電機として[generatorAGC](/Docs/component/#generator_agc)を，負荷として[load_varying_impedance](/Docs/component/#load_varying_impedance) を導入したネットワークである．  


## network_70bus

[network_70bus.m]()

定本さんの論文(magazine)における，<font color="red">IEEE 68bus 16machineシステムへ(?)</font> solar, wind farm を導入した電力ネットワーク．  
発電機として[generator](/Docs/component/#generator)を，負荷として[load_const_impedance](/Docs/component/#load_const_impedance), [load_const_power](/Docs/component/#load_const_power) を導入したネットワークである．  
発電機として[generator]ネットワーク定義の際に `net=network_70bus(load_type)`のように定義する．ここで，load_typeには1~2を代入する．負荷には，1の場合は[load_const_impedance](/Docs/component/#load_const_impedance)，2の場合は[load_const_power](/Docs/component/#load_const_power)を導入する．引数が省略されている場合は[load_const_impedance](/Docs/component/#load_const_impedance)を負荷として導入する．[](現状、load_typeには1~3が代入できるが、3は今後削除予定なので省略した)  


## network_9bus

[network_9bus.m]()

<font color="red">要説明追加</font>  