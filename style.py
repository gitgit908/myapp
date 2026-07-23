# ==========================================
# myapp.py (1/5)
# AI 없이 동작하는 스타일 추천기
# ==========================================

import streamlit as st
import random
import os

st.set_page_config(
    page_title="스타일 추천기",
    page_icon="👕",
    layout="wide"
)

# -------------------------
# CSS
# -------------------------

st.markdown("""
<style>

.stApp{

background:linear-gradient(
135deg,
#FFF6F3,
#EEF5FF,
#FFFFFF
);

}

.title{

font-size:45px;

font-weight:900;

text-align:center;

margin-bottom:20px;

}

.card{

background:white;

padding:20px;

border-radius:20px;

box-shadow:0px 10px 25px rgba(0,0,0,.08);

}

</style>
""",unsafe_allow_html=True)

# -------------------------
# DATA
# -------------------------

MBTI=[

"INTJ","INTP","ENTJ","ENTP",

"INFJ","INFP","ENFJ","ENFP",

"ISTJ","ISFJ","ESTJ","ESFJ",

"ISTP","ISFP","ESTP","ESFP"

]

ANIMALS={

"고양이":"미니멀",

"강아지":"캐주얼",

"토끼":"러블리",

"여우":"시크",

"곰":"오버핏",

"늑대":"다크",

"햄스터":"아기자기"

}

MOODS=[

"😊 기쁨",

"😢 슬픔",

"😡 화남",

"😴 무기력"

]

# -------------------------
# SESSION
# -------------------------

if "result" not in st.session_state:

    st.session_state.result={}

# -------------------------
# TITLE
# -------------------------

st.markdown(
'<div class="title">👕 스타일 추천기</div>',
unsafe_allow_html=True
)

left,right=st.columns([1,1.5])

with left:

    mbti=st.selectbox(
        "MBTI",
        MBTI
    )

    animal=st.selectbox(
        "좋아하는 동물",
        list(ANIMALS.keys())
    )

    temp=st.slider(
        "현재 온도",
        -10,
        40,
        22
    )

    weather=st.selectbox(
        "날씨",
        [

        "맑음",

        "흐림",

        "비",

        "눈"

        ]

    )

    mood=st.selectbox(
        "기분",
        MOODS
    )

    create=st.button(
        "✨ 스타일 추천",
        use_container_width=True
    )

    again=st.button(
        "🔄 다시 생성",
        use_container_width=True
    )# ==========================================
# myapp.py (2/5)
# ==========================================

STYLE_INFO={

"미니멀":{

"title":[
"모던 미니멀 룩",
"감성 데일리 룩",
"뉴트럴 클래식"
],

"top":[
"화이트 셔츠",
"베이지 니트",
"오버핏 맨투맨"
],

"bottom":[
"슬랙스",
"와이드 팬츠",
"청바지"
],

"shoes":[
"화이트 스니커즈",
"로퍼",
"독일군 스니커즈"
],

"acc":[
"실버 목걸이",
"가죽 시계",
"캔버스백"
]

},

"캐주얼":{

"title":[
"캠퍼스 룩",
"캐주얼 데일리",
"주말 산책 룩"
],

"top":[
"후드티",
"맨투맨",
"반팔 티셔츠"
],

"bottom":[
"조거팬츠",
"청바지",
"카고팬츠"
],

"shoes":[
"컨버스",
"뉴발란스",
"러닝화"
],

"acc":[
"볼캡",
"백팩",
"에코백"
]

},

"러블리":{

"title":[
"러블리 코디",
"소프트 데이트룩",
"파스텔 감성"
],

"top":[
"가디건",
"니트",
"블라우스"
],

"bottom":[
"플리츠 스커트",
"와이드 팬츠",
"청치마"
],

"shoes":[
"메리제인",
"플랫슈즈",
"스니커즈"
],

"acc":[
"리본",
"진주 목걸이",
"미니백"
]

},

"시크":{

"title":[
"시크 모노톤",
"도시 감성",
"블랙 스타일"
],

"top":[
"블랙 셔츠",
"터틀넥",
"자켓"
],

"bottom":[
"블랙 슬랙스",
"코팅진",
"와이드 팬츠"
],

"shoes":[
"첼시부츠",
"더비슈즈",
"스니커즈"
],

"acc":[
"선글라스",
"실버링",
"가죽백"
]

},

"오버핏":{

"title":[
"힙한 오버핏",
"편안한 스트릿",
"꾸안꾸"
],

"top":[
"오버핏 후드",
"루즈핏 니트",
"오버핏 셔츠"
],

"bottom":[
"와이드 팬츠",
"카고팬츠",
"조거팬츠"
],

"shoes":[
"농구화",
"운동화",
"어글리슈즈"
],

"acc":[
"비니",
"크로스백",
"볼캡"
]

},

"다크":{

"title":[
"다크 스트릿",
"올블랙 룩",
"모던 시크"
],

"top":[
"블랙 후드",
"레더 자켓",
"검정 셔츠"
],

"bottom":[
"블랙진",
"슬랙스",
"카고팬츠"
],

"shoes":[
"워커",
"부츠",
"검정 스니커즈"
],

"acc":[
"체인목걸이",
"반지",
"가죽팔찌"
]

},

"아기자기":{

"title":[
"큐트룩",
"소프트 캐주얼",
"포근한 스타일"
],

"top":[
"파스텔 니트",
"후드집업",
"맨투맨"
],

"bottom":[
"청바지",
"와이드팬츠",
"반바지"
],

"shoes":[
"운동화",
"캔버스화",
"스니커즈"
],

"acc":[
"키링",
"에코백",
"볼캡"
]

}

}

