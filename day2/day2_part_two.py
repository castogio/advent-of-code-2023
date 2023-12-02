from dataclasses import dataclass, field

@dataclass
class Result:
    red: int = 0
    green: int = 0
    blue: int = 0


class Load(Result):
    
    def get_power(self) -> int:
        return self.red * self.blue * self.green


@dataclass
class Game:
    id: int
    results: list[Result] = field(default_factory=list)

    def is_possible(self, color_load: Load):
        for res in self.results:
            if res.red > color_load.red or res.blue > color_load.blue or res.green > color_load.green:
                return False
        return True
    
    def get_minimum_set(self) -> Load:
        max_red = max((res.red for res in self.results))
        max_blue = max((res.blue for res in self.results))
        max_green = max((res.green for res in self.results))
        return Load(red=max_red, blue=max_blue, green=max_green)


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
    minimum_sets_powers = (g.get_minimum_set().get_power() for g in games)
    
    print(f'total = {sum(minimum_sets_powers)}')
    