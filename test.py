from main import (
    read_csv_as_nested_dict,
    build_plot_values,
    build_plot_dict,
    style
)


def test_read_csv_as_nested_dict():
    data = read_csv_as_nested_dict("gdp.csv")

    assert isinstance(data, dict)
    assert "India" in data
    assert isinstance(data["India"], dict)


def test_build_plot_values():
    data = read_csv_as_nested_dict("gdp.csv")

    years, gdp_values = build_plot_values(data, "India")

    assert isinstance(years, list)
    assert isinstance(gdp_values, list)
    assert len(years) == len(gdp_values)


def test_build_plot_dict():
    data = read_csv_as_nested_dict("gdp.csv")

    countries = ["India", "USA", "China"]

    plot_dict = build_plot_dict(data, countries)

    assert isinstance(plot_dict, dict)
    assert "India" in plot_dict
    assert "USA" in plot_dict
    assert "China" in plot_dict


def test_style():
    style()