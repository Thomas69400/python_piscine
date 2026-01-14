from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    def get_strategy_name(self) -> str:
        """Return the name of Strategy

        Returns:
            str: Aggressive Strategy
        """

        return "Aggressive Strategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if len(available_targets) == 0:
            return []
        else:
            try:
                targets = [
                    target for target
                    in available_targets
                    if target.health < 3
                ]
                if len(targets) == 0:
                    return available_targets
                return targets
            except TypeError as e:
                return e
