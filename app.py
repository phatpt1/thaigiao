import streamlit as st
import data  # Import dữ liệu từ file data.py cùng thư mục

# --- CẤU HÌNH TRANG ---
st.set_page_config(
    page_title=data.APP_SETTINGS["page_title"],
    page_icon=data.APP_SETTINGS["page_icon"],
    layout="centered"
)

# --- TÙY CHỈNH CSS ---
def apply_custom_css():
    st.markdown("""
        <style>
        .stApp { background-color: #FFF5EE; }
        h1 { color: #FF7F50 !important; font-family: 'Trebuchet MS', sans-serif !important; text-align: center; }
        h2, h3, h4 { color: #CD5C5C !important; text-align: center; }
        .story-box {
            background-color: #FFFFFF; padding: 30px; border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05); font-size: 18px;
            line-height: 1.8; color: #4A4A4A; text-align: justify; margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #FFB6C1 !important; color: white !important;
            border-radius: 30px !important; border: none !important;
            padding: 12px 24px !important; font-size: 18px !important; font-weight: bold !important;
            transition: all 0.3s ease; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .stButton>button:hover { background-color: #FF69B4 !important; transform: translateY(-2px); }
        div[data-baseweb="select"] > div { border-radius: 15px !important; border-color: #FF7F50 !important; background-color: #FFFFFF !important; }
        </style>
    """, unsafe_allow_html=True)

def main():
    apply_custom_css()

    # --- HEADER ---
    st.title(data.APP_SETTINGS["main_title"])
    st.markdown(f"<h4>{data.APP_SETTINGS['subtitle']}</h4>", unsafe_allow_html=True)
    st.write("---")

    # --- CHỌN TRUYỆN ---
    st.markdown("### 📚 Hôm nay mẹ con mình đọc truyện gì nào?")
    story_titles = ["-- Mở cuốn truyện --"] + list(data.STORIES.keys())
    selected_story = st.selectbox("Chọn một câu chuyện:", story_titles, label_visibility="collapsed")
    st.write("") 

    # --- HIỂN THỊ NỘI DUNG TRUYỆN ---
    if selected_story != "-- Mở cuốn truyện --":
        # Render truyện, giữ nguyên định dạng xuống dòng
        story_content = data.STORIES[selected_story].replace("\n", "<br>")
        st.markdown(f'<div class="story-box">{story_content}</div>', unsafe_allow_html=True)
        
        # --- NÚT HOÀN THÀNH ---
        st.write("")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button(data.MESSAGES["read_button"], use_container_width=True):
                st.success(data.MESSAGES["success_msg"])
                st.balloons() 

if __name__ == "__main__":
    main()