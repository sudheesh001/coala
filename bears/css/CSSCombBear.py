import re

from coalib.bearlib.abstractions.Lint import Lint
from coalib.bears.LocalBear import LocalBear

class CSSCombBear(LocalBear, Lint):
	executable = 'csscomb'
	diff_message = 'css comb can be applied.'
	use_stdout = True

	def run(self, filename, file):
		"""
		Corrects and formats CSS files correctly
		"""
		return self.lint(filename, file)