# tools.cellfun

## 構文

[B = tools.cellfun(func,A)](###B-=-tools.arrayfun(func,A))

[B = tools.cellfun(func,A1,...,An)](###-B-=-tools.arrayfun(func,A1,...,An))


## 説明

### B = tools.cellfun(func,A)

この関数はセルAの各要素ごとにfuncを適用し後B{i} = func(A{i})となるようにセルBに結果を格納します．

### B = tools.cellfun(func,A1,...,An)

この関数はセルAの各要素ごとにfuncを適用し後B{i} = func(A1{i},...,An{i})となるようにセルBに結果を格納します．

## 例

```matlab
C = {1 2 3 4};
func = @(x) 2*x
```
のようセルと関数を生成します．
そこに以下のようにtools.arrayfuncを適用すると

```matlab
ans = tools.cellfunc(func,C);
```
結果は以下のようになります．

```matlab
ans =

  1×4 の cell 配列

    {[2]}    {[4]}    {[6]}    {[8]}

```

## 入力引数

- func(関数ハンドル)
  - 入力する配列の要素に適用する関数．

- A(セル)

## 出力引数

- B(セル)

## 補足
matlabの組み込み関数にも同様に[cellfunc](https://jp.mathworks.com/help/matlab/ref/arrayfun.html)という関数があるがこれは，tools.cellfuncと違い出力として配列を返す．