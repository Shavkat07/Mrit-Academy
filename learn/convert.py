from nbconvert import HTMLExporter
from django.core.exceptions import ValidationError


def turn_into_html(file, name):
    html_exporter = HTMLExporter()
    body, resources = html_exporter.from_file(file)
    html_template_path = f'templates/{name}.html'
    with open(html_template_path, 'w') as f:
        f.write(body)

    return True


def is_ipynb(file):
    file_str = str(file)
    if file_str.lower().endswith('.ipynb'):
        return file
    else:
        raise ValidationError('Only upload .ipynb files, please.')
