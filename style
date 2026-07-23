# ==============================
# app.py (1/5)
# ==============================

import streamlit as st
import requests
import random
import json
import base64
from openai import OpenAI

# ------------------------
# PAGE
# ------------------------

st.set_page_config(
    page_title="AI 스타일 추천기",
    page_icon="👕",
    layout="wide"
)

# ------------------------
# OPENAI
# ------------------------

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# ------------------------
# WEATHER
# ------------------------

OPENWEATHER_KEY = st.secrets["OPENWEATHER_API_KEY"]

def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={OPENWEATHER_KEY}&units=metric&lang=kr"
    )

    try:

        data = requests.get(url, timeout=10).json()

        return {
            "weather": data["weather"][0]["description"],
            "temp": round(data["main"]["temp"])
        }

    except:

        return {
            "weather":"맑음",
            "temp":23
        }

# ------------------------
# STYLE
# ------------------------

st.markdown("""

<style>

@font-face{
font-family:Nanum;
src:url("youtube/NanumGothic.ttf");
}

html,body,[class*="css"]{

font-family:Nanum;

}

.stApp{

background:
linear-gradient(
135deg,
#fffaf7,
#eef3ff,
#ffffff
);

}

.box{

background:white;

padding:25px;

border-radius:20px;

box-shadow:0 15px 30px rgba(0,0,0,.08);

margin-bottom:20px;

}

.title{

font-size:42px;

font-weight:800;

text-align:center;

margin-bottom:20px;

}

.subtitle{

font-size:18px;

color:#666;

}

</style>

""",unsafe_allow_html=True)

# ------------------------
# SESSION
# ------------------------

if "style_data" not in st.session_state:

    st.session_state.style_data={}

if "images" not in st.session_state:

    st.session_state.images={}

if "seed" not in st.session_state:

    st.session_state.seed=random.randint(1,999999)

# ------------------------
# MBTI
# ------------------------

MBTI=[
"INTJ","INTP","ENTJ","ENTP",
"INFJ","INFP","ENFJ","ENFP",
"ISTJ","ISFJ","ESTJ","ESFJ",
"ISTP","ISFP","ESTP","ESFP"
]

# ------------------------
# TITLE
# ------------------------

st.markdown(
"<div class='title'>👕 AI 스타일 추천기</div>",
unsafe_allow_html=True
)

# ------------------------
# LAYOUT
# ------------------------

left,right=st.columns([1,1.5])

with left:

    st.markdown("## 사용자 정보")

    mbti=st.selectbox(
        "MBTI",
        MBTI
    )

    animal=st.text_input(
        "좋아하는 동물",
        placeholder="예) 고양이"
    )

    city=st.text_input(
        "도시",
        value="Seoul"
    )

    weather=get_weather(city)

    st.info(
        f"""
현재 날씨

☁️ {weather["weather"]}

🌡️ {weather["temp"]}℃
"""
    )

    generate=st.button(
        "✨ 스타일 생성",
        use_container_width=True
    )

    regenerate=st.button(
        "🔄 다시 생성",
        use_container_width=True
    )

# ------------------------
# MOODS
# ------------------------

MOODS={

"😊 기쁨":{

"name":"기쁨",

"background":"warm sunset, flowers, dreamy park, golden light"

},

"😢 슬픔":{

"name":"슬픔",

"background":"rainy window, blue tone, emotional street"

},

"😡 화남":{

"name":"화남",

"background":"red neon city, cyberpunk lights"

},

"😴 무기력":{

"name":"무기력",

"background":"foggy cafe, gray mood, cozy"

}

}

tabs=st.tabs(list(MOODS.keys()))

result_boxes=[]

for tab in tabs:

    with tab:

        img=st.empty()

        txt=st.empty()

        result_boxes.append((img,txt))# ==============================
# app.py (2/5)
# ==============================

