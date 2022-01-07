from app.hidden_words import GridGenerator


class TestGridGenerator:
    def test_init(self):
        grid = GridGenerator(10, 20)
        first_dictionary = grid.all_words_in_dict[0]

        assert isinstance(grid.all_words_in_dict, list)
        assert isinstance(first_dictionary, dict)
        assert isinstance(grid.all_words, list)
        assert len(grid.random_words) == 10
        assert len(grid.grid) == grid.grid_size

    def test_create_full_grid(self):
        grid = GridGenerator(10, 20)
        populated_grid = grid.create_full_grid()

        assert len(populated_grid) == grid.grid_size
        assert populated_grid[0][0].isalpha()
        assert populated_grid[19][19].isalpha()
