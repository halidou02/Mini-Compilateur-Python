import AST
from functools import reduce
import re


class Interpreter:
    def __init__(self):
        self.symbol_table = {}

    def interpret(self, node):
        if isinstance(node, AST.ProgramNode):
            for function in node.functions:
                self.interpret(function)
        elif isinstance(node, AST.FunctionsNode):
            self.symbol_table[node.name.value] = node
            self.interpret(node.body)
        elif isinstance(node, AST.ValueNode):
            return node.value
        elif isinstance(node, AST.AssignNode):
            self.symbol_table[node.identifier] = self.interpret(node.expression)
        elif isinstance(node, AST.SiNode):
            condition = self.interpret(node.condition)
            if condition:
                self.interpret(node.if_body)
            else:
                self.interpret(node.else_body)
        elif isinstance(node, AST.WhileNode):
            while self.interpret(node.condition):
                self.interpret(node.body)
        elif isinstance(node, AST.ReadNode):
            value = input("Enter a value for variable {}: ".format(node.identifier))
            self.symbol_table[node.identifier] = int(value)
        elif isinstance(node, AST.PrintNode):
            value = self.interpret(node.expression)
            print(value)
        elif isinstance(node, AST.OperationNode):
            left = self.interpret(node.left)
            right = self.interpret(node.right)
            if node.operator == '+':
                return left + right
            elif node.operator == '-':
                return left - right
            elif node.operator == '*':
                return left * right
            elif node.operator == '/':
                return left / right
            elif node.operator == '&':
                return left and right
            elif node.operator == '|':
                return left or right
            elif node.operator == '<':
                return left < right
            elif node.operator == '>':
                return left > right
            elif node.operator == '==':
                return left == right
            elif node.operator == '!=':
                return left != right
        elif isinstance(node, AST.ReturnNode):
            return self.interpret(node.expression)
        elif isinstance(node, AST.BodyNode):
            for expression in node.expressions:
                self.interpret(expression)
        elif isinstance(node, AST.FunctionCallNode):
            function_name = node.identifier
            function = self.symbol_table.get(function_name)
            if function:
                self.interpret(function)
            else:
                print("Error: Function '{}' is not defined.".format(function_name))