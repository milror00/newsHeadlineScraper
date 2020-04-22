import logging

from behave import given, when, then

from features.configuration.configuration import Configuration
from features.helpers.FoxNewsAdapter import FoxNewsAdapter
from features.helpers.NewspaperAdapter import NewspaperAdapter
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
        paper = newspaper[1]
        if newspaper[1] == 'FOXNEWS':
            page = FoxNewsPage()
            page.getHeadline(context)

@then(u'for each headline I can write it out to stdout')
def step_impl(context):
    for newspaper in context.newspapers:
        paper = newspaper[1]
        if paper == 'FOXNEWS':
            page = FoxNewsPage()
            page.asText(context)

@then(u'for each headline I can write it out to my database headlines')
def step_impl(context):
    for newspaper in context.newspapers:
        paper = newspaper[1]
        if paper == 'FOXNEWS':
            fox = FoxNewsAdapter()
            fox.insertNewsheadline(context)

@then(u'for each paper print out the latest headline from database headlines')
def step_impl(context):
    news = NewspaperAdapter()
    newspapers = news.getAllDistinctNewspapers(context)
    loop = 0
    for newspaper in newspapers:
        if newspaper[loop] == 'FOXNEWS':
            fox = FoxNewsAdapter()
            headline = fox.getLatestHeadline(context, newspaper[loop])
            print("Latest " + newspaper[loop] + " headline in DB: \n" + headline[0][0])
        loop = loop + 1



