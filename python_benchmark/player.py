from skeleton.actions import FoldAction, CallAction, CheckAction, RaiseAction
from skeleton.states import GameState, TerminalState, RoundState
from skeleton.states import NUM_ROUNDS, STARTING_STACK, BIG_BLIND, SMALL_BLIND
from skeleton.bot import Bot
from skeleton.runner import parse_args, run_bot

class Player(Bot):

    def __init__(self):
        self.rank_mapping = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

    def handle_new_round(self, game_state, round_state, active):

        pass

    def handle_round_over(self, game_state, terminal_state, active):

        pass

    def get_action(self, game_state, round_state, active):
        
        legal_actions = round_state.legal_actions()
        street = round_state.street
        my_cards = round_state.hands[active]
        if street == 0:
            v1 = self.rank_mapping[my_cards[0][0]]
            v2 = self.rank_mapping[my_cards[1][0]]
            if (v1 + v2) >= 17 and RaiseAction in legal_actions:
                min_raise, max_raise = round_state.raise_bounds()
                return RaiseAction(min_raise)
        else:
            board = round_state.deck[:street]
            for card in board:
                if card[0] == my_cards[0][0] or card[0] == my_cards[1][0]:
                    if RaiseAction in legal_actions:
                        min_raise, max_raise = round_state.raise_bounds()
                        return RaiseAction(min_raise)
                    break
        if CheckAction in legal_actions:
            return CheckAction()
        return CallAction()

if __name__ == '__main__':
    run_bot(Player(), parse_args())
