import os

local_development = os.environ.get("LOCAL_DEVELOPMENT", False)


if local_development:
    serverpath = "http://0.0.0.0:8000/"  # the path the site is served on
else:
    serverpath = "https://governingopen.com/"
