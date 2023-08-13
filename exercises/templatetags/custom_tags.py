from django import template

register = template.Library()


@register.filter
def replace_diams(value):
    return value.replace('&diams;', '<input type="text" id="answersInput" name="answer_data" >')
