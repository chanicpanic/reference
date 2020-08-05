
from docutils import nodes
from docutils.parsers.rst import Directive, directives

def classification(argument):
    return directives.choice(argument, ("P", "A"))

class AbilityDescription(Directive):

    required_arguments = 0
    optional_arguments = 0
    option_spec = {"name": directives.unchanged,
                   "classification": directives.unchanged,
                   "effect": directives.unchanged,
                   "rulings": directives.unchanged}
    has_content = False
    
    def run(self):
        name = nodes.strong(text=self.options["name"])
        c = " (" + self.options["classification"] + "): "
        classification = nodes.strong(text=c)
        effect = nodes.emphasis(text=self.options["effect"])
        rulings = nodes.paragraph(text=self.options["rulings"])
        return [name, classification, effect, rulings]

def setup(app):
    app.add_directive("ability", AbilityDescription)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True
    }
