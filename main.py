import csv
import matplotlib.pyplot as plt

def read_csv_as_nested_dict(filename):
    data = {}

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            country = row["Country"]
            data[country] = {}

            for year in row:
                if year != "Country":
                    data[country][year] = float(row[year])

    return data

def build_plot_values(data, country):
    years = []
    gdp_values = []

    for year, gdp in data[country].items():
        years.append(int(year))
        gdp_values.append(gdp)

    return years, gdp_values

def build_plot_dict(data, countries):
    plot_dict = {}

    for country in countries:
        years, gdp_values = build_plot_values(data, country)

        plot_dict[country] = {
            "x": years,
            "y": gdp_values
        }

    return plot_dict

def style():
    plt.title("GDP Line Plot")
    plt.xlabel("Year")
    plt.ylabel("GDP")
    plt.grid(True)

if __name__ == "__main__":
    data = read_csv_as_nested_dict("gdp.csv")

    countries = ["India", "USA", "China"]

    plot_dict = build_plot_dict(data, countries)

    for country in plot_dict:
        plt.plot(
            plot_dict[country]["x"],
            plot_dict[country]["y"],
            label=country
        )

    style()
    plt.legend()
    plt.show()