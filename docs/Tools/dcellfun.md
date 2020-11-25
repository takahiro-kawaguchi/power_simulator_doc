# tools.dcellfun
## 構文

[B = tools.dcellfun(func,A)](###B-=-tools.dcellfun(func,A))

## 説明

### B = tools.dcellfun(func,A)

この関数はセルAの各要素ごとにfuncを適用し後B(i,i) = func(A{i})となるように正方行列Bに結果を格納します．

## 例

```matlab
c = {1 2 3};
func = @(x) 2*x
```
のように配列と関数を生成します．
そこに以下のようにtools.dcellfunを適用すると

```matlab
ans = tools.dcellfun(func,c);
```
結果は以下のようになります．

```matlab
ans =

     2     0     0
     0     4     0
     0     0     6
```


## 入力引数

- func(関数ハンドル)
  - 入力する配列の要素に適用する関数．

- A(セル)

## 出力引数

- B(行列)
  - 対角行列となる