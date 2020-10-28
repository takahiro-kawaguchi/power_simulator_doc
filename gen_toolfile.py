import os

tool_name = [
    "arrayfun",
    "cell2var",
    "cellfun",
    "darrayfun",
    "dcellfun",
    "deal_cell",
    "diag_cell",
    "harrayfun",
    "hcat_cell",
    "hcellfun",
    "idx2f",
    "Reporter",
    "sample2f",
    "select_apply",
    "select_value",
    "times_matrix",
    "varrayfun",
    "vcat_cell",
    "vcellfun",
    "zeros",
]


for tool in tool_name:
    f = open('./docs/Tools/' + tool + '.md', mode='w')
    contents = [
        "# tools." + tool + "\n",
        "" + "\n",
        "## 構文" + "\n",
        "" + "\n",
        "## 説明" + "\n",
        "" + "\n",
        "## 例" + "\n",
        "" + "\n",
        "## 入力引数" + "\n",
        "" + "\n",
        "## 出力引数" + "\n",
    ]
    f.writelines(contents)
    f.close()

f = open('./docs/Tools/tools.md', mode='w')
f.write('# ツール群\n\n')
for tool in tool_name:
    f.write('- ['+tool+'](./'+tool+'.md)\n\n')
f.close()
