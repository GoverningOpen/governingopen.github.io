import markdown
from os import listdir, makedirs
from os.path import isfile, join
from jinja2 import Environment, FileSystemLoader

from config import serverpath


env = Environment(loader=FileSystemLoader('theme/templates'))


def is_metadata(line: str) -> dict:
    """Short helper function which takes a line and tests if it is metadata, with a colon dividing a key-value pair. Also
    checks that the key is one of the valid metadata tags, that it is lower-cased for use in the templates, and it strips 
    newlines from the values."""
    VALID_METADATA_TAGS = ["title", "authors", "contributors", "challenge", "challenges", "summary"]
    tokens = line.split(":")
    if len(tokens) == 2 and tokens[0].lower() in VALID_METADATA_TAGS:
        return {tokens[0].lower(): tokens[1].strip("\n").strip(" ")}


def generate_filename_and_url(path_to_file):
    """Small helper function to take a relative path and generate a filename with a .html instead of .md type, as well
    as a url with the correct server path and relative path."""

    tokens = path_to_file.split("/")
    relative_path = "/".join(tokens[1:-1]) + "/"   # note that we drop the first token, the internal "content" folder
    filename = tokens[-1].split(".")[0] + ".html"

    return filename, serverpath + relative_path + filename


def process_markdown_file(path_to_file: str) -> dict:
    """Takes a file path and loads the file. Creates dictionary with the following key-value pairs:

    filename : the name of the markdown file, with path and .md extension removed
    url : the full path to the url, taking into account whether we're in dev mode or live
    content : the non-metadata content of the file, converted from markdown to html
    all valid metadata key-value pairs
    """

    filename, url = generate_filename_and_url(path_to_file)

    data = {"filename": filename, "url": url}
    metadata_finished = False
    content = ""

    with open(path_to_file, mode="r") as markdown_file:

        for line in markdown_file:

            if metadata_finished:
                content += line
                continue

            if metadata_pair := is_metadata(line): 
                data.update(metadata_pair)
            else:
                metadata_finished = True

    data["content"] = markdown.markdown(content, extensions=["toc"])
    return data


def get_files_in_directory(directory: str) -> list:
    """Given a directory path, gets all files (and only files) at that path and return as list."""
    files = []
    for file_name in listdir(directory):
        challenge_file = join(directory, file_name)
        if isfile(challenge_file):
            files.append(challenge_file)
    return files


def get_data_from_markdown_files(file_category: str) -> dict:
    """Given a file_category load all markdown files of that category and create a dictionary."""
    data = []
    for file_name in get_files_in_directory(f"content/{file_category}"):
        file_data = process_markdown_file(file_name)
        data.append(file_data)
    return data


def get_resources_given_challenge(data, challenge_file=""):
    resources = []
    for resource in data["resources"]:
        if challenge_file[:-5] in resource.get('challenge', []):  # note - :-5 strips ".html" from file name
            resources.append(resource)
    return resources


def render_files(file_category: str, data:dict):

    # create directory
    directory_path = f"./output/{file_category}s/" 
    makedirs(directory_path, exist_ok=True)

    # render list page
    template = env.get_template(f"{file_category}_list.html")
    with open(directory_path + "index.html", "w") as newFile:  
        newFile.write(template.render(**data))

    # render detail pages
    template = env.get_template(f"{file_category}.html")
    for file_data in data[f"{file_category}s"]:
        if file_category == "challenge":
            data["challenge_resources"] = get_resources_given_challenge(data, file_data["filename"])
        with open(directory_path + file_data["filename"], "w") as newFile:  
            newFile.write(template.render(**data, **file_data))
