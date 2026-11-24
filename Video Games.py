import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\TAMILARASI\Downloads\Video+Game+Sales\vgchartz-2024.csv")
print(df.head())

print("Original Data:")
print(df.head())


print("\nMissing Values:")
print(df.isnull().sum())


df = df.drop_duplicates()


numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())


text_cols = df.select_dtypes(include=['object']).columns

for col in text_cols:
    df[col] = df[col].fillna("Unknown")


df = df.dropna(how='all')

print("\nCleaned Data:")
print(df.head())


if 'genre' in df.columns:

    genre_count = df['genre'].value_counts().head(10)

    plt.figure(figsize=(10,6))
    colors=['red','blue','green','orange','purple','pink','cyan','yellow','brown','gray']

    plt.bar(
        genre_count.index,
        genre_count.values,
        color=colors
    )

    plt.xlabel("Genre")
    plt.ylabel("Count")
    plt.title("Top 10 Video Game Genres")

    plt.xticks(rotation=45)

    plt.show()


if 'total_sales' in df.columns:

    plt.figure(figsize=(8,5))

    plt.hist(df['total_sales'], bins=20,color='pink',edgecolor='black')

    # Set horizontal axis from 0 to 5
    plt.xlim(0,5)

    plt.xlabel("Global Sales")
    plt.ylabel("Frequency")
    plt.title("Distribution of Game Sales")

    plt.show()

if 'genre' in df.columns:

    genre_count = df['genre'].value_counts().head(5)

    plt.figure(figsize=(7,7))

    colors = ['red','blue','green','orange','purple']

    plt.pie(
        genre_count.values,
        labels=genre_count.index,
        autopct='%1.1f%%',
        colors=colors
    )

    plt.title("Genre Distribution")

    plt.show()



if 'total_sales' in df.columns:

    sales = df['total_sales'].head(20)

    plt.figure(figsize=(10,5))

    plt.plot(
        sales,
        marker='o',
        color='green'
    )

    plt.xlabel("Game Number")
    plt.ylabel("Sales")
    plt.title("Sales Trend")

    plt.grid()

    plt.show()



if (
'critic_score' in df.columns and
'total_sales' in df.columns
):

    plt.figure(figsize=(8,5))

    plt.scatter(
        df['critic_score'],
        df['total_sales'],
        color='purple'
    )

    plt.xlabel("Critic Score")
    plt.ylabel("Total Sales")
    plt.title("Critic Score vs Total Sales")

    plt.show()





    
