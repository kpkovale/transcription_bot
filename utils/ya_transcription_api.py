from speechkit import model_repository, configure_credentials, creds
from speechkit.stt import AudioProcessingType
from utils.token_generator import IAMToken
from utils.bot_logger import logger
from typing import Union, BinaryIO
from pathlib import Path


class VoiceMsgRecognizer():

    def __init__(self):
        logger.info("Initiating voice recognizer object")
        token = IAMToken()
        # Аутентификация через AIM Токен
        configure_credentials(
            yandex_credentials=creds.YandexCredentials(
                iam_token=token.iam_token)
            )
        self.__init_recognition_model()

    def __init_recognition_model(self):
        logger.debug("Initiating voice recognition model")
        self.model = model_repository.recognition_model()

        # Set model parameters
        self.model.model = 'general'
        self.model.language = 'ru-RU'
        self.model.audio_processing_type = AudioProcessingType.Full

    def recognize(self, audio: Union[Union[str, Path], BinaryIO, bytes]):
        logger.info("Starting voice recognition")

        # Распознавание речи в указанном аудиофайле и вывод результатов в консоль.
        if isinstance(audio, str):
            result = self.model.transcribe_file(audio)
        elif isinstance(audio, (BinaryIO, bytes)):
            result = self.model.transcribe(audio)
        else:
            print(type(audio))
            return "Некорректный формат аудиофайла..."

        if result:
            logger.info("Voice recognition successul. Sending results.")
            return result[0].normalized_text
        else:
            return "Не удалось распознать аудиосообщение..."


if __name__ == '__main__':
    recognizer = VoiceMsgRecognizer()
    with open('/home/kirill/tmp/short_msg.ogg', 'rb') as af:
        res1 = recognizer.recognize(af.read())
        print(res1)
    # res2 = recognizer.recognize('/home/kirill/tmp/long_msg.ogg')
    # print(res2)
