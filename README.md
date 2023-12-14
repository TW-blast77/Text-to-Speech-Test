
# Text-to-Speech-Test
## 安装

首先，您需要安裝 Eleven Labs Python SDK。您可以使用 pip 進行安裝：
參考網站 : https://github.com/elevenlabs/elevenlabs-python (elevenlabs-python)

```bash
pip install elevenlabs
```
在使用 Eleven Labs 之前，您需要設定一個有效的 API 金鑰。請按照以下步驟在您的程式中設定 API 金鑰：

開啟 setting-api-key.py 檔案。

使用以下程式碼匯入 set_api_key 函數並設定您的 API 金鑰。將 <YOUR_API_KEY> 替換為您的實際 API 金鑰：
```py
from elevenlabs import set_api_key
set_api_key("<YOUR_API_KEY>")
```
## 使用示例
1. 獲取可用語音列表
您可以使用 Show_voices_Lib.py 來列出可用的語音選項：
```py
from elevenlabs import show_voices, set_api_key
set_api_key("<YOUR_API_KEY>")
show_voices()
```
2. 文本轉語音
您可以使用 Text-to-Speech.py 示範程式碼來將文字轉化為語音。將 <YOUR_API_KEY> 替換為您的實際 API 金鑰：
```py
from elevenlabs import generate, play, set_api_key

set_api_key("<YOUR_API_KEY>")
audio = generate(
    text="你好!",
    voice="Bella",
    model='eleven_monolingual_v1'
)

play(audio)

```
# 作者
本實驗參考 : https://github.com/elevenlabs/elevenlabs-python (elevenlabs-python)
技術歸elevenlabs所有

如果您有任何問題或需要幫助，請聯絡 [TW-blast77](apple123499220@gmail.com)