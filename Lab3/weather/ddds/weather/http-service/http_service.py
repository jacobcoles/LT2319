# -*- coding: utf-8 -*-

import json
from os import getenv

from flask import Flask, request
from jinja2 import Environment
from urllib.request import Request, urlopen

import structlog

from logger import configure_stdout_logging

api_key = "a7d03e3d7217f4118ca5c99873b754cf"


def setup_logger():
    logger = structlog.get_logger(__name__)
    try:
        log_level = getenv("LOG_LEVEL", default="INFO")
        configure_stdout_logging(log_level)
        return logger
    except BaseException:
        logger.exception("exception during logger setup")
        raise


logger = setup_logger()
app = Flask(__name__)
environment = Environment()


def jsonfilter(value):
    return json.dumps(value)


environment.filters["json"] = jsonfilter


def error_response(message):
    response_template = environment.from_string("""
    {
      "status": "error",
      "message": {{message|json}},
      "data": {
        "version": "1.0"
      }
    }
    """)
    payload = response_template.render(message=message)
    response = app.response_class(
        response=payload,
        status=200,
        mimetype='application/json'
    )
    logger.info("Sending error response to TDM", response=response)
    return response


def query_response(value, grammar_entry):
    response_template = environment.from_string("""
    {
      "status": "success",
      "data": {
        "version": "1.1",
        "result": [
          {
            "value": {{value|json}},
            "confidence": 1.0,
            "grammar_entry": {{grammar_entry|json}}
          }
        ]
      }
    }
    """)
    payload = response_template.render(value=value, grammar_entry=grammar_entry)
    response = app.response_class(
        response=payload,
        status=200,
        mimetype='application/json'
    )
    logger.info("Sending query response to TDM", response=response)
    return response


def multiple_query_response(results):
    response_template = environment.from_string("""
    {
      "status": "success",
      "data": {
        "version": "1.0",
        "result": [
        {% for result in results %}
          {
            "value": {{result.value|json}},
            "confidence": 1.0,
            "grammar_entry": {{result.grammar_entry|json}}
          }{{"," if not loop.last}}
        {% endfor %}
        ]
      }
    }
     """)
    payload = response_template.render(results=results)
    response = app.response_class(
        response=payload,
        status=200,
        mimetype='application/json'
    )
    logger.info("Sending multiple query response to TDM", response=response)
    return response


def validator_response(is_valid):
    response_template = environment.from_string("""
    {
      "status": "success",
      "data": {
        "version": "1.0",
        "is_valid": {{is_valid|json}}
      }
    }
    """)
    payload = response_template.render(is_valid=is_valid)
    response = app.response_class(
        response=payload,
        status=200,
        mimetype='application/json'
    )
    logger.info("Sending validator response to TDM", response=response)
    return response

def get_data(city,country, unit="metric"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&units={unit}&APPID={api_key}"
    print("\n\n the URL is ", url, "\n\n")
    request = Request(url)
    response = urlopen(request)
    data = response.read()
    return json.loads(data)


@app.route("/dummy_query_response", methods=['POST'])
def dummy_query_response():
    response_template = environment.from_string("""
    {
      "status": "success",
      "data": {
        "version": "1.1",
        "result": [
          {
            "value": "dummy",
            "confidence": 1.0,
            "grammar_entry": null
          }
        ]
      }
    }
     """)
    payload = response_template.render()
    response = app.response_class(
        response=payload,
        status=200,
        mimetype='application/json'
    )
    logger.info("Sending dummy query response to TDM", response=response)
    return response


@app.route("/action_success_response", methods=['POST'])
def action_success_response():
    response_template = environment.from_string("""
   {
     "status": "success",
     "data": {
       "version": "1.1"
     }
   }
   """)
    payload = response_template.render()
    response = app.response_class(
        response=payload,
        status=200,
        mimetype='application/json'
    )
    logger.info("Sending successful action response to TDM", response=response)
    return response


@app.route("/get_temp", methods=['POST'])
def temperature():
    payload = request.get_json()
    city = payload["context"]["facts"]["city_pred"]["grammar_entry"]
    country = payload["context"]["facts"]["country_pred"]["grammar_entry"]
    try: 
      unit = payload["context"]["facts"]["unit_pred"]["grammar_entry"]
      print(unit)
    except:
      unit = "metric"
    data = get_data(city, country, unit)
    temp = data['main']['temp']
    tempstr = str(temp)
    print("temperature response is ", tempstr)
    return query_response(value=tempstr, grammar_entry=None)

@app.route("/get_weather", methods=['POST'])
def weather():
    payload = request.get_json()
    city = payload["context"]["facts"]["city_pred"]["grammar_entry"]
    country = payload["context"]["facts"]["country_pred"]["grammar_entry"]
    data = get_data(city, country)
    weather_desc = data['weather'][0]['description']
    weather_desc_str = str(weather_desc)
    print("weather response is ", weather_desc_str)
    return query_response(value=weather_desc_str, grammar_entry=None)
