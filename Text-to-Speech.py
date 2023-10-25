from elevenlabs import generate, play, set_api_key
from pydub import AudioSegment
import os

# 设置 Eleven Labs API 密钥
set_api_key("1557cf4f516bc662637f043d97e94d73")

# 输入待转换的文本
a = input("輸入文字轉語音: ")

# 生成语音
audio = generate(
    text=f"{a}",
    voice="Ryan",
    model='eleven_multilingual_v2'
)

# 播放语音
play(audio)

# 将 bytes 对象保存为临时 WAV 文件
tmp_wav_file = "temp.wav"
with open(tmp_wav_file, "wb") as f:
    f.write(audio)

# 使用 pydub 加载 WAV 文件
audio_segment = AudioSegment.from_file(tmp_wav_file, format="wav")

# 保存为 MP3 文件
output_filename = "output.mp3"
audio_segment.export(output_filename, format="mp3")

# 删除临时 WAV 文件
os.remove(tmp_wav_file)

print(f"语音已保存为 {output_filename}")
