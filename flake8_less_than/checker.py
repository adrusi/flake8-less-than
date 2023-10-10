import ast

class LessThanChecker:
    name = 'flake8-less-than'
    version = '0.1'
    _gt_error_code = 'LT001'
    _gte_error_code = 'LT002'
    _gt_error_message = "LT001: Use '<' instead of '>'."
    _gte_error_message = "LT002: Use '<=' instead of '>='."

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Compare):
                yield from self.handle_comparison(node)

    def handle_comparison(self, node):
        for idx, operator in enumerate(node.ops):
            if isinstance(operator, ast.Gt):
                yield (
                    node.lineno,
                    node.col_offset, #+ sum(len(c.s) + 1 for c in node.comparators[:idx]) if idx > 0 else node.col_offset,
                    self._gt_error_message,
                    type(self)
                )
            elif isinstance(operator, ast.GtE):
                yield (
                    node.lineno,
                    node.col_offset, #+ sum(len(c.s) + 1 for c in node.comparators[:idx]) if idx > 0 else node.col_offset,
                    self._gte_error_message,
                    type(self)
                )

