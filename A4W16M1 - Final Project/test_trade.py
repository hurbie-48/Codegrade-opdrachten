from tradereporter import Reporter  # Assumes your class code is in reporter.py


def test_total_amount_of_products_real_db():
    reporter = Reporter()
    result_of_query = reporter.total_amount_of_products()
    assert result_of_query == 19


def test_country_with_most_trade_records():
    reporter = Reporter()
    result_of_query = reporter.country_with_most_trade_records()
    assert result_of_query.name == "USA"


def test_product_with_highest_trade_value():
    reporter = Reporter()
    result_of_query = reporter.product_with_highest_trade_value()
    expected_title = (
        "MACHINERY AND MECHANICAL APPLIANCES; ELECTRICAL EQUIPMENT; PARTS "
        "THEREOF; SOUND RECORDERS AND REPRODUCERS, TELEVISION IMAGE AND "
        "SOUND RECORDERS AND REPRODUCERS, AND PARTS AND ACCESSORIES OF "
        "SUCH ARTICLES"
    )
    assert result_of_query.title == expected_title


def test_country_with_highest_export_value():
    reporter = Reporter()
    result_of_query = reporter.country_with_highest_export_value()
    assert result_of_query.name == "China"
