import os
import logging
class Config:
    API_ID = int(os.environ.get("API_ID", "27448818"))
    API_HASH = os.environ.get("API_HASH", "ff2beee4d6339b57d22d91acda059234")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6612388626:AAFL2n50i-vV9lFxr6ThC9pv1L0VSfh1HIQ")
    Channel_id = os.environ.get("Channel_id", "@alfredo16_bot")
    Drivebuzz_crypt = os.environ.get("Drivebuzz_crypt", "")
    Drivefire_crypt = os.environ.get("Drivefire_crypt", "")
    Jiodrive_crypt = os.environ.get("Jiodrive_crypt", "")
    Gadrive_crypt = os.environ.get("Gadrive_crypt", "")
    Kolop_crypt = os.environ.get("Kolop_crypt", "")
    Katdrive_crypt = os.environ.get("Katdrive_crypt", "")
    Gtot_crypt = os.environ.get("Gtot_crypt", "")
    Appdrive_email = os.environ.get("Appdrive_email", "")
    Appdrive_password = os.environ.get("Appdrive_password", "")
    Hubdrive_crypt = os.environ.get("Hubdrive_crypt", "")
    Sharerpw_xsrf_token = os.environ.get("Sharerpw_xsrf_token", "")
    Sharerpw_laravel_session = os.environ.get("Sharerpw_laravel_session", "")
