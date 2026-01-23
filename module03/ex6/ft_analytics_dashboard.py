"""Examples of comprehension usage for simple game analytics demonstrations."""
from typing import Any, Dict, List, Set


def dict_comp(data: Dict[str, Any]) -> None:
    """Build dictionaries summarizing player scores and achievements.

    Args:
        data (Dict[str, Any]): the game data dictionary
    """

    print("\n=== Dict Comprehension Examples ===")
    player_score: Dict[str, int] = {
        player: data["players"][player]["total_score"]
        for player in data["players"]}
    scores: Dict[str, int] = {"high": len(list(session
                                               for session
                                               in data["sessions"]
                                               if session["score"] >= 2500))}
    scores.update({"medium": len(list(session
                                      for session in data["sessions"]
                   if session["score"] >= 1500 and session["score"] < 2500))})
    scores.update({"low": len(list(session
                   for session in data["sessions"]
                   if session["score"] < 1500))})
    achievements: Dict[str, int] = {
        player: data["players"][player]["achievements_count"]
        for player in data["players"]}
    print(f"Player scores: {player_score}")
    print(f"Scores categories: {scores}")
    print(f"Achievement counts: {achievements}")


def list_comp(data: Dict[str, Any]) -> None:
    """Show list comprehension examples for sessions and players.

    Args:
        data (Dict[str, Any]): the game data dictionary
    """

    print("\n=== List Comprehension Examples ===")
    high: List[str] = [player for player in data["players"]
                       if data["players"][player]["total_score"] > 2000]
    bob_sessions_time: List[int] = [session["duration_minutes"]
                                    for session in data["sessions"]
                                    if session["player"] == "bob"]
    comp_games: List[str] = [session["player"] for session in data["sessions"]
                             if session["mode"] == "competitive"]
    print(f"High scorers (>2000): {high}")
    print(f"Bob' sessions time: {bob_sessions_time}")
    print(f"Bob's max session {max(bob_sessions_time)} minutes" +
          f" -> average {sum(bob_sessions_time)/len(bob_sessions_time)}" +
          " minutes")
    print(f"All competitive games: {comp_games}")


def set_comp(data: Dict[str, Any]) -> None:
    """Show set comprehension examples for unique values.

    Args:
        data (Dict[str, Any]): the game data dictionary
    """

    print("\n=== Set Comprehension Examples ===")
    unique_play: Set[str] = {player for player in data["players"]}
    unique_achievement: Set[str] = {
        achievement for achievement in data["achievements"]}
    unique_session_score: Set[int] = {
        session["score"] for session in data["sessions"]}
    print(f"Unique players: {unique_play}")
    print(f"Unique achievements: {unique_achievement}")
    print(f"Unique session score: {unique_session_score}")


def combine(data: Dict[str, Any]) -> None:
    """Combine different summary metrics into a final analysis.

    Args:
        data (Dict[str, Any]): the game data dictionary
    """

    print("\n=== Combined Analysis ===")
    total: int = len({player for player in data["players"]})
    unique: int = len({achievement for achievement in data["achievements"]})
    scores: List[int] = [score["score"] for score in data["sessions"]]
    average: float = sum(scores)/len(scores)
    scores_player: List[int] = [data["players"][player]["total_score"]
                                for player in data["players"]]
    top: Dict[str, Dict[str, Any]] = {
        player: data["players"][player]
        for player in data["players"]
        if data["players"][player]["total_score"] == max(scores_player)}
    print(f"Total players: {total}")
    print(f"Total unique achievement: {unique}")
    print(f"Average score by session: {'%.2f' % average}")
    for p in top:
        print(f"Top performer: {p} ({top[p]['total_score']} points, " +
              f"{top[p]['achievements_count']} achievements)")


def main() -> None:
    """Execute program"""
    data: Dict[str, Any] = {
        "players": {
            "alice": {
                "level": 41,
                "total_score": 2824,
                "sessions_played": 13,
                "favorite_mode": "ranked",
                "achievements_count": 5,
            },
            "bob": {
                "level": 16,
                "total_score": 4657,
                "sessions_played": 27,
                "favorite_mode": "ranked",
                "achievements_count": 2,
            },
            "charlie": {
                "level": 44,
                "total_score": 9935,
                "sessions_played": 21,
                "favorite_mode": "ranked",
                "achievements_count": 7,
            },
            "diana": {
                "level": 3,
                "total_score": 1488,
                "sessions_played": 21,
                "favorite_mode": "casual",
                "achievements_count": 4,
            },
            "eve": {
                "level": 33,
                "total_score": 1434,
                "sessions_played": 81,
                "favorite_mode": "casual",
                "achievements_count": 7,
            },
            "frank": {
                "level": 15,
                "total_score": 8359,
                "sessions_played": 85,
                "favorite_mode": "competitive",
                "achievements_count": 1,
            },
        },
        "sessions": [
            {
                "player": "bob",
                "duration_minutes": 94,
                "score": 1831,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "bob",
                "duration_minutes": 32,
                "score": 1478,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 17,
                "score": 666,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 98,
                "score": 666,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 15,
                "score": 2361,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "eve",
                "duration_minutes": 29,
                "score": 2985,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 34,
                "score": 1285,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "alice",
                "duration_minutes": 53,
                "score": 1238,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "bob",
                "duration_minutes": 52,
                "score": 1555,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "frank",
                "duration_minutes": 92,
                "score": 2754,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 98,
                "score": 1102,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "diana",
                "duration_minutes": 39,
                "score": 2721,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 46,
                "score": 329,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 56,
                "score": 1196,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 117,
                "score": 1388,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "diana",
                "duration_minutes": 118,
                "score": 2733,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 22,
                "score": 1110,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "frank",
                "duration_minutes": 79,
                "score": 1854,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "charlie",
                "duration_minutes": 33,
                "score": 666,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 101,
                "score": 292,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 25,
                "score": 2887,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 53,
                "score": 2540,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "eve",
                "duration_minutes": 115,
                "score": 147,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 118,
                "score": 2299,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 42,
                "score": 1880,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 97,
                "score": 1178,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 18,
                "score": 2661,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "bob",
                "duration_minutes": 52,
                "score": 761,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 46,
                "score": 2101,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 117,
                "score": 1359,
                "mode": "casual",
                "completed": True,
            },
        ],
        "game_modes": ["casual", "competitive", "ranked"],
        "achievements": [
            "first_blood",
            "level_master",
            "speed_runner",
            "treasure_seeker",
            "boss_hunter",
            "pixel_perfect",
            "combo_king",
            "explorer",
            "combo_king",
            "speed_runner"
        ],
    }

    print("=== Game Analytics Dashboard ===")
    list_comp(data)
    dict_comp(data)
    set_comp(data)
    combine(data)


if __name__ == "__main__":
    main()
