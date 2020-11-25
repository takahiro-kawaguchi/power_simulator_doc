# gen_ss_generator_file



## 変数
- **n**: 発電機の次数（デフォルトは*1*）
- **theta**: 発電機のパラメータによるcell配列（事前情報）
- **gen_ss**: クラス`gen_ss_sym_file`のインスタンス
- **ub**: `params`の上限
- **lb**: `params`の下限
- **name**: モデル自身に割り振られる名前（例えば*generator_pss_noinput*）
- **has_input**: 発電機が入力を含むか否か（デフォルトは*false*）
- **has_pss**: 発電機がPSSを含むか否か（デフォルトは*true*）

## メソッド
- **obj = gen_ss_generator_file(n, has_pss, has_input)**  
    コンストラクタ

- generate_file(obj)  
    **gen_ss_generator_file**において, "+systemID/+gen_ss_sym/"以下に`name`と同じ名前の.mファイルがない際に呼ばれる  
    

- **set_components(obj, components)**  
    componentからパラメータを設定（関数"components2params"が呼ばれる）
    - `component`: componentのインスタンス

- [theta, n] = components2params(obj, components)  
    **set_components**にて呼ばれる  
    複数の発電機のパラメータの平均値をパラメータとして返す
    - `theta`: システムのパラメータ
    - `n`: componentの数

