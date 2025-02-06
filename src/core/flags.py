from argparse import ArgumentParser
from typing import Optional

class FlagManager:
    def __init__(self):
        self.parser = ArgumentParser()
        self._setup_flags()
    
    def _setup_flags(self):
        self.parser.add_argument('--debug', type=bool, default=False)
        self.parser.add_argument('--verbose', type=bool, default=False)
    
    def parse(self):
        return self.parser.parse_args()