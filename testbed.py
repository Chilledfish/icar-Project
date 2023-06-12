import pandas as pd

df = pd.DataFrame(
	{
		"city": ["London", "Amsterdam", "New York", None],
		"sales": [100, 300, 200, 400],
	}
)


def calculate_total_sales(df):
	return df["sales"].sum()


def create_top_city_leaderboard(df):
	return (
		df.dropna(subset=["city"])
		.sort_values(by=["sales"], ascending=False)
	)


calculate_total_sales(df)

create_top_city_leaderboard(df)