def make_prompt(
    mbti,
    animal,
    weather,
    temp,
    mood,
    background,
    seed
):

    return f"""
당신은 세계 최고의 패션 스타일리스트입니다.

사용자 정보

MBTI : {mbti}

좋아하는 동물 : {animal}

현재 날씨 : {weather}

현재 기온 : {temp}도

현재 감정 : {mood}

아래 형식의 JSON만 출력하세요.

{{
"title":"",
"top":"",
"bottom":"",
"shoes":"",
"accessory":"",
"description":"",
"origin":"",
"trend_period":"",
"trend_reason":"",
"image_prompt":""
}}

조건

- 한국인이 좋아할 감성

- 계절을 반드시 고려

- 기온을 반드시 고려

- 동물의 분위기를 은은하게 반영

- MBTI를 반영

- 이전 결과와 완전히 다른 스타일

- 랜덤값 {seed}

이미지 프롬프트는 영어로 작성

배경은

{background}

포즈는 전신

고품질

패션 일러스트

editorial

clean background
"""


# ---------------------------------------
# GPT
# ---------------------------------------

def generate_style(

    mbti,

    animal,

    weather,

    temp,

    mood,

    background,

    seed

):

    prompt=make_prompt(

        mbti,

        animal,

        weather,

        temp,

        mood,

        background,

        seed

    )

    response=client.chat.completions.create(

        model="gpt-4.1",

        temperature=1.25,

        response_format={

            "type":"json_object"

        },

        messages=[

            {

                "role":"system",

                "content":"당신은 최고의 패션 디렉터입니다."

            },

            {

                "role":"user",

                "content":prompt

            }

        ]

    )

    text=response.choices[0].message.content

    return json.loads(text)


# ---------------------------------------
# IMAGE
# ---------------------------------------

def generate_image(prompt):

    result=client.images.generate(

        model="gpt-image-1",

        prompt=prompt,

        size="1024x1024"

    )

    image_bytes=base64.b64decode(

        result.data[0].b64_json

    )

    return image_bytes
# ==============================
# app.py (3/5)
# ==============================

# ---------------------------------------
# GENERATE
# ---------------------------------------

if generate:

    st.session_state.seed = random.randint(1, 999999)

    with st.spinner("AI가 스타일을 만들고 있습니다..."):

        for i, (tab_name, info) in enumerate(MOODS.items()):

            mood = info["name"]
            background = info["background"]

            data = generate_style(
                mbti=mbti,
                animal=animal,
                weather=weather["weather"],
                temp=weather["temp"],
                mood=mood,
                background=background,
                seed=st.session_state.seed + i
            )

            image = generate_image(
                data["image_prompt"]
            )

            st.session_state.style_data[mood] = data
            st.session_state.images[mood] = image

# ---------------------------------------
# REGENERATE
# ---------------------------------------

if regenerate:

    st.session_state.seed = random.randint(1, 999999)

    st.rerun()

# ---------------------------------------
# SHOW
# ---------------------------------------

for idx, (tab_name, info) in enumerate(MOODS.items()):

    mood = info["name"]

    with tabs[idx]:

        if mood in st.session_state.style_data:

            data = st.session_state.style_data[mood]

            col1, col2 = st.columns([1.2, 1])

            with col1:

                st.image(
                    st.session_state.images[mood],
                    use_container_width=True
                )

            with col2:

                st.markdown(f"## 👗 {data['title']}")

                st.markdown("---")

                st.markdown(f"### 👕 상의")
                st.write(data["top"])

                st.markdown(f"### 👖 하의")
                st.write(data["bottom"])

                st.markdown(f"### 👟 신발")
                st.write(data["shoes"])

                st.markdown(f"### 👜 액세서리")
                st.write(data["accessory"])

                st.markdown("---")

                st.markdown("### ✨ 코디 설명")
                st.write(data["description"])

                st.markdown("### 📚 스타일 유래")
                st.write(data["origin"])

                st.markdown("### 📅 유행 시기")
                st.write(data["trend_period"])

                st.markdown("### 🔥 유행한 이유")
                st.write(data["trend_reason"])

        else:

            st.info("왼쪽에서 '✨ 스타일 생성' 버튼을 눌러주세요.")
