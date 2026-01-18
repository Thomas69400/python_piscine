"""Demo entry point for the Tournament Platform.

This script registers a couple of TournamentCard instances, runs a match,
displays a leaderboard and prints a platform report.
"""

from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main() -> None:
    """Create and run a short tournament demonstration."""
    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")

    tournament = TournamentPlatform()
    creature1 = TournamentCard(
        "Fire Dragon", 5, "Epic", 8, 5, 8, "dragon_001", 1200)
    creature2 = TournamentCard(
        "Ice Wizard", 4, "Rare", 6, 3, 5, "wizard_001", 1150)

    stat_creature1 = creature1.get_tournament_stats()
    print(stat_creature1["name"] + f" (ID {stat_creature1['id']}):")
    print(f"- Interfaces: {stat_creature1['interfaces']}")
    print(f"- Rating: {stat_creature1['rating']}")
    print(f"- Record: {stat_creature1['wins']}-{stat_creature1['losses']}\n")

    stat_creature2 = creature2.get_tournament_stats()
    print(stat_creature2["name"] + f" (ID {stat_creature2['id']}):")
    print(f"- Interfaces: {stat_creature2['interfaces']}")
    print(f"- Rating: {stat_creature2['rating']}")
    print(f"- Record: {stat_creature2['wins']}-{stat_creature2['losses']}\n")

    tournament.register_card(creature1)
    tournament.register_card(creature2)

    print("Creating tournament match...")
    match_results = tournament.create_match(creature1.id, creature2.id)
    print(f"Match Results: {match_results}")

    print("\nTournament Leaderboard:")
    leaderboard = tournament.get_leaderboard()
    for card in leaderboard:
        print(f"{card['rank']}. {card['name']} - "
              f"Rating: {card['rating']} "
              f"({card['wins']}-{card['losses']})")

    print("\nPlatform Report:")
    print(tournament.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ==")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
