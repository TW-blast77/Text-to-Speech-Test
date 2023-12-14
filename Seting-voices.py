from elevenlabs import Voice, VoiceSettings, generate, stream ,set_api_key
from elevenlabs import generate, play, set_api_key
from pydub import AudioSegment
audio = generate(
    text="幹你老師.",
    voice=Voice(
        voice_id='21m00Tcm4TlvDq8ikWAM',
        settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)#穩定度,相似度,風格
    )
)

play(audio) 