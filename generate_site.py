import shutil
from jinja2 import Environment, FileSystemLoader
import utils, config


# Copy assets
shutil.copytree("./theme/static", "./output/static", dirs_exist_ok=True)

# Render one-off pages index
env = Environment(loader=FileSystemLoader('theme/templates'))
for page_name in ["index.html", "blog.html", "community.html", "workshops.html"]:
    with open(f"./output/{page_name}", "w") as newFile:
        template = env.get_template(page_name)
        newFile.write(template.render())

# Gather data
data = {"global": {"base_url": config.serverpath}}
data["challenges"] = utils.get_data_from_markdown_files("challenges")
data["resources"] = utils.get_data_from_markdown_files("resources")

# Render pages
utils.render_files("challenge", data)
utils.render_files("resource", data)