# ==============================
# app.py (4/5)
# ==============================

# ---------------------------------------
# IMAGE PROMPT ENHANCER
# ---------------------------------------

STYLE_SUFFIX = """
full body fashion illustration,
Korean fashion,
editorial magazine,
high-end clothing,
extremely detailed,
beautiful face,
realistic fabric,
natural pose,
soft lighting,
luxury fashion,
masterpiece,
best quality,
8k,
clean composition,
centered subject,
fashion photography style,
professional styling,
sharp focus,
no text,
no watermark
"""

def build_image_prompt(data):

    return f"""
{data["image_prompt"]}

{STYLE_SUFFIX}
"""


# ---------------------------------------
# GENERATE IMAGE AGAIN
# ---------------------------------------

def regenerate_current_styles():

    for mood in MOODS:

        info = MOODS[mood]

        data = generate_style(

            mbti=mbti,

            animal=animal,

            weather=weather["weather"],

            temp=weather["temp"],

            mood=info["name"],

            background=info["background"],

            seed=random.randint(1,999999)

        )

        img = generate_image(

            build_image_prompt(data)

        )

        st.session_state.style_data[info["name"]] = data

        st.session_state.images[info["name"]] = img


if regenerate:

    with st.spinner("새로운 스타일을 만드는 중입니다..."):

        regenerate_current_styles()

    st.rerun()


# ---------------------------------------
# DOWNLOAD
# ---------------------------------------

for mood in st.session_state.images:

    st.download_button(

        label=f"💾 {mood} 이미지 저장",

        data=st.session_state.images[mood],

        file_name=f"{mood}.png",

        mime="image/png"

    )


# ---------------------------------------
# RANDOM TIP
# ---------------------------------------

tips=[

"레이어드를 하면 훨씬 세련된 분위기가 납니다.",

"액세서리를 하나만 추가해도 분위기가 달라집니다.",

"신발 색상을 상의와 맞추면 안정감이 생깁니다.",

"오버핏은 대부분의 체형에서 좋은 비율을 만들어줍니다.",

"톤온톤 코디는 실패 확률이 매우 낮습니다."

]

st.markdown("---")

st.info(
"💡 오늘의 스타일 팁\n\n"
+random.choice(tips)
)
# ==============================
# app.py (5/5)
# ==============================

# ---------------------------------------
# FOOTER
# ---------------------------------------

st.markdown("---")

st.caption(
"""
Made with ❤️ using

• Streamlit

• OpenAI GPT-4.1

• GPT Image

• OpenWeather API
"""
)

# ---------------------------------------
# CACHE
# ---------------------------------------

@st.cache_data(ttl=600)
def cached_weather(city):
    return get_weather(city)

# ---------------------------------------
# ERROR
# ---------------------------------------

try:
    pass

except Exception as e:

    st.error("오류가 발생했습니다.")

    st.exception(e)

# ---------------------------------------
# EMPTY STATE
# ---------------------------------------

if not st.session_state.style_data:

    st.markdown(
    """
    ## 👋 사용 방법

    1. MBTI 선택
    2. 좋아하는 동물 입력
    3. 도시 입력
    4. '✨ 스타일 생성' 클릭
    5. 감정 탭(😊😢😡😴)을 넘기며 스타일 확인
    6. '🔄 다시 생성'으로 새로운 스타일 추천
    """
    )

# ---------------------------------------
# REQUIREMENTS.TXT
# ---------------------------------------
"""
streamlit>=1.45.0
openai>=1.50.0
requests>=2.32.0
Pillow>=10.4.0
"""

# ---------------------------------------
# .streamlit/secrets.toml
# ---------------------------------------
"""
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
OPENWEATHER_API_KEY="YOUR_OPENWEATHER_API_KEY"
"""
