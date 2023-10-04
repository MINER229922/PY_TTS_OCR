import time
import asyncio
from winsdk.windows.media.speechsynthesis import SpeechSynthesizer, SpeechAppendedSilence, SpeechPunctuationSilence, VoiceGender, SpeechSynthesisStream, SpeechSynthesizerOptions, VoiceInformation
from winsdk.windows.storage.streams import DataReader # TODO
import typing
import pprint


def PrintVoiceInfo(voice):
    print("id\t-\t", voice.id)
    print("display_name:\t", voice.display_name, "gender:\t", voice.gender)
    print("language\t-\t", voice.language)
    print("description\t-\t", voice.description)


# print("====================", "all_voices", "====================")
# result = SpeechSynthesizer.all_voices
# for i in range(0, result.size):
#     PrintVoiceInfo(result[i])

print("====================", "default_voice", "====================")
voice_default = SpeechSynthesizer.default_voice
PrintVoiceInfo(voice_default)
#! not work
# # print("====================", "my_voice", "====================")
# voice_my = typing.ClassVar[SpeechSynthesizer.voice]
# PrintVoiceInfo(voice_my)


async def ensure_coroutine(awaitable):
    return await awaitable


def blocking_wait(awaitable):
    return asyncio.run(ensure_coroutine(awaitable))


print("Time Start:\t", time.time())
# result = blocking_wait(SpeechSynthesizer.synthesize_text_to_stream_async("他是白痴"))
speech = SpeechSynthesizer()
result = blocking_wait(speech.synthesize_text_to_stream_async("他是白痴"))
print(result)
print("Time End:\t", time.time())
