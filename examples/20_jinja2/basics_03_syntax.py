# -*- coding: utf-8 -*-
from pprint import pprint
import sys
import os

from jinja2 import Environment, FileSystemLoader, StrictUndefined
import yaml
from rich import print as rprint
from rich.rule import Rule

# $ python basics_03_syntax.py templates/variables.txt data_files/vars.yml
# $ python basics_03_syntax.py templates/for.txt data_files/for.yml
template_dir, template_file = os.path.split(sys.argv[1])
vars_file = sys.argv[2]


env = Environment(
    loader=FileSystemLoader(template_dir),
    trim_blocks=True,
    lstrip_blocks=True,
    # undefined=StrictUndefined,
)
template = env.get_template(template_file)

with open(vars_file) as f:
    vars_dict = yaml.safe_load(f)

# rprint(vars_dict)
# rprint(Rule())
print()
print(template.render(vars_dict))
