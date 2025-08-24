from dynaconf import Dynaconf, Validator

settings = Dynaconf(
    envvar_prefix="BOT",
    load_dotenv=True,
    environments=False,
    settings_files=[".env"]
)

settings.validators.register(
    Validator("API_BASE", must_exist=True, ne=""),
    Validator("API_KEY", must_exist=True, ne=""),
)

settings.validators.validate()