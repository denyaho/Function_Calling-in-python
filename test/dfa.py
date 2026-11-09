## -?(0|[1-9][0-9]*) DFA


class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_state):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_state = accept_state

    def step(self, state, symbol: str):
        if symbol not in self.alphabet:
            return "sink"
        return self.transitions.get(state, {}).get(symbol, "sink")

    def accepts(self, input: str) -> bool:
        state = self.start_state
        for symbol in input:
            print(f"allowed symbols from state {state}: {self.allowed_symbols(state)}")
            state = self.step(state, symbol)
            if state == "sink":
                return False
            print(f"can end at state {state}: {self.can_end(state)}")
        return state in self.accept_state

    def allowed_symbols(self, state):
        return sorted(set(self.transitions.get(state, {}).keys()))
    
    def can_end(self, state):
        return state in self.accept_state

    def advance(self, state, input: str):
        for symbol in input:
            state = self.step(state, symbol)
            if state == "sink":
                break
        return state

if __name__ == "__main__":
    dfa = DFA(
        states={"q0","q1", "q2", "q3", "sink"},
        alphabet= {"-", "0", "1", "2","3", "4", "5", "6", "7", "8", "9"},
        transitions={
            "q0": {"-": "q1", "0": "q3", "1": "q2", "2": "q2", "3": "q2", "4": "q2", "5": "q2", "6": "q2", "7": "q2", "8": "q2", "9": "q2"},
            "q1": {"0": "q3", "1": "q2", "2": "q2", "3": "q2", "4": "q2", "5": "q2", "6": "q2", "7": "q2", "8": "q2", "9": "q2"},
            "q2": {"0": "q2", "1": "q2", "2": "q2", "3": "q2", "4": "q2", "5": "q2", "6": "q2", "7": "q2", "8": "q2", "9": "q2"},
        },
        start_state="q0",
        accept_state={"q2","q3"},
    )
    print(dfa.accepts("-123"))
    print(dfa.accepts("0"))
    print(dfa.accepts("456"))
    print(dfa.accepts("-0"))
    print(dfa.accepts("01"))
    print(dfa.accepts("-456"))
    print(dfa.accepts("00"))
    print(dfa.accepts("-"))
    print("--- advance ---")
    print(dfa.advance("q0", "-123"))
    print(dfa.advance("q0", "0"))
    print(dfa.advance("q0", "456"))
    print(dfa.advance("q0", "-0"))
    print(dfa.advance("q0", "01"))
    print(dfa.advance("q2", "-456"))
    print(dfa.advance("q3", "00"))
    print(dfa.advance("q0", "-"))
