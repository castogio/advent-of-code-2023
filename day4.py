from dataclasses import dataclass

@dataclass
class Scratchcard:
    id: int
    winning_numbers: set[int]
    card_nums: set[int]

    @property
    def part1_points(self) -> int:
        return 2 ** (self.num_matches-1) if self.num_matches > 0 else 0
    
    @property
    def num_matches(self) -> int:
        return len(self.card_nums.intersection(self.winning_numbers))


    @staticmethod
    def loads(entry: str) -> 'Scratchcard':
        id_part, nums_part = entry.split(sep=':')
        card_id = int(id_part.split()[1].strip())
        numbers_str, winning_str = nums_part.split(sep='|')
        winning_numbers = {int(n) for n in winning_str.strip().split()}
        card_nums = {int(n) for n in numbers_str.strip().split()}
        return Scratchcard(card_id, winning_numbers, card_nums)

def get_win(card: Scratchcard, cards: list[Scratchcard]) -> list[Scratchcard]:
    if not card.num_matches:
        return []
    return cards[card.id:card.id+card.num_matches]

def depth_first_search(bucket: list[Scratchcard], all_cards: list[Scratchcard]) -> list[Scratchcard]:
    new_bucket = []
    for c in bucket:
        new_bucket.extend(get_win(c, all_cards))

    if not len(new_bucket):
        return bucket
    
    return bucket + depth_first_search(new_bucket, all_cards)

if __name__ == "__main__":

    expected_card = Scratchcard(1, {6, 9, 48, 17, 83, 53, 86, 31}, {41, 48, 83, 86, 17})
    assert Scratchcard.loads('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53')

    assert Scratchcard.loads('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53').part1_points == 8
    assert Scratchcard.loads('Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19').part1_points == 2
    assert Scratchcard.loads('Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1').part1_points == 2
    assert Scratchcard.loads('Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83').part1_points == 1
    assert Scratchcard.loads('Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36').part1_points == 0
    assert Scratchcard.loads('Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11').part1_points == 0

    with open('./input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    
    cards = [Scratchcard.loads(l) for l in lines]

    total = sum(c.part1_points for c in cards)
    print(f'part1 total = {total}')


    test_cards = [
        Scratchcard.loads('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'),
        Scratchcard.loads('Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19'),
        Scratchcard.loads('Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1'),
        Scratchcard.loads('Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83'),
        Scratchcard.loads('Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36'),
        Scratchcard.loads('Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'),
    ]

    assert get_win(test_cards[0], test_cards) == test_cards[1:5]
    assert get_win(test_cards[1], test_cards) == test_cards[2:4]
    assert get_win(test_cards[2], test_cards) == test_cards[3:5]
    assert get_win(test_cards[4], test_cards) == []
    assert get_win(test_cards[5], test_cards) == []

    assert len(depth_first_search(test_cards, test_cards)) == 30

    total = len(depth_first_search(cards, cards))
    print(f'part2 total = {total}')
    













