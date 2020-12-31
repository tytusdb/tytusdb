class grammar_result:

    def __init__(self, grammarerrors, grammarreport: str, noderoot):
        self.grammarerrors = grammarerrors
        self.grammarreport: str = grammarreport
        self.noderoot = noderoot