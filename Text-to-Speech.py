from elevenlabs import generate, play,set_api_key
set_api_key("1557cf4f516bc662637f043d97e94d73")
audio = generate(
    text="你好我是你爹!",
    voice="Bella",
    model='eleven_monolingual_v1'
)

play(audio)
