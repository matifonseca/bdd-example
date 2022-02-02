from behave import fixture, use_fixture
import os


# Hooks para hacer Rollbacks y setear variable de entorno de test
def before_all(context):
    os.environ["TEST_MODE"] = "1"


def before_feature(context, feature):
    context.vars = {}  # Rollback de variables entre feature (vars permite compartir variables entre steps)


def after_scenario(context, scenario):
    pass


def after_all(context):
    del os.environ["TEST_MODE"]
