import streamlit as st

# 假设的新闻内容
international_news = [
    {"title": "International News Headline 1", "content": "Content of International News 1"},
    {"title": "International News Headline 2", "content": "Content of International News 2"}
]

sports_news = [
    {"title": "Sports News Headline 1", "content": "Content of Sports News 1"},
    {"title": "Sports News Headline 2", "content": "Content of Sports News 2"}
]

tech_news = [
    {"title": "Tech News Headline 1", "content": "Content of Tech News 1"},
    {"title": "Tech News Headline 2", "content": "Content of Tech News 2"}
]

# 设置网页标题
st.title('Simple News Website')

# 使用侧边栏选择新闻类别
option = st.sidebar.selectbox('Choose a news category', ('International', 'Sports', 'Tech'))

# 根据选择显示新闻
if option == 'International':
    st.header('International News')
    for news_item in international_news:
        st.subheader(news_item['title'])
        st.write(news_item['content'])
elif option == 'Sports':
    st.header('Sports News')
    for news_item in sports_news:
        st.subheader(news_item['title'])
        st.write(news_item['content'])
elif option == 'Tech':
    st.header('Tech News')
    for news_item in tech_news:
        st.subheader(news_item['title'])
        st.write(news_item['content'])
