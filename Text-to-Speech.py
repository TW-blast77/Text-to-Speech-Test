from elevenlabs import generate, play, set_api_key
from pydub import AudioSegment
import os


set_api_key("1557cf4f516bc662637f043d97e94d73")

while True:

    a = input("輸入文字轉語音（输入 'exit' 退出）: ")

    if a.lower() == 'exit':
        break

    audio = generate(
        text=f"{a}",
        voice="Ryan",
        model='eleven_multilingual_v2'
    )

    if not audio:
        print("语音生成失败，请检查输入文本和语音模型设置。")
        continue 

    play(audio)
    output_filename = "output.mp3"

    with open(output_filename, "wb") as f:
        f.write(audio)
    print(f"语音已保存为 {output_filename}")

