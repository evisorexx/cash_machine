from jinja2 import Environment, FileSystemLoader


def render_receipt(receipt_data: dict):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("receipt.html")
    return template.render(**receipt_data)
