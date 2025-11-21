import ast
import re
import sys
from spellchecker import SpellChecker

SPELL = SpellChecker(language='en')

def split_words(name):
    parts = name.split('_')
    final_words = []
    for part in parts:
        camel_parts = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?![a-z])', part)
        final_words.extend(camel_parts)
    return [word.lower() for word in final_words]

with open("Wallet.py", "r") as f:
    tree = ast.parse(f.read())

def get_class_attributes(class_name, tree):
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            attributes = []
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name == "__init__":
                    for stmt in item.body:
                        if isinstance(stmt, ast.Assign):
                            for target in stmt.targets:
                                if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == "self":
                                    attributes.append(target.attr)
            return attributes
    return []

attributes = get_class_attributes("Wallet", tree)

misspelled = []
for attr in attributes:
    words = split_words(attr)
    unknown = SPELL.unknown(words)
    if unknown:
        misspelled.append((attr, list(unknown)))

if misspelled:
    for attr, unknown_words in misspelled:
        print(f"attribute {attr} is not and english word")
    sys.exit(1)
