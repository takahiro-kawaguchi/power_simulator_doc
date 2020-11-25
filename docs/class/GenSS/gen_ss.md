# gen_ss

連続時間状態空間モデルの同定を行うクラス

## 子クラス
- [gen_ss_diagcat](./gen_ss_diagcat.md)
- [gen_ss_generator_file](./gen_ss_generator_file.md)
- [gen_ss_power_area](./gen_ss_power_area.md)
- [gen_ss_sym_file](./gen_ss_sym_file.md)

## 抽象変数
- **params**: それぞれの要素がパラメータ`theta`のパラメータ名に対応するcell配列

## 抽象メソッド

- **get_params(obj)**  
    パラメータ`theta`の取得

- **set_params(obj, theta)**  
    パラメータ`theta`の変更

- **[A, B, C, D, dA, dB, dC, dD] = get_ss(obj, theta)**  
    パラメータ`theta`からシステムの状態空間モデル（連続時間・離散時間）を取得する
    - `A,B,C,D`: 連続時間の状態空間モデル
    - `dA,dB,dC,dD`: 離散時間の状態空間モデル

## メソッド
- **set_sys(obj, sys)**  
    システムの事前情報の導入


- **sys = get_sys(obj, theta, Ts)**  
    システムのモデルを出力
    - `sys`: 連続時間状態空間モデル. `Ts`が引数に含まれる場合は離散時間状態空間モデル
    - `Ts`: サンプル時間（省略可能）

- **varargout = get_ss_p(obj)**  
    システムの情報（`A,B,C,D,dA,dB,dC,dD`）をN×1のcell配列で出力する

- **o = order(obj)**  
    システムの次数を出力する
    - `o`: システムの次数

- **[c, ceq, dc, dceq] = con_blance(obj, theta)**  

- **[c, ceq] = con_stable(obj, theta)**  

- **[c, ceq, dc, dceq] = constraint(obj, theta)**  

