import streamlit as st
from ui.ui_functions import footer
from core.setup_llm import setup_conversation, setup_model
from config.options import get_options
from core.chat_core import run_conversation
from config.settings import settings


def setup_page():
    st.set_page_config(page_title="Separo ChatBot", page_icon="media/bot profile.png")

    st.markdown("""
    <h1 style="text-align:center; font-size:45px; margin-top: 0; margin-bottom: 10px;">
    Welcome to <span style="
        background: linear-gradient(to right, green 25%, red);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size:52px;
    ">Separo</span> ChatBot
    </h1>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <style>
    div[role=radiogroup] > label > div:first-child {
        background-color: #22c55e !important;
        border: 2px solid #16a34a !important;
    }
    </style>
    """, unsafe_allow_html=True)

    footer()


def show_first_message(language_choice):

    if "last_language" not in st.session_state:
        st.session_state.last_language = None
    if st.session_state.last_language != language_choice:
        welcome_messages = {
            "English": "Hello, I'm Separo. I'm ready to help you!",
            "Persian": "!سلام، من سپارو هستم. آماده‌ام که به شما کمک کنم",
            "French": "Bonjour, je suis Separo. Je suis prêt à vous aider!",
            "Spanish": "¡Hola, soy Separo. Estoy listo para ayudarte!",
            "German": "Hallo, ich bin Separo. Ich bin bereit, dir zu helfen!",
            "Italian": "Ciao, sono Separo. Sono pronto ad aiutarti!",
            "Portuguese": "Olá, eu sou Separo. Estou pronto para ajudá-lo!",
            "Russian": "Привет, я Сепаро. Я готов помочь вам!",
            "Chinese": "你好，我是Separo。我准备好帮助你了！",
            "Japanese": "こんにちは、私はSeparoです。お手伝いする準備ができています！",
            "Korean": "안녕하세요, 저는 Separo입니다. 도움을 드릴 준비가 되어 있습니다!",
            "Arabic": "مرحباً، أنا سبارو. أنا مستعد لمساعدتك!",
            "Hindi": "नमस्ते, मैं Separo हूं। मैं आपकी मदद के लिए तैयार हूं!",
            "Turkish": "Merhaba, ben Separo. Size yardım etmeye hazırım!",
            "Dutch": "Hallo, ik ben Separo. Ik ben klaar om je te helpen!",
            "Swedish": "Hej, jag är Separo. Jag är redo att hjälpa dig!",
            "Norwegian": "Hei, jeg er Separo. Jeg er klar til å hjelpe deg!",
            "Danish": "Hej, jeg er Separo. Jeg er klar til at hjælpe dig!",
            "Polish": "Cześć, jestem Separo. Jestem gotowy, aby Ci pomóc!",
            "Czech": "Ahoj, jsem Separo. Jsem připraven ti pomoci!",
            "Hungarian": "Helló, én vagyok Separo. Készen állok segíteni neked!",
            "Greek": "Γεια σας, είμαι ο Separo. Είμαι έτοιμος να σας βοηθήσω!",
            "Hebrew": "שלום, אני Separo. אני מוכן לעזור לך!",
            "Thai": "สวัสดี ฉันคือ Separo ฉันพร้อมที่จะช่วยคุณ!",
            "Vietnamese": "Xin chào, tôi là Separo. Tôi sẵn sàng giúp đỡ bạn!",
            "Indonesian": "Halo, saya Separo. Saya siap membantu Anda!",
            "Malay": "Halo, saya Separo. Saya bersedia membantu anda!",
            "Filipino": "Kumusta, ako si Separo. Handa akong tumulong sa iyo!",
            "Ukrainian": "Привіт, я Сепаро. Я готовий допомогти вам!",
            "Romanian": "Salut, sunt Separo. Sunt gata să te ajut!"
        }
        
        message = welcome_messages.get(language_choice, welcome_messages["English"])
        st.chat_message("assistant", avatar="media/bot profile.png").write(message)


def show_message(role, content):
    if role == "user":
        st.chat_message("user", avatar="media/user profile.png").write(content)
    else:
        assistant_msg = st.chat_message("assistant", avatar="media/bot profile.png")
        if "$" in content or "\\" in content:
            assistant_msg.markdown(content, unsafe_allow_html=True)
        else:
            assistant_msg.write(content)


def show_chat_history():
    for msg in st.session_state.memory.chat_memory.messages:
        if msg.type == "human":
            show_message("user", msg.content)
        else:
            show_message("assistant", msg.content)


def run_chat():
    setup_page()
    
    with st.sidebar:
        st.markdown("### Chat Options")
        language_choice, model_id, assistant_mode_choice = get_options()
    
    api_key = settings.get_api_key()
    if not api_key:
        st.warning("⚠️ **API Key Required**")
        st.info("Please configure your Groq API key in the Options section to start chatting.")
        st.markdown("""
        **How to get your API key:**
        1. Go to [console.groq.com](https://console.groq.com)
        2. Sign up or log in to your account
        3. Navigate to API Keys section
        4. Create a new API key
        5. Copy and paste it in the Options section above
        """)
        return
    
    try:
        llm = setup_model(model_id)
        conversation = setup_conversation(llm=llm)
        show_first_message(language_choice)
        setup_conversation(llm)
        show_chat_history()

        prompt = st.chat_input("Say something")
        if prompt:
            response = run_conversation(conversation, language_choice, prompt, assistant_mode_choice)
            show_message("user", prompt)
            show_message("assistant", response)
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")