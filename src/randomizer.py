from random import normalvariate, triangular, randrange, choice
from src.configurator import config, get_config_for_cell
from math import pi


def gen_value_scale(cell_name):
    rule = get_rule_for_operation(cell_name, gen_value_scale)
    return _calculate_coordinate("x", rule), _calculate_coordinate("y", rule)


def gen_value_translate(cell_name, *, modify=1, step=0):
    move = gen_value_scale(cell_name)
    return 0, 0
    return (modify * move[0]) + step, (modify * move[1]) + step


def gen_rotate_angular(cell_name):
    return triangular(0, pi, float(config["mu"]))


def _calculate_coordinate(coordinate, rule):
    coordinate_rule = get_rule_for_coordinate(coordinate, rule)
    type_rule = (isinstance(coordinate_rule, dict) and coordinate_rule.get("type")) or coordinate_rule or "random"
    if type_rule == "random":
        return _gen_norm_random()
    elif type_rule == "fix":
        return float(coordinate_rule["values"])
    elif type_rule == "range":
        return _gen_range(int(coordinate_rule["values"][0]), int(coordinate_rule["values"][1]))
    elif type_rule == "choice":
        return _gen_choice(coordinate_rule.get("values"))
    else:
        raise Exception(f"{type_rule} not supported")


def get_rule_for_operation(cell_name, operation):
    rules = get_config_for_cell(cell_name)
    if not rules:
        return rules
    if operation == gen_value_scale:
        rule = rules.get("scale")
        if isinstance(rule, str):
            return {"type": rule}
        elif isinstance(rule, object):
            return rule
    elif operation == "rotate":
        pass
    elif operation == "translate":
        pass
    else:
        raise Exception("Operation not provided")


def get_rule_for_coordinate(coordinate, rule):
    return (isinstance(rule, dict) and (rule.get("both") or rule.get(coordinate))) or "random"


def _gen_norm_random():
    return normalvariate(float(config["mu"]), float(config["sigma"]))


def _gen_range(start, end):
    return randrange(start, end+1)


def _gen_choice(seq):
    return choice(seq)
