from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_dynamic_url_updated_by_user(server):
    """
    Test that when the user change the grid size and the words number,
    the URL is dynamically updated to reflect the user choices.
    """
    server.get('http://hidden-words.fr/')

    grid_choices = server.find_element(By.ID, 'grid-size')
    words_number_choices = server.find_element(By.ID, 'words-number')

    select_grid = Select(grid_choices)
    select_words_number = Select(words_number_choices)
    select_grid.select_by_visible_text('20 x 20')
    select_words_number.select_by_value('8')

    assert "https://4is90gmk99.execute-api.eu-west-1.amazonaws.com" \
           "/production/generate-file?grid-size=20&amp;words-number=8" in \
           server.page_source
