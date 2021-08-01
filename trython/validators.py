import json
import xmltodict
import feedparser


def requests_json_validator(result):
    return json.loads(result.text)


def requests_xml_validator(result):
    return xmltodict.parse(result.text)


def requests_rss_validator(result):
    return feedparser.parse(result.text)
