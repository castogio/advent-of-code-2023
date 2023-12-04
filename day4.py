import time
from dataclasses import dataclass

@dataclass
class Scratchcard:
    id: int
    winning_numbers: set[int]
    card_nums: set[int]
    _num_matches: int = -1

    @property
    def part1_points(self) -> int:
        return 2 ** (self.num_matches-1) if self.num_matches > 0 else 0
    
    @property
    def num_matches(self) -> int:
        if self._num_matches < 0:
            self._num_matches = len(self.card_nums.intersection(self.winning_numbers))
        return self._num_matches

    def __lt__(self, other):
        return self.id < other.id

    @staticmethod
    def loads(entry: str) -> 'Scratchcard':
        id_part, nums_part = entry.split(sep=':')
        card_id = int(id_part.split()[1].strip())
        numbers_str, winning_str = nums_part.split(sep='|')
        winning_numbers = {int(n) for n in winning_str.strip().split()}
        card_nums = {int(n) for n in numbers_str.strip().split()}
        return Scratchcard(card_id, winning_numbers, card_nums)

previous_wins = {}
def get_win(card: Scratchcard, cards: list[Scratchcard]) -> list[Scratchcard]:
    if card.id in previous_wins:
        return previous_wins[card.id]
    list_win = []
    if card.num_matches:
        list_win = cards[card.id:card.id+card.num_matches]
    previous_wins[card.id] = list_win
    return list_win

def recursive_card_list_creation(bucket: list[Scratchcard], all_cards: list[Scratchcard]) -> list[Scratchcard]:
    new_bucket = []
    for c in bucket:
        new_bucket.extend(get_win(c, all_cards))

    if not len(new_bucket):
        return bucket
    
    return bucket + recursive_card_list_creation(new_bucket, all_cards)

def iterative_card_list_creation(initial_bucket: list[Scratchcard], all_cards: list[Scratchcard]) -> list[Scratchcard]:
    tmp_bucket = initial_bucket + [] # make copy
    final_bucket = []

    for c in tmp_bucket:
        tmp_bucket.extend(get_win(c, all_cards))
        final_bucket.append(c)
    
    return final_bucket

def compute_card_number_stack(cards: list[Scratchcard]) -> int:

    counter = 0
    stack = []

    for c in cards:
        counter += 1
        stack.append(c)
    
    while len(stack):
        c = stack.pop()
        for nc in get_win(c, cards):
            counter += 1
            stack.append(nc)
    
    return counter

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

    assert len(recursive_card_list_creation(test_cards, test_cards)) == 30
    assert len(iterative_card_list_creation(test_cards, test_cards)) == 30
    assert compute_card_number_stack(test_cards) == 30

    t0 = time.time()
    total = len(recursive_card_list_creation(cards, cards))
    t1 = time.time()
    time_elapsed = t1-t0
    print(f'part2 RECUSRIVE total = {total} computed in {time_elapsed} s')

    t0 = time.time()
    total = len(iterative_card_list_creation(cards, cards))
    t1 = time.time()
    time_elapsed = t1-t0
    print(f'part2 ITERATIVE total = {total} computed in {time_elapsed} s')

    t0 = time.time()
    total = compute_card_number_stack(cards)
    t1 = time.time()
    time_elapsed = t1-t0
    print(f'part2 STACK total = {total} computed in {time_elapsed} s')
    