SEASON={

"summer":[
"린넨 소재를 사용해 시원한 느낌을 살렸습니다.",
"가볍고 통풍이 좋은 코디입니다."
],

"spring":[
"부드러운 색감으로 봄 분위기를 표현했습니다.",
"산뜻한 느낌을 주는 코디입니다."
],

"fall":[
"따뜻한 브라운 계열을 사용했습니다.",
"가을 감성에 잘 어울리는 스타일입니다."
],

"winter":[
"보온성을 고려한 코디입니다.",
"포근한 겨울 느낌을 살렸습니다."
]

}# ==========================================
# myapp.py (3/5)
# ==========================================

def get_season(temp):

    if temp >= 28:
        return "summer"

    elif temp >= 18:
        return "spring"

    elif temp >= 8:
        return "fall"

    else:
        return "winter"


def make_style():

    style = ANIMALS[animal]

    info = STYLE_INFO[style]

    season = get_season(temp)

    if mood == "😊 기쁨":
        color = "밝은 파스텔 계열"
    elif mood == "😢 슬픔":
        color = "블루 & 그레이 계열"
    elif mood == "😡 화남":
        color = "블랙 & 레드 계열"
    else:
        color = "베이지 & 크림 계열"

    if weather == "비":
        item = "우산"
    elif weather == "눈":
        item = "머플러"
    elif weather == "흐림":
        item = "가디건"
    else:
        item = "선글라스"

    result = {

        "title": random.choice(info["title"]),

        "top": random.choice(info["top"]),

        "bottom": random.choice(info["bottom"]),

        "shoes": random.choice(info["shoes"]),

        "acc": random.choice(info["acc"]),

        "weather_item": item,

        "color": color,

        "season_desc": random.choice(SEASON[season]),

        "origin": random.choice([

            "1990년대 스트릿 패션에서 영향을 받은 스타일입니다.",

            "한국의 미니멀 패션과 북유럽 감성을 결합한 스타일입니다.",

            "일본 캐주얼 패션과 한국 데일리룩을 조합한 스타일입니다.",

            "SNS 감성 패션에서 많은 사랑을 받은 스타일입니다."

        ]),

        "trend": random.choice([

            "2019~2021",

            "2020~2022",

            "2022~2024",

            "2023~현재"

        ]),

        "reason": random.choice([

            "편안하면서도 세련된 분위기를 연출할 수 있어서",

            "SNS와 숏폼 콘텐츠에서 자주 소개되어서",

            "실용성과 디자인을 모두 만족했기 때문에",

            "누구나 쉽게 따라 입을 수 있는 스타일이었기 때문입니다."

        ])

    }

    return result


