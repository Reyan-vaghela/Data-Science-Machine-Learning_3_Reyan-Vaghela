import pandas as pd

data = {
    'Subject': ['Math', 'Math', 'Science', 'Science', 'English', 'English'],
    'Student': ['Reyan', 'Dev', 'Reyan', 'Dev', 'Reyan', 'Dev'],
    'Score': [74, 80, 68, 98, 80, 95]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

def coefficient_of_variation(series):
    return series.std() / series.mean() if series.mean() != 0 else 0

grouped = df.groupby('Subject')

result = grouped['Score'].agg(coefficient_of_variation)

print("\nCoefficient of Variation for Exam Scores by Subject:")
print(result)