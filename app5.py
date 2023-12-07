import streamlit as st
import random
import time
from datetime import datetime
import pytz

timezone = "Asia/Tokyo"
tz = pytz.timezone(timezone)

current_time = datetime.now(tz).strftime("%H:%M")
times = datetime.now(tz).strftime("%H")
hours1 = int(times) + 1


#道具箱
hours2 =  hours1 + 1
hours3 = hours2 + 1
hours4 = hours3 + 1
hours5 = hours4 + 1
hours6 = hours5 + 1

st.markdown(f"<h1 style='text-align:center;'>{current_time}</h1>", unsafe_allow_html=True)

templates02 = {
    "勉強": ["教科書を読んでみてはいかがですか", "演習問題を解いてみましょう", "ノートまとめをしてみましょう", ],
    "運動": ["ジョギングをしてみましょう", "ストレッチをして体を柔らかくしてみましょうと体幹トレーニングをしてみてはいかがでしょうか", ],
    "外出": ["映画に行に行きましょう", "図書館に行って今日は１０冊本を読みましょう", "散歩をして新しい発見をしてみましょう"],
    "暇": ["ぼっけとするのも手ですよ", "こんな日は新しいことに取り組んでみましょう", "運動をしてみてはいかがですか"],
    "何もしたくない": ["ぼっけとするのも手ですよ", "こんな日は新しいことに取り組んでみましょう", "課題は絶対終わってないのではないでしょうか"],
    "遊び": ["運動をしてみてはいかがですか", "外出してみてもいいですね。散歩をしてみましょう", ],
}

st.write("")
st.write("")
time.sleep(2)

# 質問
listen = "AI「今日は何がしたいですか？」"
st.markdown(f"<font color='green'>{listen}</font>", unsafe_allow_html=True)
user_input01 = st.text_input("下に入力")

# 入力された文章からキーワードを抽出
keywords = ["勉強", "運動", "外出", "暇", "遊び", "何もしたくない"]  # キーワードは適宜拡充してください
found_keywords = [kw for kw in keywords if kw in user_input01]

selected_template02 = None

# ユーザーが選択したキーワードをもとに予定を生成
if found_keywords:
    selected_template02 = random.choice(found_keywords)
    random_plan02 = random.choice(templates02[selected_template02])
else:
    time.sleep(2)
    st.warning("AI 「キーワードが見つかりませんでした。もう一度試してください。」")

time.sleep(2)

st.write("")
st.write("")
time.sleep(2)

