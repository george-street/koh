from src.parser import Parser
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader


def render_template(name, template_dir="templates", **kwargs):
    if name.endswith(".tex"):
        block_start_string = kwargs.get("block_start_string", '\\block{')
        block_end_string = kwargs.get("block_end_string", '}')
        variable_start_string = kwargs.get("variable_start_string", '\\var{')
        variable_end_string = kwargs.get("variable_end_string", '}')
        comment_start_string = kwargs.get("comment_start_string", '\\#{')
        comment_end_string = kwargs.get("comment_end_string", '}')

        env = Environment(block_start_string=block_start_string,
                          block_end_string=block_end_string,
                          variable_start_string=variable_start_string,
                          variable_end_string=variable_end_string,
                          comment_start_string=comment_start_string,
                          comment_end_string=comment_end_string,
                          autoescape=False,
                          loader=FileSystemLoader(template_dir))
    else:
        env = Environment(loader=PackageLoader('template', template_dir),
                          autoescape=select_autoescape(['html', 'xml']))
    return env.get_template(name).render(**kwargs)
