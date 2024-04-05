import openai
import os
import subprocess

openai.api_key = os.environ.get("OPENAI_API_KEY")

def transcribe_audio(file):
    file_root, _ = os.path.splitext(file)
    output_file = file_root + ".mp3"
    command = ['ffmpeg', '-i', file, output_file]
    subprocess.run(command, check=True)
    audio_file= open(output_file, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    print(transcript)
    return transcript

def ask_gpt(describemsg, max_tokens=3000):
    # prompt = f"Conversación con un asistente AI:\n{describemsg}"
    prompt12345 = f" 现在假设你是一个市政服务专家,我将给你一段文本,请给出分类,分类请从'经济调节','市场监管','社会管理','公共服务', '生态环境保护'这几项中选择一个最合适的,文本如下:{describemsg},请直接给出某一项的分类,不需要其他的输出, 即:直接回答分类的结果"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt12345,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.2,
    )

    print (response.choices[0].text.strip())
    return response.choices[0].text.strip()
