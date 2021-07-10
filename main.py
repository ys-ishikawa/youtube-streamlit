import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Streamlit 入門')
# st.write('DataFrame')
# st.write('Display Image')
# st.write('Interative Widgets')
st.write('プログレスバーの表示')
'Start'

# 空を入れる
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.05)
'Done!'

# st.sidebarとすることで、サイドバーに表示
# text = st.text_input('あなたの趣味は？')
# condition = st.slider('あなたの今の調子は？',0 , 100, 50)
# 'あなたの趣味は', text, 'です。'
# 'コンディション: ', condition

# option = st.selectbox(
#     'あなたが好きな数字は？', 
#     list(range(1, 11)),
# )
# 'あなたの好きな数字は', option, 'です。'

# if st.checkbox('Show Image'):
#     img = Image.open('コンポーネント思考.png')
#     st.image(img, caption='Sample Image', use_column_width=True)

# DataFrameを用意
# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# df = pd.DataFrame(
#     # 東京都新宿付近でプロットできるように（緯度、経度）
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.write(df)

# writeでもOKだが、dataframeであれば、引数を指定できる
# st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)

# staticな表を作りたい時は、tableでも
# st.table(df)

# 折れ線グラフ
# st.line_chart(df)

# マッピング
# st.map(df)


# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

# １列に複数カラムをレイアウトする
left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ内容1を書く')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ内容2を書く')