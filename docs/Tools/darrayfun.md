# tools.darrayfun

## 構文

[B = tools.darrayfun(func,A)](###B-=-tools.darrayfun(func,A))

## 説明

### B = tools.darrayfun(func,A)

この関数は配列Aの各要素ごとにfuncを適用し後B(i,i) = func(A(i))となるように正方行列Bに結果を格納します．

## 例

```matlab
arr = [1 2 3];
func = @(x) 2*x
```
のように配列と関数を生成します．
そこに以下のようにtools.darrayfunを適用すると

```matlab
ans = tools.arrayfunc(func,arr);
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

- A(配列)

## 出力引数

- B(行列)
  - 対角行列となる

