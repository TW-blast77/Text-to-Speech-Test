from elevenlabs import Voice, VoiceSettings, generate, stream ,set_api_key
audio = generate(
    text="Hello! My name is Bella.",
    voice=Voice(
        voice_id='EXAVITQu4vr4xnSDxMaL',
        settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)#穩定度,相似度,風格
    )
)

stream(audio) 