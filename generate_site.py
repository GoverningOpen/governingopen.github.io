import shutil
from os import listdir, makedirs
from jinja2 import Environment, FileSystemLoader
import utils, config


# Create output directory if needed
makedirs("./output", exist_ok=True)

# Copy assets
shutil.copytree("./theme/static", "./output/static", dirs_exist_ok=True)

# Make basic data structure
data = {"base_url": config.serverpath}

# Render one-off pages index
env = Environment(loader=FileSystemLoader('theme/templates'))
for page_name in ["index.html", "get-involved.html", "get-help.html"]:
    with open(f"./output/{page_name}", "w") as newFile:
        template = env.get_template(page_name)
        newFile.write(template.render(**data))

# Gather data
data["challenges"] = utils.get_data_from_markdown_files("challenges")
data["resources"] = utils.get_data_from_markdown_files("resources")

# Render pages
utils.render_files("challenge", data)
utils.render_files("resource", data)
