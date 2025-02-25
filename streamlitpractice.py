import streamlit as st
import pandas as pt


#侧边栏布局
#输入文本
with st.sidebar:
    name = st.text_input('请输入您的名字',key='input2')
    if name:
        st.write(f'你好，{name}')

#分页
column1,column2, column3=st.columns([10,10,10])

with column1:
    ##随便输入
    '# 我是谁？'
    a=10*30
    a
    b=100
    a+b
    [1,2,3,4,5,]

    ##标题输入
    st.title('我的网站')

    #图片输入
    st.image("G:\视频编辑大全\数字人形象\最新数字人\人物图\中式美圣5.png",width=500)

    #动态表格输入
    dat=pt.DataFrame({'姓名':['小张','小王','小李'],'年龄':[12,40,55],'爱好':['捉迷藏','游泳','打篮球']})
    st.dataframe(dat)

    #分割线
    st.divider()

    #静态表格
    st.table(dat)
    st.divider()

with column2:

    #密码输入
    pasword=st.text_input("请输入要您的密码", type='password')
    st.divider()

    #输入长文本
    text=st.text_area('请输入自我介绍')
    st.divider()

    #输入数字
    num=st.number_input('请输入您的年龄',value=100,min_value=1,max_value=150,step=5)
    if num:
        st.write(f'您的年龄是: {num} 岁')
    st.divider()
    #输入勾选框
    check=st.checkbox('同意条款')
    if check:
        st.write('感谢您同意')
    st.divider()

    #创造按钮
    button=st.button('提交')
    if button:
        st.write('提交成功')
    st.divider()

with column3:
    #单选按钮
    st.radio('您的性别是？',['男性', '女性', '跨性别'],index=None)
    st.divider()

    #单选下拉框
    contact=st.selectbox('您的联系方式有哪些？',['微信', 'QQ', '邮箱'], index=None)
    if contact:
        st.write(f'好的，我们将通过{contact} 联系您')
    st.divider()

    #多选下拉框
    fruits=st.multiselect('您喜欢的水果有哪些', ['桃子', '葡萄', '香蕉','苹果'])
    for fruit in fruits:
        st.write(f'您喜欢的水果有：{fruits}')
    st.divider()

    #滑块
    high=st.slider('您的身高是？',value=200, min_value=140, max_value=200, step= 5)
    st.divider()

    #文件上传组件

    file=st.file_uploader('请上传文件',type=['PDF','txt','gpj'])
    if file:
        st.write(f'您上传的文件内容如下：{file.read().decode('utf-8')}')

#tabax选项
tab1,tab2,tab3=st.tabs(['第一', '第二', '第三'])

with tab1:
    #图片输入
    st.image("G:\视频编辑大全\数字人形象\最新数字人\人物图\中式美圣5.png",width=500)

with tab2:
    # 滑块
    high = st.slider('您的身高是？', value=200, min_value=140, max_value=200, step=5,key='sli2')
    st.divider()

with tab3:
    # 单选下拉框
    contact = st.selectbox('您的联系方式有哪些？', ['微信', 'QQ', '邮箱'], index=None, key='sle2')
    if contact:
        st.write(f'好的，我们将通过{contact} 联系您')
    st.divider()

#折叠展开选项
with st.expander('信息'):
    contact = st.selectbox('您的联系方式有哪些？', ['微信', 'QQ', '邮箱'], index=None, key='232')
    if contact:
        st.write(f'好的，我们将通过{contact} 联系您')
    st.divider()

    # 创造按钮
    button = st.button('提交',key='46')
    if button:
        st.write('提交成功')
st.divider()

#绘画储存状态
if 'a' not in st.session_state:
    st.session_state.a=0
click=st.button('加1')
if click:
    st.session_state.a+=1
st.write(st.session_state.a)

#如何创建多页？
#可以选定一个页面作为主页，再在系统文件下创建一个目录（必须叫做pages）,把其他剩余的页面放到pages下即可。

