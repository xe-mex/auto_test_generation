from random import normalvariate, triangular, randrange, choice
from src.configurator import config, get_config_for_cell
from math import pi


def gen_value_scale(cell_name):
    rule = get_rule_for_operation(cell_name, gen_value_scale)
    if rule.get("type") == "random":
        return _gen_norm_random(), _gen_norm_random()
    elif rule.get("type") == "fix":
        return float(rule["values"][0]), float(rule["values"][1])
    elif rule.get("type") == "range":
        return _gen_range(int(rule["values"][0]), int(rule["values"][1]))
    elif rule.get("type") == "choice":
        return _gen_choice(rule.get("values")), _gen_choice(rule.get("values"))
    else:
        raise Exception(f"{rule.get('type')} not supported")
    # return randrange(1, 2)


def gen_value_translate(cell_name, *, modify=1, step=0):
    move = gen_value_scale(cell_name)
    return (modify * move[0]) + step, (modify * move[1]) + step


def gen_rotate_angular(cell_name):
    return triangular(0, pi, float(config["mu"]))


def get_rule_for_operation(cell_name, operation):
    rules = get_config_for_cell(cell_name)
    if not rules:
        return "random"
    if operation == gen_value_scale:
        rule = rules["scale"]
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


def _gen_norm_random():
    return normalvariate(float(config["mu"]), float(config["sigma"]))


def _gen_range(start, end):
    return randrange(start, end+1), randrange(start, end+1)


def _gen_choice(seq):
    return choice(seq)