if create or again:

    st.session_state.result = make_style()# ==========================================
# myapp.py (4/5)
# ==========================================

with right:

    if st.session_state.result:

        data = st.session_state.result

        st.markdown("## 👕 추천 코디")

        # -------------------------
        # 이미지 표시
        # -------------------------

        style_name = ANIMALS[animal].lower()

        image_folder = f"images/{style_name}"

        image_list = []

        if os.path.exists(image_folder):

            for file in os.listdir(image_folder):

                if file.endswith(".png") or file.endswith(".jpg"):

                    image_list.append(
                        os.path.join(image_folder,file)
                    )

        if len(image_list)>0:

            st.image(
                random.choice(image_list),
                use_container_width=True
            )

        else:

            st.info("이미지 폴더를 추가하면 코디 이미지가 표시됩니다.")

        st.markdown("---")

        st.markdown(f"## ✨ {data['title']}")

        st.write(f"**상의** : {data['top']}")

        st.write(f"**하의** : {data['bottom']}")

        st.write(f"**신발** : {data['shoes']}")

        st.write(f"**액세서리** : {data['acc']}")

        st.write(f"**추천 아이템** : {data['weather_item']}")

        st.write(f"**추천 색상** : {data['color']}")

        st.markdown("---")

        st.subheader("📖 스타일 설명")

        st.write(data["season_desc"])

        if mbti[0]=="I":

            st.write(
                "내향적인 성향에 어울리는 차분하고 안정감 있는 스타일입니다."
            )

        else:

            st.write(
                "활동적이고 개성 있는 분위기를 강조하는 스타일입니다."
            )

        st.write(
            f"{animal}의 이미지를 은은하게 반영한 코디입니다."
        )

        st.markdown("---")

        st.subheader("📚 스타일 유래")

        st.write(data["origin"])

        st.subheader("📅 유행했던 시기")

        st.write(data["trend"])

        st.subheader("🔥 유행한 이유")

        st.write(data["reason"])

    else:

        st.info("왼쪽에서 '✨ 스타일 추천' 버튼을 눌러주세요.")# ==========================================
# myapp.py (5/5)
# ==========================================

st.markdown("---")

st.subheader("💡 오늘의 스타일 한마디")

quotes = [

"패션은 자신을 가장 먼저 소개하는 언어입니다.",

"편안한 옷이 가장 멋진 옷입니다.",

"유행은 지나가지만 스타일은 남습니다.",

"오늘의 자신감은 오늘의 코디에서 시작됩니다.",

"좋은 스타일은 작은 디테일에서 완성됩니다."

]

st.success(random.choice(quotes))

st.markdown("---")

st.subheader("⭐ 오늘의 스타일 점수")

score = random.randint(85,100)

st.progress(score/100)

st.write(f"AI 추천 점수 : **{score}점**")

st.markdown("---")

st.subheader("🎨 추천 컬러")

colors = {

"😊 기쁨":[
"아이보리",
"스카이블루",
"연노랑",
"라이트베이지"
],

"😢 슬픔":[
"네이비",
"그레이",
"블루",
"차콜"
],

"😡 화남":[
"블랙",
"버건디",
"다크레드",
"다크그레이"
],

"😴 무기력":[
"크림",
"베이지",
"카키",
"브라운"
]

}

for c in random.sample(colors[mood],2):

    st.write("🎨",c)

st.markdown("---")

st.subheader("👔 이런 사람에게 추천")

if mbti[0]=="I":

    st.write("✔ 조용하고 편안한 분위기를 좋아하는 사람")

else:

    st.write("✔ 활동적이고 개성을 표현하고 싶은 사람")

if temp>=28:

    st.write("✔ 더운 날씨에 시원하게 입기 좋은 코디")

elif temp>=18:

    st.write("✔ 가볍게 외출하기 좋은 코디")

elif temp>=8:

    st.write("✔ 일교차가 큰 날씨에 추천")

else:

    st.write("✔ 추운 겨울에 따뜻하게 입기 좋은 코디")

st.markdown("---")

st.caption(
"""
Made with ❤️ using Streamlit

AI 없이 동작하는 스타일 추천기
"""
)