with st.form("additional_plan_form"):
    life1 = st.write("予定生成を開始してください")

    next_button = st.form_submit_button("生成開始")

    if next_button:
        teian2 = f"「今日の予定は '{selected_template02}' のテーマにしてみましょう、'{random_plan02}'」　"
        st.markdown(f'<font color="green">{teian2}</font>', unsafe_allow_html=True)

        time.sleep(2)
        st.write("")

        keikaku = f"AI 「ではキリがいいので{hours1}時からから生活アシストをしますね」"
        st.markdown(f'<font color="green">{keikaku}</font>', unsafe_allow_html=True)
        st.write("")
        st.write("")

        # 変数に変換
        hensu = selected_template02
        hensu2 = random_plan02

        if hensu == "勉強":
            time.sleep(3)
            st.write("AI「 ”勉強”が選択されました。予定を生成し始めます」")

            if hensu2 == "教科書を読んでみてはいかがですか" or "演習問題を解いてみましょう":
                time.sleep(3)
                st.write(
                    f"{hours1}:00 : 10ページ読む  \n{hours2}:00　: 休憩（趣味の時間）  \n{hours3}:00 : 復習  \n{hours4}:00 : できるなら問題演習   \n{hours5}:00 : 休憩（趣味の時間）  \n{hours6}:00　: 一日の復習　")
                time.sleep(3)
                st.warning("予定はあくまで提案として生活をしてみてください")

            else:
                time.sleep(3)
                st.write(
                    f"{hours1}:00 :今までの範囲を復習  \n{hours2}:00 : 休憩（趣味の時間）　ノートまとめをする  \n{hours3}:00　: ある程度分かってきたら問題に取り組む  \n{hours4}:00　: 問題演習に取り組む  \n{hours5}:00 : 休憩（趣味の時間）  \n{hours6}:00 : 今日一日の復習と振り返り")
                time.sleep(3)
                st.warning("予定はあくまで提案として生活をしてみてください")

        elif hensu == "運動":
            time.sleep(3)
            st.write("AI「　”運動”が選択されました。予定を生成し始めます」")

            if hensu2 == "ジョギングをしてみましょう":
                time.sleep(3)
                st.write(f"{hours1}:00 : 目的地を決めて走り出す  \n{hours2}:00 : 休憩（体を休める）  \n{hours3}:00 : 帰宅を始める　　\n{hours4}:00 : 休憩（趣味の時間")
                time.sleep(3)
                st.warning("予定はあくまで提案として生活をしてみてください")
                    
            else:
                time.sleep(3)
                st.write(f"{hours1}:00　: ヨガに取り組む  \n{hours2}:00 : ストレッチをしたら温かいお茶を飲む \n{hours3}:00 : 休憩 \n{hours4}:00 : ほかのことに取り組む 　\n{hours5}:00 : 休憩  \n{hours6}:00 : 今日行った体操をもう一度行う")
                time.sleep(3)
                st.warning("予定はあくまで提案として生活をしてみてください")    
                 #外出する場合と遊ぶ場合の予定生成               
        elif hensu == "外出" or "遊び":
            time.sleep(3)
            st.write("AI「 ”外出”が選択されました。予定を生成し始めます」")
                
                    
            if hensu2 == "散歩をして新しい発見をしてみましょう" or "外出してみてもいいですね。散歩をしてみましょう":
                time.sleep(3)
                st.write(f"{hours1}:00 : 散歩を開始  \n{hours2}:00　： 近辺の公園などで休憩  \n{hours3}:00　： 公園の周りなどを散策  \n{hours4}:00  ： 帰宅開始  \n{hours5}:00　： 一日の反省と記録  \n{hours6}:00　： 自由時間")
                time.sleep(3)
                st.warning("予定はあくまで提案として生活をしてみてください")
                    
            elif hensu2 == "映画に行に行きましょう":
                time.sleep(3)
                st.write(f"{hours1}:00　： 近くの映画館へ移動  \n{hours2}:00　： 好きな映画を見ましょう  \n{hours3}:00 : 好きな映画を見ましょう  \n{hours4}:00　： 好きな映画を見ましょう  \n{hours5}:00　： 好きな映画を見ましょう  \n{hours6}:00 : 感想を書いてレビューをしましょう")
                time.sleep(3)
                st.warning("予定はあくまで提案として生活をしてみてください")
                    
            elif hensu2 =="図書館に行って今日は１０冊本を読みましょう":
                time.sleep(3)
                st.write(f"{hours1}:00　： まずお近くの図書館へ移動  \n{hours2}:00　： 本を読み進める  \n{hours3}:00 : 本を読み進める  \n{hours4}:00 ： 本を読み進める  \n{hours5}:00　： 本を読み進める  \n{hours6}:00 :　残りはお家で読みましょう♪")
                time.sleep(3)
                st.warning("予定はあくまで提案として生活をしてみてください")
                    
            elif hensu2 == "運動をしてみてはいかがですか":
                time.sleep(3)
                st.write(f"{hours1}:00　： 準備体操・アップ  \n{hours2}:00 ： 現在地から１０キロ先まで走りましょう  \n{hours3}:00 ： 水分補給と休憩  \n{hours4}:00 ： 帰宅  \n{hours5}:00　： 記録と反省  \n{hours6}:00　： 記録と反省")
                time.sleep(3)
                st.warning("予定はあくまで提案として生活をしてみてください")    
                                
            elif hensu2 == "何もしたくない":
                time.sleep(3)
                st.write("AI「 ”何もしたくない”が選択されました。予定を生成し始めます」")
                    
                if hensu2 == "課題は絶対終わってないのではないでしょうか":
                    time.sleep(3)
                    st.write(f"{hours1}:00 : teamsの確認　 \n{hours2}:00 ： 課題にとりかかる　 \n{hours3}:00 ： 休憩（趣味の時間） \n{hours4}:00 ： 課題にとりかかる 　\n{hours5}:00　： 課題にとりかかる  \n{hours6}:00 : 一日の反省と復習")
                    time.sleep(2)
                    st.write("課題が終わってるのであればテーマをより明確化して再度質問してみましょう")
                    time.sleep(3)
                    st.warning("予定はあくまで提案として生活をしてみてください")
                    
                elif hensu2 == "ぼっけとするのも手ですよ":
                    time.sleep(3)
                    st.write(f"{hours1}:00　: ボケっとする場所を選び移動しましょう  \n{hours2}:00 : ボケっと開始　 \n{hours3}:00 : 今後の将来について考える　 \n{hours4}:00　: 過去について振り返る 　\n{hours5}:00　: 今何ができるかを考える  \n{hours6}:00　: お家に帰る")
                    time.sleep(3)
                    st.warning("予定はあくまで提案として生活をしてみてください")
                    
                    #user_inputでどんな新しいことに取り組むか聞かなければならない
            elif hensu2 == "こんな日は新しいことに取り組んでみましょう":
                time.sleep(3)
                st.warning("ユーザーの具体的な新しいことが把握できないので省略させていただきます")
                        
                        
            
        