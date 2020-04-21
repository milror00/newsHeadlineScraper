import logging

from behave import given, when, then

from features.configuration.configuration import Configuration
from features.pages.FoxNewsPage import FoxNewsPage

@given(u'I am I have a list of newspaper urls')
def step_impl(context):
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    context.headlines = []
    context.newspapers = context._stack[0]['table']
    #newspaper= context._stack[0]['table'][0][0]


@given(u'I capture the top headline for each newspaper')
def step_impl(context):
    for newspaper in context.newspapers:
        context.currentURL = newspaper[0]
        newspaper=newspaper[1]
        page = FoxNewsPage()
        page.getHeadline(context)

@then(u'for each headline I can write it out to stdout')
def step_impl(context):
   print(context.headlines[0]['headline'])
   print(context.headlines[0]['image'])
   print(context.headlines[0]['hash'].hexdigest())

