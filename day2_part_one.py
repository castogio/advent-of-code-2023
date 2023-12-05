from dataclasses import dataclass, field

@dataclass
class Result:
    red: int = 0
    green: int = 0
    blue: int = 0


class Load(Result):
    ...


@dataclass
class Game:
    id: int
    results: list[Result] = field(default_factory=list)

    def is_possible(self, color_load: Load):
        for res in self.results:
            if res.red > color_load.red or res.blue > color_load.blue or res.green > color_load.green:
                return False
        return True


def parse_line(line: str) -> Game:
    raw_game_id, results_oneline = line.split(sep=':')
    game = Game(id=int(raw_game_id.strip().split()[1]))
    results_oneline = results_oneline.strip()
    separated_results = results_oneline.split(sep=';')
    for ind_result in separated_results:
        raw_color_results = ind_result.split(sep=',')
        result = Result()
        for color in raw_color_results:
            value, color_id = color.split()
            setattr(result, color_id, int(value))
        game.results.append(result)
    return game


if __name__ == "__main__":

    load = Load(red=12, green=13, blue=14)

    with open('./input.txt') as f:
        lines = f.readlines()

    games = (parse_line(l) for l in lines)
    possible_games_id_total = sum((g.id for g in games if g.is_possible(load)))

    print(f'total = {possible_games_id_total}')

    