import json
from bot_config import KEYS_FILE
import time
from datetime import datetime
import jwt
from utils.bot_logger import logger
from requests import post
from utils.meta_singleton import MetaSingleton


class IAMToken(metaclass=MetaSingleton):
    encoded_jwt_token = None
    iam_token_value = None

    def __init__(self, *args, **kwargs):
        """  Creates a JWT and IAM token generator instance\n
        :param path to keys_file as first parameter is mandatory
        """
        logger.info("Initiating token generator object")
        try:
            with open(KEYS_FILE) as keys_file:
                data_dict = json.loads(keys_file.read())
        except FileExistsError as fee:
            logger.error(fee)
        if not data_dict:
            logger.error("API Keys file is empty.")
            return
        self.service_account_id = data_dict['service_account_id']
        self.key_id = data_dict['id']
        self.private_key = data_dict['private_key']
        self.key_algorithm = 'PS256'  # data_dict['key_algorithm']
        self.expires_at = time.time()
        super().__init__(*args, **kwargs)

    @property
    def payload(self):
        now = int(time.time())
        payload = {
            'aud': 'https://iam.api.cloud.yandex.net/iam/v1/tokens',
            'iss': self.service_account_id,
            'iat': now,
            'exp': now + 360}
        return payload

    def __get_jwt(self):
        # Формирование JWT.
        self.encoded_jwt_token = jwt.encode(
            self.payload,
            self.private_key,
            algorithm=self.key_algorithm,
            headers={'kid': self.key_id})

    def __refresh_iam_token(self) -> None:
        if self.iam_token_value and self.expires_at > time.time():
            return
        self.__get_jwt()
        logger.info("Refreshing IAM Token")
        try:
            response = post("https://iam.api.cloud.yandex.net/iam/v1/tokens",
                            data=json.dumps({"jwt": self.encoded_jwt_token}),
                            headers={"Content-Type": "application/json"}
                            )
        except ConnectionError as ce:
            logger.error("Refreshing IAM Token attempt failed.")
            logger.error(ce)
            return
        except Exception as e:
            logger.error("Refreshing IAM Token attempt failed.")
            logger.error(e)
            return

        response_dict = json.loads(response.content)
        self.iam_token_value = response_dict["iamToken"]
        self.expires_at = datetime.timestamp(datetime.strptime(response_dict["expiresAt"][:23],
                                                               "%Y-%m-%dT%H:%M:%S.%f"))
        logger.info("AIM Token has been refreshed successfully.")

    @property
    def iam_token(self):
        if self.expires_at < time.time():
            self.__refresh_iam_token()
        return self.iam_token_value


if __name__ == '__main__':
    token = IAMToken()
    token_val = token.iam_token
    print(datetime.fromtimestamp(token.expires_at), token_val)
