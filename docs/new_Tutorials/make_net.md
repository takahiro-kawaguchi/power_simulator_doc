<img src="/Figures/index-1.jpg" width=100%;>

# <div style="text-align: center;"><span style="font-size: 130%; color: black;">解析する電力ネットワークを作成する</span></div>

***
power_simulatorでは電力ネットワークの情報をクラスを用いて一つの変数に格納し定義します。(本サイトでは`net`という変数としています。)この変数の内部には、

- バスの情報を含む`bus`  
- ブランチの情報を含む`branch`
- コントローラの情報を含む`controller,controller_global`
- 潮流計算によって求まった各バスのパラメータの定常値`x_ss,V_ss,I_ss`
- その他にクラス内の関数を実行するために必要なパラメータ

などがあり、さらに変数`bus`の中には各バスにおける定常状態でのパラメータやそのバスに付加されている機器の情報を含む変数`component`などがあります。図で表すと以下の様な感じに電力ネットワークの情報が格納されています。  
<div style="text-align: center;">
<img src="/Figures/make-1.jpg" width=100%;>
</div>

<span style="font-size: 130%; color: black;">__本章ではこの変数`net`を定義することが目標となります。__</span>  
  
それでは以下に、この変数`net`を定義する方法を難易度別に解説していきます。

## <span style="font-size: 100%; color: black;">【既存のモデルを使う】</span>
- networkクラスのインスタンスを呼び出そう。

## <span style="font-size: 100%; color: blue;">【基礎編】</span>
- <span style="font-size: 100%; color: blue;">既存のバスやコンポーネントのパラメータを自分で設定してみよう。</span>  
  ↑主にSTEP4の内容を貼り付ける
- <span style="font-size: 100%; color: blue;">既存のコントローラをネットワークに付加しよう。</span>  
  ↑主にSTEP3の内容を貼り付ける

## <span style="font-size: 100%; color: red;">【応用編】</span>
- <span style="font-size: 100%; color: red;">新しい機器を自作しよう。</span>  
  ↑主にSTEP5の内容を貼り付ける
- <span style="font-size: 100%; color: red;">新しい制御器を自作しよう。</span>  
  ↑主にSTEP6の内容を貼り付ける

---
<div style="text-align: center;">
```mermaid
graph TB
作成(電力ネットワークの構成編のページへ)
解析(電力ネットワークの解析編のページへ)
style 作成 fill:#fff,stroke:#000,stroke-width:1px
style 解析 fill:#fff,stroke:#000,stroke-width:1px
click 作成 "./make_net.md"
click 解析 "///new_Tutorials/analysis_net.md"
```
</div>